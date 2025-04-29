from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

import asyncio

# llm = ChatOpenAI(model="gpt-4o")
# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
