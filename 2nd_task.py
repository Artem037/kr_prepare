import argparse
import csv
import json

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, required=True)
parser.add_argument("--type", type=str, default='elliptical')

args = parser.parse_args()

data = []
res = {}

with open(args.file, encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=':', quotechar='"')
    for index, row in enumerate(reader):
        if index > 0:
            data.append(row)

for id, galaxy, type, mass, dark, distance in data:
    if type == args.type:
        res[galaxy] = round(int(dark) / int(mass), 1)

with open('relations.json', 'w', encoding='utf-8') as f:
    json.dump(res, f)
