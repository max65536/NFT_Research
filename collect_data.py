import requests
from config import API_key_mnemonic, API_key_NFTscan, END_TIME
from IPython import embed

class Collection(object):
    def __init__(self, name, address, rank, details) -> None:
        self.name = name
        self.address = address
        self.rank = rank
        self.details = details
        

def collection_price(contract_address, endtime=END_TIME, API_key=API_key_mnemonic):
    url = "https://ethereum.rest.mnemonichq.com/pricing/v1beta1/prices/by_contract/" + contract_address

    query = {
    "duration": "DURATION_365_DAYS",
    "timestampLt": endtime,
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