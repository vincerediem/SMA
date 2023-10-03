import requests
import pandas as pd

import sys
sys.path.append(r"C:\Users\kopen\OneDrive\Desktop\Code\Algo Trading\Base Functions")

import BaseFunctionv1 as bf

ALPHA_VANTAGE_KEY = 'Y84MMO9G796B0PNO'

stock_list = bf.stock_list()

def sma(stock_list):
    url = 'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo'
    r = requests.get(url)
    data = r.json()
    return data
    
print(sma(stock_list))