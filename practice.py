import pandas as pd
import numpy as np
from pycoingecko import CoinGeckoAPI
import requests


X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)
print(Z)

a=np.array([0,1])
b=np.array([1,0])
c = np.dot(a,b)
print(c)

y = '1:2,3:4'.split(':')
print(y)

# help(requests)
# import requests
r = requests.get('https://www.unn.edu.ng')
print(r)

print(dir(r))
# print(help(r))
print('---------')
print('---------')
print('---------')
print('---------')
print('---------')
print(r.history)
print('---------')
print('---------')
print('---------')
print('---------')
print('---------')
req = r.request.headers

req_df = pd.DataFrame(req)
print(req_df)

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', 
                                            vs_currency='usd', days=30)
# print(bitcoin_data)

df =pd.DataFrame(bitcoin_data)
print(df)

# Opening and reading avocado.csv file using with statement
# Using with statement automatically closes the file object

avocado_df = pd.read_csv('avocado.csv')
print(avocado_df)
avocado_df.head()

with open('avocado.csv', 'r') as file:
    file1 = file.readline() # Reading the first line of the avocado file
    print(file1)
    file1 = file.readlines(7)
    print('-------------')
    print(file1)
    print('-------------')
    file1 = file.readline() # Reading the talk 
    print(file1)
    file1 = file.readline()
    print(file1)

print('')
print(file.name)
print(file.mode)

file = open('avocado.csv', 'r')
print('---------------')
print(file.name)
print(file.mode)
file.close()