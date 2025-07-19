# Mysql-Ai-Chatbot
Offline SQL chatbot using Gemma3, LangChain &amp; Streamlit
🤖 MySQL Chatbot (Free, Local, No Cloud/No API Key)
A fully offline, open-source chatbot built with Python, Streamlit, LangChain, and Ollama’s Gemma3 AI for querying your MySQL database in plain English, with a modern Instagram- or WhatsApp-style chat UI.

🚀 Features
Conversational AI interface for your database (ask and follow up naturally)

Powered by Gemma3 LLM via Ollama (NO OpenAI account, no cloud, no API keys)

Streamlit web app with chat bubbles and chat history (dark and light themes)

100% runs totally on your local machine (privacy + free)

Robust error handling: empty queries, invalid tables, and output parsing errors are managed

📁 Folder Structure
text
my-ai-sql-chatbot/
├── app.py              # Streamlit UI (modern chat bubbles)
├── langchain_chat.py   # AI agent (LangChain + Ollama + MySQL)
├── requirements.txt    # All Python dependencies
├── test_mysql.py       # Quick MySQL test script
├── README.md           # (You are reading this!)
🛠️ Setup Instructions
1. Install Ollama + a Model
Download Ollama: https://ollama.com/download

Install and open a terminal, then pull a model:

text
ollama pull gemma3
Or for faster responses, try:

text
ollama pull phi3
ollama pull mistral
Start the model:

text
ollama run gemma3
# or ollama run phi3
2. Clone and Install Python Dependencies
bash
git clone https://github.com/your-username/your-repo-name.git
cd my-ai-sql-chatbot
pip install -r requirements.txt
3. Configure Your MySQL Database
Update the connection string in langchain_chat.py if needed:

python
engine = create_engine("mysql+pymysql://root:@localhost/sampledb")
Make sure your database and employees table exist and are populated for best results.

4. Run the App
In terminal:

bash
python -m streamlit run app.py
Open your browser at http://localhost:8501.

💬 Example Questions to Try
"List all employees"

"How many managers are there?"

"Show employees older than 30"

"What is the average age of employees?"

"List all engineers"

"Who is the youngest employee?"

🎨 UI Highlights
Modern, dark theme

User and AI messages display in colored bubbles (right/left, like messaging apps)

Scrollable chat history

"Clear Chat" button to start fresh

🔒 Privacy & Local-Only AI
Everything runs locally on your machine:

No questions, data, or results are ever sent to any cloud service

Your database credentials are safe and only on your device

🧠 Built With
Python 3.10+

MySQL (or SQLite, if preferred)

Streamlit (UI)

LangChain (agent framework)

Ollama + Gemma3/phi3/mistral (local LLM)

SQLAlchemy, pymysql

📦 Requirements
All Python dependencies are in requirements.txt:

text
streamlit
langchain
langchain-community
sqlalchemy
pymysql
mysql-connector-python
📝 Sample employee table structure
Make sure your database includes a structure like:

sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    role VARCHAR(100),
    age INT
);
💡 Notes & Troubleshooting
Use phi3 or mistral models for faster responses if Gemma3 is slow on your laptop

If you get a parsing error, just re-ask, simplify the prompt, or increase max_iterations in langchain_chat.py

Best results come from clear, table-matching column names and questions

📷 Demo Screenshot
