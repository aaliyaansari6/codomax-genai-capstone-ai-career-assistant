# 🤖 AI Career & Document Assistant

A Generative AI Capstone Project developed as part of the Codomax Internship.

## 📌 Project Overview

The AI Career & Document Assistant is a Generative AI application that combines LLM APIs, Prompt Engineering, RAG, vector databases, and AI-agent style routing into one application.

The application can provide general AI assistance, career guidance, and answers based on uploaded documents.

## ✨ Features

- 💬 AI-powered chat assistant
- 📄 PDF and TXT document upload
- 🔎 Document-based question answering
- 🧠 Retrieval-Augmented Generation (RAG)
- 🗄️ ChromaDB vector database
- ✂️ Document chunking
- 🤖 AI agent decision routing
- 💼 Career and resume assistance
- ✍️ Prompt-based content generation
- 🧠 Conversation history
- 🌐 Streamlit web interface
- 🔐 Secure Gemini API key management

## 🏗️ Architecture

User
↓
Streamlit Interface
↓
AI Agent / Decision Router
↓
Choose Action
↓
General Chat / Career Assistant / Document Q&A
↓
Gemini LLM or RAG Pipeline
↓
Final Response

### RAG Pipeline

Document
→ Text Extraction
→ Chunking
→ Vector Representation
→ ChromaDB
→ Similarity Retrieval
→ Relevant Context
→ Gemini
→ Answer

## 🛠️ Technologies

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- ChromaDB
- Scikit-learn
- PyPDF
- GitHub

## 🔐 API Key Security

The Gemini API key is stored securely using Streamlit Secrets.

It is not included in the GitHub repository.

Example:

```toml
GEMINI_API_KEY = "your_api_key_here"
