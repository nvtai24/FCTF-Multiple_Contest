"""Check actual schema of contests_challenges table on cloud DB"""
import pymysql

conn = pymysql.connect(
    host='34.126.80.121',
    port=30306,
    user='root',
    password='QXVwILHTeNpRHpy2ds1xr3BZlPqjjWx2AJBT7w4cXrDYsav904',
    database='ctfd'
)

cursor = conn.cursor()
cursor.execute("DESCRIBE contests_challenges")
columns = cursor.fetchall()
print("=== contests_challenges columns ===")
for col in columns:
    print(f"  {col[0]:30} {col[1]}")

cursor.close()
conn.close()
