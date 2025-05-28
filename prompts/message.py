from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)


messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print("Messages:" + str(messages))
