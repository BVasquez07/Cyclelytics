#this file will handle making the parquet files and pushing them to the s3 data lake as parquet files
import asyncio
import pandas as pd
import tempfile
import fastparquet
import boto3

"""
TODO:
- make more efficient by checking if a bucket exists instead of trying to create it each time!
- update the file_key by specific data partition to make use of parquet strengths in retrieving partitioned data!
- add error handling for the s3 upload process
- add logging instead of print statements
- add configuration options for parquet file creation (compression, partitioning, etc)
- revise and improve concurrency if needed!
"""

async def create_and_upload_parquet(df: pd.DataFrame, s3_config_obj: dict, file_key: str) -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = f"{temp_dir}/temp_parquet.parquet" #this file name has to be updated
        try:
            df.to_parquet(temp_file_path, index=False, engine='fastparquet')
        except Exception as e:
            return f"Error creating parquet file: {e}"
        finally:
            s3 = boto3.client('s3', config=s3_config_obj['botocore_config'])

            try:
                #establishing connection to bucket
                s3.create_bucket(Bucket=s3_config_obj['bucket_name'], 
                                 CreateBucketConfiguration={'LocationConstraint': s3_config_obj['botocore_config'].region_name})
            except Exception as e:
                print(f"Bucket creation may have failed or bucket already exists: {e}")
            try:
                #uploading file
                s3.upload_file(temp_file_path, f'{s3_config_obj["bucket_name"]}', file_key)

                print(f"Successfully uploaded parquet file to s3://{s3_config_obj['bucket_name']}/{file_key}")
            except Exception as e:
                return f"Error uploading parquet file to S3: {e}"
            

