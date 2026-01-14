#this is the runner file which will start the entire ETL process!
from config import db_credentials, gbfs_feed
import asyncio

from src.main import run_etl

async def main():
    await run_etl(gbfs_feed, db_credentials=db_credentials)

asyncio.run(main())
