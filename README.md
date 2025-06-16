🇮🇹 [Leggi in Italiano](#-rag-streamlit-app-con-ollama)  
🇬🇧 [Read in English](#-rag-streamlit-app-with-ollama)


## 🇬🇧 RAG Streamlit App with Ollama

⚠️ This is a personal project created for learning purposes and to explore RAG, Streamlit, and Ollama technologies.

🚀 RAG Streamlit App with Ollama

A Retrieval-Augmented Generation (RAG) application for PDF/DOCX documents, running locally using Ollama, LangChain, and ChromaDB.

🔍 Recommended Model

The app is optimized for: `deepseek-r1:7b`  
This is the model used during development, but you are free to experiment with any Ollama-supported model (e.g., mistral, llama3, etc.).

✨ Key Features

- Temporary upload of PDF/DOCX documents for immediate querying  
- Persistent indexing of documents using ChromaDB  
- Multi-model support through Ollama (deepseek, mistral, llama3, etc.)  
- Intuitive interface built with Streamlit  
- 100% local processing without any cloud dependencies

🛠 Tech Stack

| Technology   | Description                        |
|--------------|------------------------------------|
| Ollama       | Framework for running LLMs locally |
| LangChain    | Framework for building LLM apps    |
| ChromaDB     | Open-source vector database         |
| Streamlit    | Framework to create Python web apps|

🏗 Project Structure

├── app.py # Main application code

├── requirements.txt # Python dependencies

├── .gitignore # Ignore temporary files and chroma_db/

└── chroma_db/ # Indexed documents directory (ignored by git)


🚀 Usage Guide

### Prerequisites

- Install [Ollama](https://ollama.com)
- Download a language model (e.g., `ollama pull deepseek`)

### Launch the App

bash
pip install -r requirements.txt   # Install dependencies
streamlit run app.py              # Run the app

Workflow

    Upload a document (PDF or DOCX)

    Choose between:

        "Ask!" → Query the document temporarily

        "Index Document" → Save the document in the persistent ChromaDB

    Enter your question and receive contextual answers from the LLM


## 🇮🇹 RAG Streamlit App con Ollama

⚠️ Questo è un progetto personale creato per scopi di apprendimento ed esplorazione delle tecnologie RAG, Streamlit e Ollama.
# 🚀 RAG Streamlit App con Ollama

Un'applicazione per il Recupero Aumentato con Generazione (RAG) su documenti PDF/DOCX, in locale grazie a Ollama, LangChain e ChromaDB.

## 🔍 Modello Consigliato
L'applicazione è configurata per funzionare ottimamente con:
deepseek-r1:7b

Questo è il modello specifico utilizzato durante lo sviluppo. Puoi comunque sperimentare con altri modelli supportati da Ollama.

## ✨ Funzionalità principali

- **Caricamento temporaneo** di documenti PDF/DOCX per interrogazione immediata
- **Archiviazione persistente** dei documenti indicizzati in ChromaDB
- **Supporto multi-modello** tramite Ollama (deepseek, mistral, llama3, ecc.)
- **Interfaccia intuitiva** realizzata con Streamlit
- **Elaborazione 100% locale** senza dipendenze da servizi cloud

## 🛠 Stack Tecnologico

| Tecnologia | Descrizione |
|------------|-------------|
| [Ollama](https://ollama.com/) | Framework per eseguire LLM localmente |
| [LangChain](https://www.langchain.com/) | Framework per applicazioni LLM |
| [ChromaDB](https://www.trychroma.com/) | Database vettoriale open-source |
| [Streamlit](https://streamlit.io/) | Framework per creare app web in Python |

## 🏗 Struttura del progetto

├── app.py # Codice principale dell'applicazione

├── requirements.txt # Dipendenze Python

├── .gitignore # Esclude file temporanei e chroma_db/

└── chroma_db/ # Directory dei documenti indicizzati (ignorata da git)


## 🚀 Guida all'uso

### Prerequisiti
1. Installa [Ollama](https://ollama.com/)
2. Scarica un modello LLM (es: `ollama pull deepseek`)

### Avvio dell'applicazione
bash
pip install -r requirements.txt  # Installa le dipendenze
streamlit run app.py            # Avvia l'applicazione

Flusso di lavoro

    Carica un documento (PDF o DOCX)

    Scegli tra:

        "Chiedi!": Interroga il documento temporaneamente

        "Indicizza documento": Aggiungi il documento al database permanente

    Inserisci la tua domanda e ottieni le risposte dal modello LLM
