from dotenv import load_dotenv
import os
from botocore.config import Config
#will be refrencing the GBFS from the city bike data source found here: https://github.com/MobilityData/gbfs/blob/master/gbfs.md
#can also check if there is a venv directory and create one if not found
try:
    with open('.env', 'r') as f:
        pass # we don't really care to do anything if the file exists and the file will close automatically due to the with statement
except OSError:
    with open('.env', 'w') as f:
        f.write("PSQL_USERNAME='postgres'\n")
        f.write("PSQL_PASSWORD='0000'\n")
        f.write("PSQL_HOST_ADDR='127.0.0.1'\n")
        f.write("PSQL_PORT='5430'\n")
        f.write("DB_NAME='cycleytics_warehouse'\n")
        f.write("CONNECTION_TIMEOUT=10\n")
        f.write("region=us-east-2\n")
        f.write("s3_bucket_name=cyclelytics-parquet-lake\n")
finally:
    print('.env file checked for existence!')

load_dotenv()

db_credentials = {
    "user": os.getenv(key="PSQL_USERNAME", default="No Key Found"),
    "password": os.getenv(key="PSQL_PASSWORD", default="No Key Found"),
    "host": os.getenv(key="PSQL_HOST_ADDR", default="No Key Found"),
    "port": os.getenv(key="PSQL_PORT", default="No Key Found"),
    "database": os.getenv(key="DB_NAME", default="No Key Found"),
    "timeout": os.getenv(key="CONNECTION_TIMEOUT", default="No Key Found"),
}
s3_config = {
    'bucket_name': os.getenv(key="s3_bucket_name", default="No Key Found"),
    'botocore_config': Config(
        region_name=os.getenv(key="region", default="us-east-2"),
        retries = {
            'max_attempts': 10,
            'mode': 'standard'
        },
    )
}

gbfs_feed = {
    "base_url": "https://gbfs.lyft.com/gbfs/2.3/bkn/gbfs.json",
    "feeds": {
        "en": {
            "station_information": "https://gbfs.lyft.com/gbfs/2.3/bkn/en/station_information.json",
            "station_status": "https://gbfs.citibikenyc.com/gbfs/en/station_status.json",
            "free_bike_status": "https://gbfs.lyft.com/gbfs/2.3/bkn/en/free_bike_status.json",
            "vehicle_types": "https://gbfs.lyft.com/gbfs/2.3/bkn/en/vehicle_types.json",
            "system_alerts": "https://gbfs.lyft.com/gbfs/2.3/bkn/en/system_alerts.json",
        },
        "fr":{
            "station_information": "https://gbfs.lyft.com/gbfs/2.3/bkn/fr/station_information.json",
            "station_status": "https://gbfs.citibikenyc.com/gbfs/fr/station_status.json",
            "free_bike_status": "https://gbfs.lyft.com/gbfs/2.3/bkn/fr/free_bike_status.json",
            "vehicle_types": "https://gbfs.lyft.com/gbfs/2.3/bkn/fr/vehicle_types.json",
            "system_alerts": "https://gbfs.lyft.com/gbfs/2.3/bkn/fr/system_alerts.json",
        },
        "es":{
            "station_information": "https://gbfs.lyft.com/gbfs/2.3/bkn/es/station_information.json",
            "station_status": "https://gbfs.citibikenyc.com/gbfs/es/station_status.json",
            "free_bike_status": "https://gbfs.lyft.com/gbfs/2.3/bkn/es/free_bike_status.json",
            "vehicle_types": "https://gbfs.lyft.com/gbfs/2.3/bkn/es/vehicle_types.json",
            "system_alerts": "https://gbfs.lyft.com/gbfs/2.3/bkn/es/system_alerts.json",
        }
    }
}