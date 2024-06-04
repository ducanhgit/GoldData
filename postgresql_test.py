import psycopg2
#cn to db
conn = psycopg2.connect(
    host = "10.254.59.61", 
    port ="8018",
    database ="goldprice",
    user = "postgres",
    password = "Datateam#123"
)
# con tro de thuc hien truy van

cur = conn.cursor()
# truy van sql
cur.execute("SELECT * FROM gold_data.thegioi")

#in 
result = cur.fetchall()

for x in result:
    print(x)

conn.close()