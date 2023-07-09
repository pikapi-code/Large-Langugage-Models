from dotenv import load_dotenv

import langchain
from langchain.llms import OpenAI
from langchain.cache import SQLiteCache, InMemoryCache
from langchain.callbacks import get_openai_callback

load_dotenv()

llm = OpenAI(model_name="text-davinci-002")

langchain.llm_cache = InMemoryCache()

with get_openai_callback() as cb:
    result = llm("How can we end world hunger?")
    print(result)
    print("--- Callback")
    print(cb)