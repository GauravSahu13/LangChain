from langchain_anthropic import ChatAnthropic
from load_dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-2", temperature=0.7)
result = model.invoke("what is the capital of France?", max_completion_tokens=100)

print(result.content)