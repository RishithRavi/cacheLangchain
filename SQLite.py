import os
from langchain.llms import OpenAI
from dotenv import load_dotenv, find_dotenv
from langchain.cache import SQLiteCache
import langchain


_ = load_dotenv(find_dotenv())  # read local .env file
OpenAI.api_key = os.environ["OPENAI_API_KEY"]

# We can do the same thing with a SQLite cache

llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

langchain.llm_cache = SQLiteCache(database_path=".langchain.db")



# The first time, it is not yet in cache, so it should take longer
print(llm("Tell me a joke"))
print(llm("Tell me a joke"))
