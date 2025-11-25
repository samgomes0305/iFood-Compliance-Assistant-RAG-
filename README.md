# 🛡️ iFood Compliance Assistant (RAG)

Assistente Jurídico Inteligente para Entregadores, capaz de responder dúvidas sobre Termos de Uso e Políticas com base em documentos oficiais, utilizando **Llama 3** e **Busca Semântica**.

---

## 🧠 Sobre o Projeto

Este projeto é um sistema de **RAG (Retrieval-Augmented Generation)** criado para resolver o desafio de acesso à informação em documentos extensos.

Ele permite que entregadores façam perguntas complexas — como:

> "O que acontece se eu ficar inativo?"

E recebam respostas **precisas, contextualizadas e fundamentadas** nos documentos oficiais do iFood.

---

## 🚀 Stack Tecnológica

- **Interface:** Gradio (Chat Interface)
- **LLM:** Llama-3.1-8B via **Groq LPU**
- **Embeddings:** Google Gemini **text-embedding-004**
- **Vector Store:** ChromaDB (local)
- **Orquestração:** LangChain

---

## 🏗️ Arquitetura da Solução

O sistema utiliza uma arquitetura de RAG moderna, desacoplando **memória (Embeddings)** do **raciocínio (LLM)**.

```mermaid
graph TD
    A[PDF: Termos de Uso] -->|Splitter & Embeddings| B(Google Gemini API)
    B -->|Vetores| C{ChromaDB Local}
    D[Usuário: Pergunta] -->|Embeddings| B
    B -->|Vetor da Pergunta| C
    C -->|Recupera Top-4 Trechos| E[Contexto]
    E -->|Contexto + Pergunta| F[LLM: Llama-3 (Groq)]
    F -->|Resposta| G[Interface Gradio]

⚡ Como Executar
🔧 Pré-requisitos

Python 3.9+

Chaves de API:

GROQ_API_KEY

GOOGLE_API_KEY

📌 Passo a Passo
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/ifood-compliance-rag.git
cd ifood-compliance-rag

2️⃣ Instale as dependências
pip install -r requirements.txt

3️⃣ Configure o arquivo .env

Crie um arquivo .env contendo:

GROQ_API_KEY=sua_chave_groq
GOOGLE_API_KEY=sua_chave_google

4️⃣ Gere o banco vetorial
python criar_db.py

5️⃣ Inicie o aplicativo
python app_gradio.py

🧪 Exemplo de Uso

Pergunta:
"O que acontece se eu ficar 60 dias sem rodar?"

Resposta:

“De acordo com os Termos Adicionais, contas que não realizarem entregas por 60 dias podem ser congeladas.
A reativação pode ser solicitada pelo aplicativo.”

🛠️ Decisões Técnicas
✔️ Por que Gradio?

Simples

Estável

Ótimo para interfaces de chat IA

✔️ Por que Google Embeddings?

Alto desempenho em PT-BR

0 custo na camada gratuita

Excelente para textos jurídicos

✔️ Por que Groq?

Inferência em tempo real

Experiência de suporte fluída

📝 Autor

Desenvolvido por Samuel Galvão como projeto de portfólio para Engenharia de GenAI.
