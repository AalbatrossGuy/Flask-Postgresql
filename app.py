import os
import psycopg2
from flask import Flask, render_template

# app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="test_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)

cur = conn.cursor()
# cur.execute(
#     'CREATE TABLE test_table(equip_id smallint PRIMARY KEY, color varchar(50) NOT NULL);')
cur.execute(
    """
    INSERT INTO test_table(equip_id, color) VALUES(%s, %s);
    """, (1, 'violet',)
)

conn.commit()
print('done')
conn.close()


# @app.route('/')
# def home():
#     return render_template('home.html')
