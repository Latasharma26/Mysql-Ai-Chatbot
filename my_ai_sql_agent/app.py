import streamlit as st
from langchain_chat import ask_database

# ✅ Page config
st.set_page_config(page_title="🤖 MySQL ChatBot (Gemma3)", page_icon="🤖", layout="wide")

# ✅ Stylish DARK MODE CSS with modern chat bubble layout
st.markdown("""
    <style>
        body, html, .main, .block-container {
            background-color: #181818 !important;
            color: #ffffff !important;
            font-family: 'Segoe UI', sans-serif;
        }

        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
            padding: 0 5% 2rem 5%;
        }

        .bubble {
            padding: 14px 18px;
            border-radius: 18px;
            max-width: 75%;
            font-size: 16px;
            line-height: 1.5;
            word-wrap: break-word;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }

        .user-bubble {
            background-color: #4a90e2;
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 0;
        }

        .ai-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-start;
            border-bottom-left-radius: 0;
            border: 1px solid #444;
        }

        .stTextInput > div > div > input,
        .stChatInput input {
            background-color: #2c2f33 !important;
            color: #fff !important;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Main Title & Instructions
st.title("🤖 MySQL Chatbot ")
# st.markdown("Ask anything about your employees like: **'How many managers?'**, **'List all employees'**, etc.")

# ✅ Store full chat history 🧠
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ✅ Get user input like ChatGPT
user_query = st.chat_input("💬 Type your message and press Enter...")

# ✅ Handle chat logic
if user_query:
    # Store user message
    st.session_state["messages"].append({"role": "user", "content": user_query})
    with st.spinner("🤖 Thinking..."):
        try:
            reply = ask_database(user_query)
        except Exception as e:
            reply = f"❌ Error: {e}"

    # Store AI response
    st.session_state["messages"].append({"role": "ai", "content": reply})

# ✅ Display all messages beautifully
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state["messages"]:
    bubble_type = "user-bubble" if msg["role"] == "user" else "ai-bubble"
    sender = "🧑 You" if msg["role"] == "user" else "🤖 AI"
    st.markdown(
        f"<div class='bubble {bubble_type}'><b>{sender}:</b><br>{msg['content']}</div>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)

# ✅ Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state["messages"].clear()
    st.rerun()

