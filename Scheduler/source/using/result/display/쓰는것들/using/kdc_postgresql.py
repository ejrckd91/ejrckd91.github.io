##각각의 요소를 따로 입력 받아서 sql문으로 입력하는데 성공
## 테이블의 첫번째 두번째 세번째 요소를 입력 받아서 테이블을 생성하는데 성공
## 데이터를 입력 받았는데 테이블에 존재하거나 체크하는건 구현안해봄

import psycopg2 as pg2

class Data_Scheduler():
	def Insert_data(date,rank,subject,schedule):

		conn_string = ("dbname='kdc' user='kdc' password='1234'")

		conn = pg2.connect(conn_string)

		cur = conn.cursor()
		name = date
		print(name)
		no = rank
		no_n2 = subject
		ss = schedule
		head_sql = ('insert into testsch values')

		kdc_sql=("{0}('{1}',{2},'{3}','{4}');".format(head_sql,name,no,no_n2,ss))
		cur.execute(kdc_sql)

		sql_string = ("select * from testsch ;")
		cur.execute(sql_string)
		result = cur.fetchall()
		print(result)
		conn.commit()
