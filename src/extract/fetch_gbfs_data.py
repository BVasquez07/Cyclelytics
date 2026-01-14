import asyncio
import aiohttp



"""
TODO: 
- implement error handling, logging, and retries for robustness
- need to update to implement streaming of the data so that batching can be properly handled
- implement batching logic to handle large datasets efficiently

"""



async def fetch_gbfs_data(url='https://gbfs.lyft.com/gbfs/2.3/bkn/gbfs.json', batch_size=100):
    print(url)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                    return await response.json()
        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
            return None

if __name__ == "__main__":
    print('hello world')
    asyncio.run(fetch_gbfs_data)