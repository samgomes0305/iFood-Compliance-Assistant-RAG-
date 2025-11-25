# criar_db.py
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

PASTA_BASE = "base"
CAMINHO_DB = "db"

def criar_db():
    # Apaga o DB anterior para evitar duplicados
    if os.path.exists(CAMINHO_DB):
        shutil.rmtree(CAMINHO_DB)

    documentos = carregar_documentos()
    if documentos:
        chunks = dividir_chunks(documentos)
        vetorizar_chunks(chunks)

def carregar_documentos():
    if not os.path.exists(PASTA_BASE):
        os.makedirs(PASTA_BASE)
        print(f"⚠️ Pasta '{PASTA_BASE}' criada. Coloque os PDFs lá.")
        return []
        
    carregador = PyPDFDirectoryLoader(PASTA_BASE)
    documentos = carregador.load()
    print(f"📄 Carregou {len(documentos)} páginas.")
    return documentos

def dividir_chunks(documentos):
    separador = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )

    chunks = separador.split_documents(documentos)

    # Embeddings do Google não precisam de "query:" e "passage:"
    print(f"✂️ Total de chunks criados: {len(chunks)}")
    return chunks

def vetorizar_chunks(chunks):
    print("🧠 Criando embeddings com Google text-embedding-004...")

    embedding_model = GoogleGenerativeAIEmbeddings(
        model="text-embedding-004"
    )

    Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CAMINHO_DB
    )

    print("✅ Banco de Dados vetorial criado com sucesso!")

if __name__ == "__main__":
    criar_db()
