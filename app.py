import streamlit as st
import tempfile
import os, re, time
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_chroma import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_ollama import ChatOllama
from langchain import hub
from langchain.chains import RetrievalQA

st.title('Sistema di Recupero delle Informazioni (RAG) con PDF e DOCX')
st.write('Prova a porre una domanda sul documento caricato o usa il modello puro.')

max_megabyte = 5
max_dimensione = max_megabyte * 1024 * 1024  # Converti MB in byte

carica_file = st.file_uploader("Carica un file", type=["pdf", "docx"])
domanda = st.text_input("Inserisci la tua domanda: ")

@st.cache_resource
def carica_llm():
    return ChatOllama(model="deepseek-r1:7b")

llm = carica_llm()

# Funzione per processare documento caricato
def processa_documento_temporaneo(file):
    if file.size > max_dimensione:
        st.error(f"Il file è troppo grande. La dimensione massima consentita è {max_megabyte} MB.")
        st.stop()
    
    temp_dir = tempfile.TemporaryDirectory()
    filename = os.path.join(temp_dir.name, file.name)
    with open(filename, 'wb') as f:
        f.write(file.getbuffer())

    try:
        if filename.endswith('.pdf'):   # verifica formato e poi estrae il testo
            loader = PyPDFLoader(filename)
        elif filename.endswith('.docx'):
            loader = Docx2txtLoader(filename)
        else:
            st.error("Formato del file non supportato. Carica un file PDF o DOCX.")
            temp_dir.cleanup()
            st.stop()

        raw_data = loader.load()
        data = [doc for doc in raw_data if doc.page_content and doc.page_content.strip()]

        if not data:
            st.error("Il documento non contiene testo o non è stato caricato correttamente.")
            temp_dir.cleanup()
            st.stop()

        return data, temp_dir
    
    except Exception as e:
        st.error(f"Si è verificato un errore durante il caricamento del documento: {str(e)}")
        temp_dir.cleanup()
        st.stop()

def genera_nome_cartella_univoco(filename):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'\W+', '_', base)  # rimuove caratteri non validi
    base = base[:50]    # Limita la lunghezza del nome della cartella
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f"{base}_{timestamp}"

# Esecuzione LLM o RAG in base alla disponibilità del file
if len(domanda) > 0 and st.button("Chiedi!", type="primary"):
    if carica_file is not None:
        data, temp_dir = processa_documento_temporaneo(carica_file)
        try:
            vectorstore = Chroma.from_documents(data, embedding=GPT4AllEmbeddings())
            retriever = vectorstore.as_retriever()
            qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
            st.markdown("🧠 Modalità: *conoscenza locale attiva* (RAG)")
            risposta = qa_chain.invoke({"query": domanda})
            st.write(risposta["result"])
        except Exception as e:
            st.error(f"Errore durante l'esecuzione della catena RAG: {str(e)}")
        finally:
            temp_dir.cleanup()
    else:
        try:
            st.markdown("💬 Modalità: *modello puro* (LLM standalone)")
            risposta = llm.invoke(domanda)
            st.write(risposta.content)
        except Exception as e:
            st.error(f"Errore durante l'invocazione del modello puro: {str(e)}")

# Bottone per indicizzare il documento caricato
if carica_file is not None and st.button("Indicizza documento", type="primary"):
    try:
        data, temp_dir = processa_documento_temporaneo(carica_file)
        nome_cartella = genera_nome_cartella_univoco(carica_file.name)
        percorso_cartella = os.path.join("chroma_db", nome_cartella)
        if not os.path.exists("chroma_db"):
            os.makedirs("chroma_db")
        os.makedirs(percorso_cartella, exist_ok=True)

        vectorstore_persistente = Chroma.from_documents(
            documents=data,
            embedding=GPT4AllEmbeddings(),
            persist_directory=percorso_cartella
        )
        del vectorstore_persistente
        st.success(f"Documento indicizzato con successo in {nome_cartella}!")
    except Exception as e:
        st.error(f"Errore durante l'indicizzazione del documento: {str(e)}")
    finally:
        temp_dir.cleanup()
