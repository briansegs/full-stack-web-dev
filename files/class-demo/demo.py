import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="example",
    user="postgres",
    password="admin",
)

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute(
    '''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
    '''
)

cursor.execute('INSERT INTO table2 (id, completed) VALUES ({}, {});'.format(1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES ({id}, {completed});'.format(id=2, completed=False)

cursor.execute(SQL)

cursor.execute('SELECT * FROM table2;')

result = cursor.fetchall()
print(result)


connection.commit()

connection.close()
cursor.close()