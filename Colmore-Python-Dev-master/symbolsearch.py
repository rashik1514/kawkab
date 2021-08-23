import requests
import json

def symbol_search(company_name,api_key):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    
    list1 = []


    # Creating buttons
    for x in data['bestMatches']:
        print(x['1. symbol'])
        list1.append(x['1. symbol'])
    #print(list1)
    return list1

def ticker_search(ticker, api_key):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    
    return data
