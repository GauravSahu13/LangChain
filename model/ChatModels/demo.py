from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo-instruct")

result= llm.invoke("what is the capital of France?", temperature=0.7, max_completion_tokens=100)

print(result.content)