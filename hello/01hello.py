from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from dotenv import load_dotenv
import os
from traceloop.sdk import Traceloop

load_dotenv()

# Traceloop.init(app_name="demo-traceloop-app", disable_batch=True)

# OPENAI_MODEL=ollama:qwen2.5:3b
model = init_chat_model(model=os.environ["OPENAI_MODEL"])

res = model.invoke(input=[HumanMessage("Tell me a joke about OpenTelemetry")])

print(res.content)
