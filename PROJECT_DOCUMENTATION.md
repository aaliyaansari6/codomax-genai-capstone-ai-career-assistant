# AI Career & Document Assistant

## 1. Introduction

AI Career & Document Assistant is a Generative AI-based application developed as the final capstone project for the Codomax Internship.

The application combines Generative AI, Prompt Engineering, Retrieval-Augmented Generation (RAG), vector search, and AI-agent style decision routing into one Streamlit-based application.

The system can answer general questions, provide career-related assistance, and answer questions from uploaded PDF or TXT documents.

---

## 2. Problem Statement

Students and job seekers often need help with resumes, interviews, career questions, and understanding documents.

Traditional applications may require users to manually search through documents or use different tools for different tasks.

This project provides a single AI-powered interface where users can:

- Ask general questions
- Get career assistance
- Upload documents
- Ask questions about uploaded documents
- Retrieve relevant information from documents
- Receive AI-generated responses

---

## 3. Objectives

The main objectives of the project are:

1. To develop a practical Generative AI application.
2. To implement an AI-agent style decision router.
3. To implement Retrieval-Augmented Generation (RAG).
4. To process PDF and TXT documents.
5. To divide documents into smaller chunks.
6. To create vector representations using TF-IDF.
7. To store and retrieve vectors using ChromaDB.
8. To use Google Gemini for response generation.
9. To provide career and resume assistance.
10. To develop an easy-to-use Streamlit interface.

---

## 4. Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- ChromaDB
- Scikit-learn
- PyPDF
- GitHub

---

## 5. System Architecture

The system follows this architecture:

User
↓
Streamlit Web Interface
↓
AI Agent / Decision Router
↓
Choose Action

### General / Career Request

General or career request
↓
Gemini LLM
↓
AI Response
↓
Streamlit Interface

### Document Question

PDF/TXT Document
↓
Text Extraction
↓
Chunking
↓
TF-IDF Vector Representation
↓
ChromaDB
↓
Similarity Retrieval
↓
Relevant Context
↓
Gemini LLM
↓
AI Response

The architecture diagram is available in:

`architecture-diagram.png`

---

## 6. RAG Implementation

The application uses Retrieval-Augmented Generation (RAG) for document-based questions.

### Step 1: Document Upload

The user uploads a PDF or TXT document through the Streamlit interface.

### Step 2: Text Extraction

Text is extracted from the uploaded document using PyPDF for PDF files.

### Step 3: Chunking

The extracted text is divided into smaller sections or chunks.

This makes it easier to search specific parts of the document.

### Step 4: Vector Representation

The document chunks are converted into numerical vector representations using TF-IDF.

### Step 5: Vector Storage

The vector representations are stored in ChromaDB.

### Step 6: Retrieval

When the user asks a question, the system searches for the most relevant document chunks.

### Step 7: Context Generation

The retrieved chunks are provided as context to the Gemini model.

### Step 8: Response Generation

Gemini generates an answer based on the retrieved document context.

---

## 7. AI Agent / Decision Router

The application contains an AI-agent style decision-making component.

The decision router analyzes the user's request and selects an appropriate action.

The main routes are:

- Document-related request
- Career-related request
- General request

For document questions, the system uses the RAG pipeline.

For career and general questions, the system sends the request directly to Gemini with an appropriate prompt.

---

## 8. Career Assistance

The application can assist users with:

- Resume improvement
- Resume-related questions
- Interview preparation
- Career guidance
- LinkedIn profile assistance
- Cover letter writing
- Job-related questions

---

## 9. User Interface

The application is developed using Streamlit.

The interface provides:

- Chat interface
- Document upload
- Document processing
- Conversation history
- Clear chat option
- Project information section
- AI-generated responses

---

## 10. Security

The Gemini API key is stored using Streamlit Secrets.

The API key is not hard-coded into the source code or uploaded to GitHub.

This helps protect sensitive credentials.

---

## 11. Testing

The application was designed to test the following scenarios:

### Test 1: General Question

Input:
"Explain artificial intelligence in simple terms."

Expected result:
The application generates a general AI explanation.

### Test 2: Career Question

Input:
"Give me tips for preparing for a technical interview."

Expected result:
The application provides interview preparation guidance.

### Test 3: Document Question

Upload a PDF or TXT document and ask a question related to its content.

Expected result:
The application retrieves relevant information from the document and generates an answer using the retrieved context.

### Test 4: Conversation

Ask multiple questions in the same session.

Expected result:
The application maintains conversation history during the session.

---

## 12. Advantages

- Combines multiple Generative AI concepts in one application.
- Provides document-based question answering.
- Provides career assistance.
- Uses vector-based document retrieval.
- Easy-to-use web interface.
- Supports PDF and TXT documents.
- Keeps API credentials separate from source code.

---

## 13. Limitations

- Document retrieval depends on the quality of the extracted text.
- Very large documents may require additional optimization.
- TF-IDF provides lexical similarity rather than deep semantic embeddings.
- The application requires access to the Gemini API for AI-generated responses.

---

## 14. Future Enhancements

Future versions can include:

- Advanced semantic embedding models
- Support for DOCX documents
- Multiple document collections
- User authentication
- Persistent user accounts
- More advanced AI-agent tools
- Job description analysis
- Automated resume scoring
- Interview simulation
- Voice-based interaction

---

## 15. Learning Outcomes

Through this project, the following concepts were implemented and practiced:

- Generative AI
- Large Language Models
- Prompt Engineering
- API Integration
- Retrieval-Augmented Generation
- Vector Search
- ChromaDB
- Document Processing
- AI Agent Concepts
- Streamlit Application Development
- GitHub Project Management
- Secure API Key Management

---

## 16. Conclusion

The AI Career & Document Assistant demonstrates how Generative AI can be combined with document retrieval and AI-agent concepts to create a practical application.

The project integrates Gemini, RAG, TF-IDF vector representation, ChromaDB, document processing, and Streamlit into a single system.

It provides users with an interactive platform for general questions, career assistance, and document-based question answering.

This project helped demonstrate the practical application of concepts learned throughout the Codomax Generative AI Internship.
