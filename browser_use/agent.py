from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv

load_dotenv()

import asyncio

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

# Select LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

# Create agent with the model
agent = Agent(
    #task="Compare the price of gpt-4o and DeepSeek-V3",
    task="open youtube.com and Find the \"Be What You Wanna Be\" video posted by Darin's channel on youtube browser tab, tell me it's URL address",
    #task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
    llm=llm,
    browser=browser,
    use_vision=True,
)

async def main():
    await agent.run()

    input('Press Enter to close the browser')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
