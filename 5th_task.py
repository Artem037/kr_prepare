from flask import Flask
import sqlite3

with open('carbon.txt', 'r', encoding='utf-8') as f:
    db_name, max_temp = f.readlines()
    db_name = db_name.strip('\n')

sqlite_connection = sqlite3.connect(db_name)
cursor = sqlite_connection.cursor()

sqlite_select_query = f"""SELECT star, stage, temperature, mass, size from stars"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()

lists = []

for star, stage, temperature, mass, size in records:
    if stage == 'C' and temperature <= int(max_temp):
        lists.append([star, temperature, mass, size])

lists.sort(key=lambda x: (x[1], -x[2]))
cursor.close()

res_list = []

for i in lists:
    res_list.append({"star": i[0], "temperature": i[1], "mass": i[2], "size": i[3]})

app = Flask(__name__)
print(res_list)


@app.route('/darkness')
def index():
    global res_list
    return res_list


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
