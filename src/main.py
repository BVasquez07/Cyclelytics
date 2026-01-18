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
- in the transform phase we will be using the geopandas to make the borough paritions
- need to merge the data from the various portions of the GBFS feed into a cohesive dataset
- fix: the vehicle types data not coming in properly in the station status json
"""
import asyncio
import pandas as pd
from src.extract.fetch_gbfs_data import fetch_gbfs_data
from src.extract.lake_prqt_upload import create_and_upload_parquet
import fastparquet
import time

async def run_etl(feed, batch_size: int =100, db_credentials: dict[dict[str]]=None, s3_config_obj: object=None) -> None:
    #extract portion
    #there is an error with the vehicle types that doesn't come in!
    feed_tasks = [{}] #list of dicts to hold tasks for each task feed to simplify management
    async with asyncio.TaskGroup() as tg:
        for en_feed_key, en_feed_url in feed['feeds']['en'].items():
            feed_tasks[0][en_feed_key] = tg.create_task(fetch_gbfs_data(en_feed_url, batch_size=batch_size))
    for task_name, task in feed_tasks[0].items():
        feed_tasks[0][task_name] = task.result()

    station_info_df = pd.DataFrame(feed_tasks[0]['station_information']['data']['stations'])
    station_status_df = pd.DataFrame(feed_tasks[0]['station_status']['data']['stations'])
    # status_exploded = station_status_df.explode('vehicle_types_available')
    # print(status_exploded.head())
    # status_normalized = pd.json_normalize(status_exploded['vehicle_types_available'])
    # station_status_df = pd.concat([station_status_df.drop(columns=['vehicle_types_available']), status_normalized], axis=1)
    # print(station_status_df.head().T)

    vehicle_types_df = pd.DataFrame(feed_tasks[0]['vehicle_types']['data']['vehicle_types']) #can't merge this in until the vehicle types data is fixed!
    joined = station_info_df.merge(station_status_df, on='station_id', how='outer')

    print(joined.info())
    print(joined.describe())
    print(joined.shape)
    #creating the parquet files from the dataframe & storing into s3 parquet lake


    await asyncio.create_task(create_and_upload_parquet(df=joined, s3_config_obj=s3_config_obj, file_key=f'gbfs_station_data.parquet{time.strftime("%Y%m%d-%H%M%S")}'))

    """
    TODO:
    [x] join all of the data that is relevant into one cohesive dataframe
        - the three to be joined are station info, station status, and vehicle_types
        -still have to 
    [x] create the parquet file(s) from the dataframe
    [X] store the parquet file(s) into the s3 data lake
        - need to add redunancy for data integrity in the upload process so something standard is using the time 
        - an alternative is to using some of the file contents so that lookup and reads are efficient
    """

    


    #transform portion




    #load portion
    
    
    #further ETL steps would go here: transform and load phases
    #this is just a skeleton to show where the ETL process would be managed
