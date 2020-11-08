import psycopg2


def add_user1(name, username, admin=False):
  db = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="admin",
        )
  c = db.cursor()
  if name == 'Kat' or name == 'Brian':
    admin = True
  c.execute('''INSERT INTO users ("Name", "Username", "Admin")
              VALUES ('{}', '{}', {})'''.format(name, username, admin))
  db.commit()
  db.close()


def add_user2(name, username, admin=False):
  db = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="admin",
        )
  c = db.cursor()
  if name == 'Kat' or name == 'Brian':
    admin = True

  c.execute('''INSERT INTO users ("Name", "Username", "Admin")
              VALUES (%s, %s, %s);''', (name, username, admin))
  db.commit()
  db.close()





db = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="admin",
        )
c = db.cursor()

c.execute('DROP TABLE IF EXISTS users;')
c.execute('CREATE TABLE users( "Id" serial primary key, "Name" varchar(20), "Username" varchar(20), "Admin" boolean);')
db.commit()
db.close()

add_user2('Cookie', 'Monster')
add_user2('Kat', 'Kitty')
add_user2('Brian', 'Pookie')
add_user2('Sammy', 'Kool kid')



db = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="admin",
        )
c = db.cursor()
c.execute('SELECT * FROM users;')
result = c.fetchall()
for row in result:
  print(row)
db.close()
