from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from load_dotenv import load_dotenv
load_dotenv()


class Review(BaseModel):
    name: str
    rating: int
    comment: str

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
structured_model = model.with_structured_output(Review)

response = structured_model.invoke("John gave a 5-star rating and said it's fantastic!")
print(response)
