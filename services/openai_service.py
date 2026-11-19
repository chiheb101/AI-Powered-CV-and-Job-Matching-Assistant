
import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

# OpenAI client for job-posting web search
client = OpenAI(api_key=API_KEY)

# LangChain model for the assistant
llm = ChatOpenAI(
    model="gpt-4.1",
    api_key=API_KEY
)
