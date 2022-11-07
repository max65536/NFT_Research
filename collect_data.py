import requests
from config import API_key_mnemonic, API_key_NFTscan, END_TIME
import pandas as pd
from IPython import embed

class Collection(object):
    def __init__(self, name, address, rank, details) -> None:
        self.name = name
        self.address = address
        self.rank = rank
        self.details = details
        

def collection_price(collection, endtime=END_TIME, API_key=API_key_mnemonic, duration="DURATION_365_DAYS"):
    '''
    DURATION_UNSPECIFIED: Unspecified value.
    DURATION_1_DAY: 1 day.
    DURATION_7_DAYS: 7 days.
    DURATION_30_DAYS: 30 days.
    DURATION_365_DAYS: 365 days.
    '''
    print(collection.name)
    url = "https://ethereum.rest.mnemonichq.com/pricing/v1beta1/prices/by_contract/" + collection.address

    query = {
    "duration": duration,
    "timestampLt": endtime,
    "groupByPeriod": "GROUP_BY_PERIOD_1_DAY"
    }

    headers = {"X-API-Key": API_key}

    response = requests.get(url, headers=headers, params=query)

    data = response.json()
    print(data['dataPoints'][0])
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

def get_all_collection_price(collection):
    all_data = []
    for i in range(2017, 2023):
        data = collection_price(collection=collection, endtime="%d-11-06T00:00:00Z"%i)
        all_data += data['dataPoints']
    return all_data

def collection_to_csv_alltime(collection):
    data = get_all_collection_price(collection)
    df = pd.DataFrame(data)
    df.to_csv("price_%s_alltime.csv"%collection.name)
    

'''
We also consider whether a transaction is a 
[x] primary sale (PrimarySale)    
and control for the changes in the number of unique wallets (ΔNumWallets), 
the number of buyers (ΔNumBuyers), the number of sellers (ΔNumSellers), 
the number of sales (ΔNumSales), the sales volume in USD (ΔSalesUSD), 
ETHUSD exchange rate (ΔETHUSD), the ETH trading volume (ΔETHVol)  
[ ] Google Index: worldwide attention to Ethereum (Adj. SVI)
'''

if __name__=="__main__":
    embed()