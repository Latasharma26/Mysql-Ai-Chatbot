import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        # Add your password if any
    database="sampledb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees;")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
