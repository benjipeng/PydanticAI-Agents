import os
from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv(".env.local")

agent = Agent(  
    'google-gla:gemini-2.0-flash',
    system_prompt='Be concise, reply with one sentence.', # Get API key from environment
)

result = agent.run_sync('Where does "hello world" come from?')  
print(result.data)
"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""