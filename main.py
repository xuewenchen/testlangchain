from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, custom_tool
from langchain.agents import create_agent

load_dotenv()

@custom_tool
def execute_code(code: str) -> str:
    """Execute python code."""
    return "27"

@custom_tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


llm = ChatOpenAI(model="gpt-5", use_responses_api=True)

agent = create_agent(llm, tools=[get_weather])

data = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
print(data)