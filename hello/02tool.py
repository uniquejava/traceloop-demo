from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain.tools import tool
from dotenv import load_dotenv
import os
from traceloop.sdk import Traceloop

load_dotenv()

Traceloop.init(app_name="demo-traceloop-app", disable_batch=True)


@tool
def get_weather(location: str) -> str:
    """Get the weather at a location"""
    return f"It's snowy in {location}"


model = init_chat_model(model=os.environ["OPENAI_MODEL"])

model_with_tools = model.bind_tools([get_weather])

messages = [HumanMessage("What's the weather like in Wuhan?")]
ai_msg = model_with_tools.invoke(messages)

for tool_call in ai_msg.tool_calls:
    print(f"Tool: {tool_call['name']}")
    print(f"Args: {tool_call['args']}")
    tool_result = get_weather.invoke(tool_call)
    print(f"Tool result:{tool_result}")
    messages.append(tool_result)

final_response = model_with_tools.invoke(messages)

# The current weather in Wuhan is snowy. Please stay warm and safe!
print(final_response.text)
