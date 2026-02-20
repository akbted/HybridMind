import os
from pathlib import Path
from typing import List, Optional, Dict
from dotenv import load_dotenv
from psycopg2 import pool


load_dotenv(override=True)

class ProjectSetting:

    # LLMs (EXTERNAL API)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    HF_TOKEN = os.getenv("HF_TOKEN")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GROK_API_KEY = os.getenv("GROK_API_KEY")


class DBSettings:
    connection_pool = pool.ThreadedConnectionPool(
        minconn=2,
        maxconn=10,
        host=os.getenv("POSTGRES_HOST"),
        port=5432,
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
)

proj_settings = ProjectSetting()
db_settings = DBSettings()