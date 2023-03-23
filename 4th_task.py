import sqlite3
import csv

db_name = input()
table, cell = input().split('.')

sqlite_connection = sqlite3.connect(db_name)
cursor = sqlite_connection.cursor()

sqlite_select_query = f"""SELECT id, type_id, luminosity_id, {cell} from {table}"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()

good_ids = []

min_val = min([i[3] for i in records])

for row in records:
    if row[3] == min_val:
        good_ids.append([row[0], row[1], row[2]])
cursor.close()

res = {}

for id, type_id, luminosity_id in good_ids:
    cursor = sqlite_connection.cursor()
    sqlite_select_query = f"""SELECT id, sign, size, stars from {table}"""
    cursor.execute(sqlite_select_query)
    records_curr = cursor.fetchall()

    for id_curr, sign, size, stars in records_curr:
        if id_curr == id:
            res[id] = [str(sign), str(size), str(stars)]

    cursor = sqlite_connection.cursor()
    sqlite_select_query = f"""SELECT id, type from types"""
    cursor.execute(sqlite_select_query)
    records_curr = cursor.fetchall()

    for type_id_curr, type in records_curr:
        if type_id_curr == type_id:
            res[id].append(type)

    cursor = sqlite_connection.cursor()
    sqlite_select_query = f"""SELECT id, range from luminosities"""
    cursor.execute(sqlite_select_query)
    records_curr = cursor.fetchall()

    for luminosity_id_curr, range_ in records_curr:
        if luminosity_id_curr == luminosity_id:
            res[id].append(range_)

with open('collisions.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='#', quotechar='"')
    writer.writerow(['no', 'galaxy', 'type', 'luminosity', 'size', 'stars'])

    count = 1
    res_list = []
    for name, size, stars, type, range_list in res.values():
        res_list.append([count, name, type, range_list, size, stars])

    res_list = sorted(res_list, key=lambda x: (x[4], x[1]), reverse=True)

    for i in res_list:
        writer.writerow(i)
