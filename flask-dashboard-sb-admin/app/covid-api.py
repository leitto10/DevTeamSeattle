import requests
import pandas as pd
from pandas.io.json import json_normalize
import json

# url = 'https://adventofcode.com/2020/leaderboard/private/view/974926.json'
url = 'https://api.covidtracking.com/v1/states/wa/daily.json'
# url = 'https://api.covidtracking.com/v1/states/wa/current.json'
# url = 'http://dydja.com/participant-activity-logs/'
df = requests.get(url)
xtc = df.json()
dailyInfo = []
for i in xtc[0:1]:
    dailyInfo.append(i['date'])
    print(dailyInfo[0])
    dailyInfo.append(i['positive'])
    dailyInfo.append(i['positiveIncrease'])
    dailyInfo.append(i['death'])
    dailyInfo.append(i['deathIncrease'])
    dailyInfo.append(i['hospitalizedCurrently'])
    print('Date:', i['date'], '| Total Positive:',i['positive'], '| New Positive:', i["positiveIncrease"],
          '| Total Death:', i["death"], '| New Deaths:', i["deathIncrease"], '| Cur Hosp:', i['hospitalizedCurrently'])
print(dailyInfo)
# print(xtc[0])