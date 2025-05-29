from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Initialize the Google Generative AI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)


# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="You are a helpful assistant. Answer the question in 5 lines: {topic}",
)

# Create the output parser
parser = StrOutputParser()

# Define the chain that combines the model, prompt, and parser
chain = prompt_template | model | parser

result = chain.invoke({"topic": "cricket"})
print(result)

chain.get_graph().print_ascii()