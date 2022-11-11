import sqlite3

# подключаемся к базе данных
conn = sqlite3.connect('TestDB.db')


cursor = conn.cursor()