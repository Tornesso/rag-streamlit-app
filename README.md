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
```bash
pip install -r requirements.txt  # Installa le dipendenze
streamlit run app.py            # Avvia l'applicazione

Flusso di lavoro

    Carica un documento (PDF o DOCX)

    Scegli tra:

        "Chiedi!": Interroga il documento temporaneamente

        "Indicizza documento": Aggiungi il documento al database permanente

    Inserisci la tua domanda e ottieni le risposte dal modello LLM
