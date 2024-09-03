import asyncio
import aiohttp
import time
import random

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            time.sleep(random.randint(1,3))
            return await response.text()

async def fetch_all(urls):
    for url in urls:
        data = await fetch(url)
        print(url)
        yield data

async def process_data(data_generator):
    async for data in data_generator:
        print(f"Längd på data: {len(data)}")

urls = [
    "https://www.lroc.asu.edu/images/gigapan",
    "https://www.example.com",
    "https://www.python.org",
    "https://www.openai.com"
]

async def main():
    data_generator = fetch_all(urls)
    await process_data(data_generator)

# Kör den asynkrona huvudfunktionen
asyncio.run(main())
