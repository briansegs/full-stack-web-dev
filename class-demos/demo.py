import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=admin')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

# No Formating
cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, True);')

# Format with %s 1
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, False))

# Format with %s 2
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    'id': 3,
    'completed': False
}
cursor.execute(SQL, data)

# Format with f-string
id = 4
completed = True
SQL2 = f'INSERT INTO table2 (id, completed) VALUES ({id}, {completed});'
cursor.execute(SQL2)

cursor.execute('SELECT * FROM table2;')

result1 = cursor.fetchone()
print('fetchone()', result1)

result2 = cursor.fetchmany(2)
print('fetchmany(2)', result2)

result3 = cursor.fetchall()
print('fetchall()', result3)

result4 = cursor.fetchall()
print('fetchall()', result4)

cursor.execute('SELECT * FROM table2;')

result5 = cursor.fetchall()
print('fetchall()', result5)

connection.commit()

connection.close()
cursor.close()
