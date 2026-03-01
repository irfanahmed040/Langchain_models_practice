# LangChain Practice Repository

This repository contains hands-on experiments with LangChain, focusing on understanding core components such as LLMs, Chat Models, Embeddings, and Document Similarity.

The objective is to build strong foundational knowledge before implementing advanced systems like Retrieval-Augmented Generation (RAG) pipelines and AI-powered applications.

---

## Overview

This repository demonstrates:

- Basic LLM usage with LangChain  
- Chat model integration (OpenAI and HuggingFace)  
- API-based vs local model execution  
- Embedding generation for queries and documents  
- Semantic similarity computation using vector embeddings  

---

## Project Structure

```
1.LLMs/
    1_llm_demo.py

2.Chat Models/
    1_chatmodel_openai.py
    2_chatmodel_hf_api.py
    3_chatmodel_hf_local.py

3.Embedded Models/
    1_embedding_openai_query.py
    2_embedding_openai_documents.py
    3_embedding_hf_local.py
    4_document_similarity.py
```

---

## Module Breakdown

### 1. LLMs

**1_llm_demo.py**

- Demonstrates basic LLM invocation using LangChain  
- Covers prompt execution and response handling  

---

### 2. Chat Models

**1_chatmodel_openai.py**

- Uses OpenAI chat models within LangChain  

**2_chatmodel_hf_api.py**

- Integrates HuggingFace models via hosted API  

**3_chatmodel_hf_local.py**

- Runs HuggingFace models locally  

Focus areas:

- Difference between LLMs and Chat Models  
- API-based vs local inference  

---

### 3. Embedded Models

**1_embedding_openai_query.py**

- Generates embeddings for query text  

**2_embedding_openai_documents.py**

- Generates embeddings for document collections  

**3_embedding_hf_local.py**

- Creates embeddings using local HuggingFace models  

**4_document_similarity.py**

- Computes similarity scores between documents  
- Demonstrates cosine similarity and vector comparison  

Focus areas:

- Vector representations  
- Semantic similarity  
- Foundation of semantic search systems  

---

## Tech Stack

- Python  
- LangChain  
- OpenAI API  
- HuggingFace Transformers  
- NumPy  
- python-dotenv  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/irfanahmed040/Langchain_models.git
cd Langchain_models
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_key_here
```

---

## Learning Objectives

This repository is part of a structured learning path toward:

- Building Retrieval-Augmented Generation (RAG) systems  
- Implementing semantic search applications  
- Developing AI-powered chat applications  
- Understanding embeddings and vector similarity in depth  
- Working with both cloud-based and local AI models  
