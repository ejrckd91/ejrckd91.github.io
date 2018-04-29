##각각의 요소를 따로 입력 받아서 sql문으로 입력하는데 성공
import psycopg2 as pg2

conn_string = ("dbname='kdc' user='kdc' password='1234'")

conn = pg2.connect(conn_string)

cur = conn.cursor()
name = ('kkk')
print(name)
no = ('19910731')
no_n2 = ('120')
head_sql = ('insert into testkdc values')

kdc_sql=("{0}('{1}',{2},{3});".format(head_sql,name,no,no_n2))
cur.execute(kdc_sql)

sql_string = ("select * from testkdc ;")
cur.execute(sql_string)
result = cur.fetchall()
print(result)
conn.commit()
