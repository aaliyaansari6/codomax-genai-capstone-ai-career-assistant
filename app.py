import streamlit as st
from google import genai
import chromadb
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer


# =========================
# PAGE SETUP
# =========================

st.set_page_config(
    page_title="AI Career & Document Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career & Document Assistant")
st.caption("Codomax Internship – GenAI Capstone Project")


# =========================
# GEMINI
# =========================

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


# =========================
# VECTOR DATABASE
# =========================

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="career_documents"
)


# =========================
# SESSION STATE
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorizer" not in st.session_state:
    st.session_state.vectorizer = None


# =========================
# DOCUMENT FUNCTIONS
# =========================

def extract_text(file):

    if file.name.lower().endswith(".pdf"):

        reader = PdfReader(file)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    return file.read().decode("utf-8")


def chunk_text(text, size=1000, overlap=200):

    chunks = []

    start = 0

    while start < len(text):

        chunk = text[start:start + size].strip()

        if chunk:
            chunks.append(chunk)

        start += size - overlap

    return chunks


def process_documents(files):

    all_chunks = []

    for file in files:

        text = extract_text(file)

        if text.strip():

            chunks = chunk_text(text)

            all_chunks.extend(chunks)

    if not all_chunks:
        return 0

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        all_chunks
    ).toarray()

    # Clear old documents
    old_ids = collection.get()["ids"]

    if old_ids:
        collection.delete(ids=old_ids)

    collection.add(
        documents=all_chunks,
        embeddings=vectors.tolist(),
        ids=[
            f"document_chunk_{i}"
            for i in range(len(all_chunks))
        ]
    )

    st.session_state.vectorizer = vectorizer

    return len(all_chunks)


def retrieve_context(question, top_k=4):

    vectorizer = st.session_state.vectorizer

    if vectorizer is None:
        return []

    question_vector = vectorizer.transform(
        [question]
    ).toarray()

    if collection.count() == 0:
        return []

    results = collection.query(
        query_embeddings=question_vector.tolist(),
        n_results=min(top_k, collection.count())
    )

    return results["documents"][0]


# =========================
# AI AGENT ROUTER
# =========================

def decide_action(user_input):

    text = user_input.lower()

    document_words = [
        "document",
        "resume",
        "cv",
        "uploaded",
        "file",
        "according to"
    ]

    career_words = [
        "resume",
        "cv",
        "career",
        "job",
        "interview",
        "skills",
        "linkedin",
        "cover letter"
    ]

    if any(word in text for word in document_words):
        return "document"

    if any(word in text for word in career_words):
        return "career"

    return "general"


# =========================
# GEMINI RESPONSE
# =========================

def generate_answer(prompt):

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


# =========================
# SIDEBAR
# =========================

st.sidebar.header("📄 Document Center")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF or TXT documents",
    type=["pdf", "txt"],
    accept_multiple_files=True
)


if st.sidebar.button("📥 Process Documents"):

    if not uploaded_files:

        st.sidebar.warning(
            "Please upload a document first."
        )

    else:

        with st.spinner(
            "Reading and indexing documents..."
        ):

            try:

                count = process_documents(
                    uploaded_files
                )

                st.sidebar.success(
                    f"{count} document chunks processed."
                )

            except Exception as e:

                st.sidebar.error(
                    f"Error: {e}"
                )


if st.sidebar.button("🗑️ Clear Documents"):

    try:

        ids = collection.get()["ids"]

        if ids:
            collection.delete(ids=ids)

        st.session_state.vectorizer = None

        st.sidebar.success(
            "Document database cleared."
        )

    except Exception as e:

        st.sidebar.error(
            f"Error: {e}"
        )


st.sidebar.divider()

st.sidebar.subheader("🤖 Agent Capabilities")

st.sidebar.write("💬 General AI Chat")
st.sidebar.write("📄 Document Q&A")
st.sidebar.write("💼 Career Assistance")
st.sidebar.write("✍️ Resume Improvement")


# =========================
# MAIN INTERFACE
# =========================

tab1, tab2 = st.tabs(
    [
        "💬 AI Assistant",
        "📊 Project Information"
    ]
)


with tab1:

    st.subheader(
        "Ask the AI Career & Document Assistant"
    )

    # Display history

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


    user_input = st.chat_input(
        "Ask about your career, resume, or documents..."
    )


    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        with st.chat_message("user"):

            st.markdown(user_input)


        try:

            with st.spinner(
                "AI Agent is thinking..."
            ):

                # Agent decides what action to take

                action = decide_action(
                    user_input
                )


                # =========================
                # DOCUMENT AGENT
                # =========================

                if action == "document":

                    context_chunks = retrieve_context(
                        user_input
                    )

                    if context_chunks:

                        context = "\n\n---\n\n".join(
                            context_chunks
                        )

                        prompt = f"""
You are a document analysis assistant.

Answer the user's question using ONLY
the provided document context.

If the information is not available,
say that you could not find it.

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{user_input}
"""

                    else:

                        prompt = f"""
The user wants information about a document,
but no processed document information is available.

Politely explain that the user should upload
and process a document first.

USER QUESTION:
{user_input}
"""


                # =========================
                # CAREER AGENT
                # =========================

                elif action == "career":

                    prompt = f"""
You are an AI Career Assistant.

Help the user with resumes, job applications,
interviews, LinkedIn profiles, career planning,
professional summaries and cover letters.

Give practical, professional and easy-to-understand
advice.

USER REQUEST:
{user_input}
"""


                # =========================
                # GENERAL AGENT
                # =========================

                else:

                    prompt = f"""
You are a helpful Generative AI assistant.

Answer clearly and accurately.

USER REQUEST:
{user_input}
"""


                answer = generate_answer(
                    prompt
                )


            with st.chat_message(
                "assistant"
            ):

                st.markdown(answer)


            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )


        except Exception as e:

            st.error(
                f"Error: {e}"
            )


with tab2:

    st.subheader(
        "🏗️ GenAI Capstone Architecture"
    )

    st.markdown(
        """
### Application Flow

**User**

↓

**Streamlit Interface**

↓

**AI Agent / Decision Router**

↓

**Choose Action**

├── 💬 General Chat → Gemini LLM

├── 💼 Career Request → Gemini LLM

└── 📄 Document Question

&nbsp;&nbsp;&nbsp;&nbsp;↓

&nbsp;&nbsp;&nbsp;&nbsp;Document Chunking

&nbsp;&nbsp;&nbsp;&nbsp;↓

&nbsp;&nbsp;&nbsp;&nbsp;Vector Representation

&nbsp;&nbsp;&nbsp;&nbsp;↓

&nbsp;&nbsp;&nbsp;&nbsp;ChromaDB

&nbsp;&nbsp;&nbsp;&nbsp;↓

&nbsp;&nbsp;&nbsp;&nbsp;Relevant Context

&nbsp;&nbsp;&nbsp;&nbsp;↓

&nbsp;&nbsp;&nbsp;&nbsp;Gemini LLM

&nbsp;&nbsp;&nbsp;&nbsp;↓

&nbsp;&nbsp;&nbsp;&nbsp;Final Answer
        """
    )

    st.subheader("🎯 Technologies")

    st.write(
        """
        • Python  
        • Streamlit  
        • Google Gemini API  
        • Retrieval-Augmented Generation (RAG)  
        • ChromaDB  
        • TF-IDF vector representation  
        • PDF processing  
        • Prompt Engineering  
        • AI Agent routing
        """
    )
