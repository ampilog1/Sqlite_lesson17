import sqlite3

# подключаемся к базе данных
conn = sqlite3.connect('TestDB.db')

cursor = conn.cursor()

# извлекаем данные из БД
cursor.execute('select * from vacancy')

result = cursor.fetchall()
print(result)

# извлекаем данные с фильтром
cursor.execute('select * from vacancy where name=?', ('Python',))
print(cursor.fetchall())

# добавляем данные в таблицу
cursor.execute('insert into full_offer (number_offer, vacancy, region, skill) values (?, ?, ?, ?)', (1, 8, 1, 1))
cursor.execute('select * from full_offer')
print(cursor.fetchall())

query = 'select n.number, v.name, r.name, ' \
        's.name from Number_offer n, vacancy v, Skills s, Region r, ' \
        'full_offer f where f.number_offer = n.id and f.vacancy = v.id and f.region = r.id ' \
        'and f.skill = s.id'

# Выводим номер обьявления, название вакансии, название региона, название навыков
cursor.execute(query)

print(cursor.fetchall())
