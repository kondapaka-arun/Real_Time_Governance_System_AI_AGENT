from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

data= pd.read_csv("Bank Branches.csv")

embeddings =OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchian_db_bank_branches" # Changed DB location
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids= []

    for i, row in data.iterrows():
        # Concatenate relevant columns for document content
        document_content = f"District: {row['Districts']}, Nationalized Banks: {row['Nationalized Banks']}, Private Banks: {row['Private Banks']}, Regional Rural Banks: {row['Regional Rural Banks']}, Cooperative Banks: {row['Cooperative Banks']}, ATMs: {row['ATMs']}"
        document = Document(
            page_content=document_content,
            metadata={
                "district": row["Districts"],
                "nationalized_banks": row["Nationalized Banks"],
                "private_banks": row["Private Banks"],
                "regional_rural_banks": row["Regional Rural Banks"],
                "cooperative_banks": row["Cooperative Banks"],
                "atms": row["ATMs"]
            },
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="bank_branches", # Changed collection name
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k":1}
)