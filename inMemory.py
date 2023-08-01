import langchain
from langchain.llms import OpenAI
from langchain.cache import InMemoryCache

import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]
# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2, verbose=True)


langchain.llm_cache = InMemoryCache()

print(llm("Tell me a joke"))
print(llm("Tell me another joke"))
