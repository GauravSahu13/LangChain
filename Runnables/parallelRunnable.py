from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="write a tweet about: {topic}",
)
prompt2 = PromptTemplate(
    input_variables=["topic"],
    template="generate a linkedin post about: {topic}",
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
)

parser = StrOutputParser()

chain = RunnableParallel({
   'tweet': RunnableSequence(prompt1, model, parser),
   'post': RunnableSequence(prompt2, model, parser)
})

print(chain.invoke({"topic": "cats"}))
