import asyncio
import aiohttp
"""
TODO: 
- implement error handling, logging, and retries for robustness
- need to update to implement streaming of the data so that batching can be properly handled
- implement batching logic to handle large datasets efficiently

"""

async def fetch_gbfs_data(url: str='https://gbfs.lyft.com/gbfs/2.3/bkn/gbfs.json', batch_size: int=100):
    print(url)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                    return await response.json() #have to check this over to make sure the event loop is getting back the control
        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
            return None

if __name__ == "__main__":
    asyncio.run(fetch_gbfs_data)