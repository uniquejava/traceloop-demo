from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

model = init_chat_model(model=os.environ["OPENAI_MODEL"])

res = model.invoke("hi")

print(res)
