import json
import requests

type_inp = input()
date_inp = input().split('/')

with open('light.json', 'r', encoding='utf-8') as file:
    templates = json.load(file)

resp = requests.get(f'http://{templates["host"]}:{templates["port"]}')

data = json.load(resp.json())
good_dates = []
res = []
for date_get in data.keys():
    year, month, day = date_get.split('/')
    if int(date_inp[0]) >= int(year):
        if int(date_inp[1]) >= int(month):
            if int(date_inp[2]) > int(day):
                good_dates.append('/'.join([year, month, day]))
for good_date in good_dates:
    for galaxy in data[good_date]:
        if galaxy['type'] == type_inp:
            res.append(galaxy['galaxy'])

print(', '.join(sorted(list(set(res)))))
