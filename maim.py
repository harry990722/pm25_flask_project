import pymysql

conn=pymysql.connect(
host="127.0.0.1",
user="root",
password="",
port=3307,
database="demo"
)

print(conn)

conn.close()
print("資料庫關閉完成")