#this is the runner file which will start the entire ETL process!
from config import db_credentials, gbfs_feed, s3_config
import asyncio
import time

from src.main import run_etl

#the TTL on the data is 60s

async def main():
    timestart = time.time()
    await run_etl(gbfs_feed, db_credentials=db_credentials, s3_config_obj=s3_config)
    timeend = time.time()   
    print(f"ETL process took {timeend - timestart} seconds")

asyncio.run(main())
