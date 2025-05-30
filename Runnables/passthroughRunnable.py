from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="write a joke about: {topic}",
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    input_variables=["text"],
    template="explain the following joke: {text}",
)

jokeGenChain = RunnableSequence(prompt1, model, parser)

parallelChain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

finalChain = RunnableSequence(jokeGenChain, parallelChain)

print(finalChain.invoke({"topic": "cats"}))
