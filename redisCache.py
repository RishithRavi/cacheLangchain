# We can do the same thing with a Redis cache
# (make sure your local Redis instance is running first before running this example)
from redis import Redis
from langchain.cache import RedisCache
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv, find_dotenv
import langchain

_ = load_dotenv(find_dotenv())  # read local .env file
OpenAI.api_key = os.environ["OPENAI_API_KEY"]

llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

langchain.llm_cache = RedisCache(redis_=Redis())

print(llm("Tell me a joke"))
print(llm("Tell me a joke"))
