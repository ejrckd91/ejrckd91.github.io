##각각의 요소를 따로 입력 받아서 sql문으로 입력하는데 성공
## 테이블의 첫번째 두번째 세번째 요소를 입력 받아서 테이블을 생성하는데 성공
## 데이터를 입력 받았는데 테이블에 존재하거나 체크하는건 구현안해봄

import psycopg2 as pg2

class Data_Scheduler():
	def Insert_data(date,sub,rank,etc,schedule):

		conn_string = ("dbname='kdc' user='kdc' password='1234'")

		conn = pg2.connect(conn_string)

		cur = conn.cursor()
		day = date
		no = sub
		no_n2 = rank
		et = etc
		ss = schedule
		#now = now_date
		head_sql = ('insert into sch values')

		kdc_sql=("{0}('{1}',{2},'{3}','{4}','{5}');".format(head_sql,day,no,no_n2,et,ss))
		cur.execute(kdc_sql)

		sql_string = ("select * from sch ;")
		cur.execute(sql_string)
		result = cur.fetchall()
		print(result)
		conn.commit()

	def Read_data(date):

		conn_string = ("dbname='kdc' user='kdc' password='1234'")

		conn = pg2.connect(conn_string)

		cur = conn.cursor()

		search=date
		search_sql = ('select * from sch where date=')
		kdc_search_sql = (("{0}{1}").format(search_sql,search))
		cur.execute(kdc_search_sql)
		result = cur.fetchall()
		print(result)
		conn.commit()
		return result
