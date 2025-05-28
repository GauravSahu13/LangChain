from langchain_google_genai import ChatGoogleGenerativeAI
from load_dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
result = model.invoke("what is the capital of France?")      

print(result.content)