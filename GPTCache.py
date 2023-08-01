from gptcache import Cache
from gptcache.manager.factory import manager_factory
from gptcache.processor.pre import get_prompt
from langchain.cache import GPTCache
from langchain.callbacks import get_openai_callback
import langchain
import hashlib
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv, find_dotenv
import time

_ = load_dotenv(find_dotenv())  # read local .env file
OpenAI.api_key = os.environ["OPENAI_API_KEY"]

def get_hashed_name(name):
    return hashlib.sha256(name.encode()).hexdigest()


def init_gptcache(cache_obj: Cache, llm: str):
    hashed_llm = get_hashed_name(llm)
    cache_obj.init(
        pre_embedding_func=get_prompt,
        data_manager=manager_factory(manager="map", data_dir=f"map_cache_{hashed_llm}"),
    )

llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

langchain.llm_cache = GPTCache(init_gptcache)

# The first time, it is not yet in cache, so it should take longer
with get_openai_callback() as cb:
    tic = time.process_time()
    result = llm("Tell me a joke")
    toc = time.process_time()
    print(cb)
    print(result)
    print(toc-tic)
with get_openai_callback() as cb:
    tic = time.process_time()
    result = llm("Tell me another joke")
    toc = time.process_time()
    print(cb)
    print(result)
    print(toc-tic)

# print(llm("Tell me a joke"))
# The first time, it is not yet in cache, so it should take longer
# print(llm("Tell me a joke"))