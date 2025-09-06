from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from data_transformation import data

from vector import retriever # Corrected retriever import
model = OllamaLLM(model='llama3.2')

template="""You are an expert in answering questions for bank branch availability and ATM availability across different districts, based on the provided data.

Here are some relevant bank branch details: {reviews}

Here is the question to answer: {question}"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    question= input("Ask a question about bank branches (enter 'q' or 'exit' to quit) ?")
    if question== "q" or question == "exit":
        break

    reviews = retriever.invoke(question) # Corrected variable name
    results = chain.invoke({"reviews": reviews, "question": question})

    print(results)