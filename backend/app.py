from flask import Flask
from flask import request
from flask import send_file

import sqlite3
import tempfile
import csv
import os

PATH_TO_SQLITE = os.path.join(os.getcwd(), 'sql', 'db.sqlite')
temp_dir = tempfile.TemporaryDirectory()

app = Flask(__name__)

@app.route('/api')
def main():
    return 'API Works and Running'

def get_path_to_csv_file(table_name) -> str:
    return os.path.join(temp_dir.name, table_name + '.csv')

def is_temp_csv_file_exist(table_name) -> bool:
    return os.path.isfile(get_path_to_csv_file(table_name)) 

@app.route('/api/get_csv_table', methods= ['POST'])
def get_csv_table():
    data = request.form
    table_name = data.get('table_name')
    csv_file = get_path_to_csv_file(table_name)

    if (not is_temp_csv_file_exist(table_name)):
        con = sqlite3.connect(PATH_TO_SQLITE)
        cur = con.cursor()

        sql_data = cur.execute(f"SELECT * FROM `{table_name}`")
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            names = list(map(lambda x: x[0], cur.description))
            writer.writerow(names)
            writer.writerows(sql_data)

        con.close()
    return send_file(csv_file)

if __name__ == "__main__":
    app.run()
    temp_dir.cleanup()