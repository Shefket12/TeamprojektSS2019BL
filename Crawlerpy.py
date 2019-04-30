import requests
import pandas as pd
import json
import time
from pandas.io.json import json_normalize

df = pd.read_csv('http://www.openligadb.de/api/getmatchdata/bl1/2018/33')   #read the Data from the website
#df = df[['MatchID','Team1','Team2']]
df.head()                                                                   #print the head of the CSV 



#df['API_response'] = df.apply(get_reverse_geocode_data,axis=1)
#df['API_response'].head()
        

##r = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/30')
##r.json()


r = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/30')
#r.json()
k = r.json()            #safe as JSON
df = pd.DataFrame(k)    #safe as DataFrame
df = df[['Team1']]      #keep only "Team1"

df.head()

k