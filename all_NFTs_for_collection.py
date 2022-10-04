import requests
from config import API_key_mnemonic
from IPython import embed



API_key = "ZoLtFq-dPENmfvr27FUDvE61FALoLBML"

url = "https://eth-mainnet.g.alchemy.com/nft/v2/%s/getNFTsForCollection?contractAddress=0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d&withMetadata=false"%API_key

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

#print(response.text)

BYAC_contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"

def compute_rarity(contractAddress, tokenID):
    url = "https://eth-mainnet.g.alchemy.com/nft/v2/%s/computeRarity"%API_key
    headers = {"accept": "application/json"}
    params = {"contractAddress": contractAddress, "tokenId":tokenID}
    response = requests.get(url, headers=headers, params=params)
    return response.text

def test():    
    result = requests.get(
        'https://ethereum.rest.mnemonichq.com/tokens/v1beta1/by_owner/0xBA19BA5233b49794c33f01654e99A60E579E6f29?limit=5',
        headers={'x-api-key': API_key_mnemonic}
    ).json()
    return result

def collection_price(contract_address, API_key=API_key_mnemonic):
    url = "https://ethereum.rest.mnemonichq.com/pricing/v1beta1/prices/by_contract/" + contract_address

    query = {
    "duration": "DURATION_1_DAY",
    "timestampLt": "2022-08-24T14:15:22Z",
    "groupByPeriod": "GROUP_BY_PERIOD_1_DAY"
    }

    headers = {"X-API-Key": API_key}

    response = requests.get(url, headers=headers, params=query)

    data = response.json()
    return data

def collection_price_opensea(contract_name):
    url = "https://api.opensea.io/api/v1/collection/%s/stats"%contract_name

    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    return response.json()

rarity = compute_rarity(BYAC_contract_address, tokenID=8345)
data1 = collection_price(contract_address=BYAC_contract_address, API_key=API_key_mnemonic)
data2 = collection_price_opensea(contract_name="boredapeyachtclub")
embed()
