import psycopg2

from psycopg2 import sql

connection = psycopg2.connect(
    host="localhost",
    database="psycopgtest",
    user="postgres",
    password="admin",
)
connection.set_session(autocommit=True)

with connection.cursor() as cursor:
    cursor.execute('SELECT COUNT(*) FROM users')
    result = cursor.fetchone()
print(result)

with connection.cursor() as cursor:
    cursor.execute('SELECT * FROM users;')
    result = cursor.fetchall()
print(result)


def is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = %(username)s
        """, {
            'username': username
        })
        result = cursor.fetchone()

    if result is None:
        # User does not exist
        return False

    admin, = result
    return admin

print(is_admin('haki'))

print(is_admin('ran'))

print(is_admin('foo'))

print(is_admin("'; select true; --"))


def count_rows(table_name: str, limit: int) -> int:
    with connection.cursor() as cursor:
        stmt = sql.SQL("""
            SELECT
                COUNT(*)
            FROM (
                SELECT
                    1
                FROM
                    {table_name}
                LIMIT
                    {limit}
            ) AS limit_query
        """).format(
            table_name = sql.Identifier(table_name),
            limit = sql.Literal(limit),
        )
        cursor.execute(stmt)
        result = cursor.fetchone()

    rowcount, = result
    return rowcount

print(count_rows('users', 1))

print(count_rows('users', 10))