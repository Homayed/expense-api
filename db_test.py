import psycopg2

connection = psycopg2.connect(
    dbname="expense_db",
    user="mhnkarim",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM expenses;")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()