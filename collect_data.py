from tkinter import W
import requests
from config import API_key_mnemonic, API_key_NFTscan, END_TIME
from IPython import embed

class Collection(object):
    def __init__(self, name, address, rank, details) -> None:
        self.name = name
        self.address = address
        self.rank = rank
        self.details = details
        

def collection_price(contract_address, API_key=API_key_mnemonic):
    url = "https://ethereum.rest.mnemonichq.com/pricing/v1beta1/prices/by_contract/" + contract_address

    query = {
    "duration": "DURATION_365_DAYS",
    "timestampLt": END_TIME,
    "groupByPeriod": "GROUP_BY_PERIOD_1_DAY"
    }

    headers = {"X-API-Key": API_key}

    response = requests.get(url, headers=headers, params=query)

    data = response.json()
    return data

def top100_value():
    url = "https://restapi.nftscan.com/api/v2/statistics/ranking/marketcap"
    headers = {"X-API-Key": API_key_NFTscan}
    response = requests.get(url, headers=headers)
    data = response.json()
    collections = []
    for k, item in enumerate(data["data"][:100]):
        collections.append(Collection(  name=item["contract_name"], 
                                        address=item["contract_address"],
                                        rank=k,
                                        details=item
                                        ))
    return collections


embed()