import gradio as gr
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# --- Carregamento Inicial ---
load_dotenv()
CAMINHO_DB = "db"

# Inicializa embedding e banco
embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

if not os.path.exists(CAMINHO_DB):
    raise RuntimeError(f"⚠️ Banco de dados '{CAMINHO_DB}' não encontrado. Rode o criar_db.py primeiro.")

db = Chroma(persist_directory=CAMINHO_DB, embedding_function=embedding)

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.1
)

template = ChatPromptTemplate.from_template("""
Você é um Assistente Jurídico Sênior do iFood.
Responda à pergunta do entregador com base APENAS no contexto abaixo.
Se a resposta não estiver no contexto, diga que o documento não informa.
Seja direto, profissional e empático.

CONTEXTO OFICIAL:
{contexto}

PERGUNTA DO USUÁRIO:
{pergunta}
""")

# --- Função de resposta para Gradio ---

def responder(pergunta, chat_history=None):
    try:
        # Busca documentos relevantes para contexto (não exibe trechos ao usuário)
        resultados = db.similarity_search_with_relevance_scores(pergunta, k=4)
        if not resultados:
            contexto = ""
            resposta_final = "⚠️ Não encontrei trechos relevantes nos documentos oficiais. Respondendo com base na minha expertise."
        else:
            contexto = "\n\n---\n\n".join([doc.page_content for doc, score in resultados])
            chain = template | llm
            resposta = chain.invoke({"contexto": contexto, "pergunta": pergunta})
            resposta_final = resposta.content

        return resposta_final
    except Exception as e:
        return f"Erro ao processar: {e}"

# --- Interface Gradio tipo Chat ---

gr.ChatInterface(
    responder,
    title="🛡️ Assistente de Compliance iFood",
    description="Consultor jurídico para entregadores do iFood.\nPowered by Groq & Google Embeddings.\n",
    chatbot=gr.Chatbot(),
    textbox=gr.Textbox(placeholder="Digite sua dúvida sobre os Termos de Uso...", container=False)
).launch()
