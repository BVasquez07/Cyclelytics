import pytest
from src.extract.fetch_gbfs_data import fetch_gbfs_data
import asyncio
import allure
from config import gbfs_feed

#To run the file:  pytest --alluredir allure-results
#To run the file and generate the allure report: pytest --alluredir allure-results && allure serve allure-results

URL: str = gbfs_feed['feeds']['en']['station_information']


@allure.title("Testing the data can be fetched")
#@pytest.mark.parametrize("url", url)
@pytest.mark.asyncio
async def test_fetch_gbfs_data():
    result = await fetch_gbfs_data(URL)
    assert isinstance(result, dict)

@allure.title("Testing the fetching of data and ensuring the data is coming back in the expected format")
#@pytest.mark.parametrize("url", url)
@pytest.mark.asyncio
async def test_fetch_gbfs_data_response_structure():
    result = await fetch_gbfs_data(URL)
    assert "data" in result 