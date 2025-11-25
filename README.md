# 🛡️ iFood Compliance Assistant (RAG)

Assistente Jurídico Inteligente para Entregadores, capaz de responder dúvidas sobre Termos de Uso e Políticas com base em documentos oficiais, utilizando Llama 3 e Busca Semântica.

---

## 🧠 Sobre o Projeto

Este projeto é um sistema de RAG (Retrieval-Augmented Generation) desenvolvido para resolver o desafio de acesso à informação em documentos regulatórios extensos. Ele permite que entregadores tirem dúvidas complexas (ex: "O que acontece se eu ficar inativo?") e recebam respostas precisas e fundamentadas nas regras oficiais do iFood.

---

## 🚀 Stack Tecnológica

- **Interface:** Gradio (Chat Interface)
- **LLM (Cérebro):** Llama-3.1-8b (via Groq LPU - Inferência ultra-rápida)
- **Embeddings (Memória):** Google Gemini text-embedding-004 (Alta precisão semântica)
- **Vector Store:** ChromaDB (Banco de dados vetorial local)
- **Orquestração:** LangChain

---

## 🏗️ Arquitetura da Solução

O sistema utiliza uma arquitetura de RAG moderna, desacoplando a memória (Google) do raciocínio (Groq) para máxima eficiência e custo zero.

---


---

## ⚡ Como Executar

### Pré-requisitos

- Python 3.9+
- Chaves de API (Gratuitas): Groq Cloud e Google AI Studio.

### Passo a Passo

1. **Clone o repositório**

    ```
    git clone https://github.com/samgomes0305/ifood-compliance-Assistant-RAG.git
    cd ifood-compliance-Assistant-RAG
    ```

2. **Instale as dependências**

    ```
    pip install -r requirements.txt
    ```

3. **Configure as Chaves**

    Crie um arquivo `.env` na raiz e adicione:
    ```
    GROQ_API_KEY=sua_chave_groq
    GOOGLE_API_KEY=sua_chave_google
    ```

4. **Crie o Banco de Dados**

    ```
    python criar_db.py
    ```

5. **Inicie o App**

    ```
    python app_gradio.py
    ```

O sistema abrirá automaticamente no navegador.

---

## 🧪 Exemplo de Uso (Input -> Output)

Cenário: Dúvida sobre regras de inatividade (Baseado nos Termos de 2023/2025).

- **👤 Pergunta:** "O que acontece se eu ficar 60 dias sem rodar?"
- **🤖 Resposta do Agente:**
  > De acordo com os Termos Adicionais, a partir de 25 de setembro de 2023, o iFood iniciou um teste onde contas de entregadores que não realizarem entregas por um período igual ou superior a 60 dias poderão ser congeladas.

---

## 🛠️ Decisões Técnicas

**Por que Gradio?**  
Optei pelo Gradio pela robustez em conexões locais e facilidade de criar interfaces de chat focadas em IA, evitando problemas de WebSocket comuns em outras bibliotecas.

**Por que Google Embeddings?**  
O modelo text-embedding-004 oferece excelente performance para Português (PT-BR) e possui uma janela de contexto generosa, ideal para documentos jurídicos.

**Groq LPU:**  
A utilização da Groq permite inferência em velocidade de tempo real, essencial para a experiência do usuário em suporte.

---

## 📝 Autor

Desenvolvido por Samuel Galvão como projeto de portfólio para Engenharia de GenAI.
