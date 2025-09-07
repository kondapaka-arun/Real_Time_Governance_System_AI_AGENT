It is an agentic architecture, query the data across different districts, providing the answers for the questions and providing the insights for the dataset.


The system operates with a clear separation of concerns and a Retrieval-Augmented Generation (RAG) system for querying.

1.data_transformation.py:
  - Ingests raw  data from .csv file.
  - Performs the operation on the .csv file like cleaning, standardization, transformation.
  - Add new columns like 'total_branches', 'atm_per_branch', and 'market shares', for these columns the data will come from 'branch'/'total_branches' for more analysis.
  - Generates key statistical insights (e.g., districts with least branches, highest ATM coverage).
    *   Visualizes data and saves it as 'branches_chart.png'.
    *   Logs all major steps and notable events to a timestamped log file for transparency and reproducibility.

2.vactor.py file for store and retriever of data.
  - Uses the processed .csv file data to create a vector store.
  - Each row of the .csv file data is converted into a 'Document' with its content embedded using an Ollama-based embedding model (`mxbai-embed-large`).


3.main.py:
 - local AI model OllamaLLM is used for understanding prompts and generating of data.
 - We are using model llama3.2:
 - Imported 'ChatPromptTemplate' for structuring the prompt which is given by user.
 - chain contains the data of both prompt and model(llama3.2).


Agentic Flow:
-----------------------------------------------------------------------------------
- A user asks a question through command line interface or web user interface. 
- CLI send this question to the database by the  help of retriever it finds the suitable records for the question.
- These questions and records passed to the model llama3.2 LLM to generate a answer.


Models Used:
----------------------------------------------------------------------------------
1.Ollama:
    -Ollama is a local AI Model it run LLM models in our system.
    -We used model llama3.2 from OllamaLLM for generating natural language.

2.Third-parties/Resources
	  - Ollama: Installed Ollama model and from that model pulled some specified models like llama3.2 and mxbai-embed-large.
	  - langchain: It is a framework used for building the applications.
	  - lanchain_ollama: Integrates Ollama models with langchain.
	  - Chroma : It is an open source vector database.
	  - lanchain_chroma : is from Chroma it used to interates with vector database with langchain.
	  - langchain_core: It contain core components of langchain.
	  - Pandas: It is library it is used for data manipulation and analysis.
	  - Matplotlib : It is usd for data visualization, it convert data into charts, graphs, etc.


Steps for Installation:
-----------------------------------------------------------------------------------------------
1. Install Ollama and Pull Models:
   -Download and install Ollama from web (https://ollama.ai/).
   -Pull the required models:
      -In terminal :
        -ollama pull mxbai-embed-large (for embedding model)
        -ollama pull llama3.2 (LLM modelused for Q&A)
       

3.  Create Environment:
    -In terminal:
      - python -m venv venv
      - After creating the environment (venv) activate it.
      -.\venv\Scripts\activate
    

4.  Install Python Libraries:
      - pip install pandas
      - pip install matplotlib 
      - pip install tabulate 
      - pip install langchain-ollama langchain-chroma
  
