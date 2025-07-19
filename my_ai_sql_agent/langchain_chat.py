from sqlalchemy import create_engine
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.llms import Ollama
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

# ✅ MySQL connection
engine = create_engine("mysql+pymysql://root:@localhost/sampledb")
db = SQLDatabase(engine=engine)

# ✅ Local AI: Gemma3 (through Ollama)
llm = Ollama(model="gemma3")

# ✅ Build the toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# ✅ AgentExecutor with speed + safety
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=False,
    handle_parsing_errors=True,  # ✅ Prevent format crash
    max_iterations=100            # ✅ Limit "thinking" rounds for speed
)

# ✅ Function accessed by Streamlit
def ask_database(query: str) -> str:
    return agent_executor.run(query)
