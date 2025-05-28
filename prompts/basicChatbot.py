from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chatHistory = []

while True:
    user_input = input("You: ")
    chatHistory.append(user_input)
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    result = model.invoke(chatHistory)
    chatHistory.append(result.content)
    print(f"Chatbot: {result.content}")

print("Chat history:" + str(chatHistory))
