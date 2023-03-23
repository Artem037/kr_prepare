import json

date_inp = '2023/04/02'.split('/')
type_inp = 'bar'
with open('server.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
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