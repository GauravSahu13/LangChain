from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    input_variables=["topic"],
    template="write a joke about: {topic}",
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
)

parser = StrOutputParser()

jokeGenChain = RunnableSequence(prompt, model, parser)

parallelChain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'wordCount': RunnableLambda(lambda x: len(x.split()))
})

finalChain = RunnableSequence(jokeGenChain, parallelChain)

result = finalChain.invoke({'topic':'cats'})

final_result = """{} \n word count - {}""".format(result['joke'], result['wordCount'])

print(final_result)
