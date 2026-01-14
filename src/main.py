"""
in this file we will control the ETL
this way the asyncio happens from here and not in any of the other modules 
and this way tasks can efficiently and properly be fetched, awaited, and gathered!
this is where the event loop will be run from!
this is very important for understanding the event loop and properly managing it! 66dbe4db-0aca-11e7-82f6-3863bb44ef7c

*** Extremely important note: 
Unlike tasks, awaiting a coroutine does not hand control back to the event loop! Wrapping a coroutine in a task 
first, then awaiting that would cede control. The behavior of await coroutine 
is effectively the same as invoking a regular, synchronous Python function. Consider this program:

***

TODO:
- implement transform and load phases of the ETL process
- in the transform phase we will be using the geopandas toi make the borough paritions


"""
import asyncio
import pandas as pd
import numpy as np
from src.extract.fetch_gbfs_data import fetch_gbfs_data

async def run_etl(feed, batch_size: int =100, db_credentials: dict[dict[str]]=None) -> None:
    feed_tasks = [{}] #list of dicts to hold tasks for each task feed to simplify management
    async with asyncio.TaskGroup() as tg:
        for en_feed_key, en_feed_url in feed['feeds']['en'].items():
            feed_tasks[0][en_feed_key] = tg.create_task(fetch_gbfs_data(en_feed_url, batch_size=batch_size))
    for task_name, task in feed_tasks[0].items():
        feed_tasks[0][task_name] = task.result()

    
    
    #further ETL steps would go here: transform and load phases
    #this is just a skeleton to show where the ETL process would be managed
