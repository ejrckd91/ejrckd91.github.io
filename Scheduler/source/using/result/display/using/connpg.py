##각각의 요소를 따로 입력 받아서 sql문으로 입력하는데 성공
## 테이블의 첫번째 두번째 세번째 요소를 입력 받아서 테이블을 생성하는데 성공
## 데이터를 입력 받았는데 테이블에 존재하거나 체크하는건 구현안해봄

import psycopg2 as pg2
##사용하는거아님
class Data_Scheduler():
	def Insert_data():

		conn_string = ("dbname='kdc' user='kdc' password='1234'")

		conn = pg2.connect(conn_string)

		cur = conn.cursor()
		name = input("input key_name\n")
		print(name)
		no = input("input yur birth ex)19910731\n")
		no_n2 = input("Priority Value ex)1\n")
		head_sql = ('insert into testkdc values')

		kdc_sql=("{0}('{1}',{2},{3});".format(head_sql,name,no,no_n2))
		cur.execute(kdc_sql)

		sql_string = ("select * from testkdc ;")
		cur.execute(sql_string)
		result = cur.fetchall()
		print(result)
		conn.commit()

	def Create_table():##미완임 수정이 좀 필요 대충 윤곽만 잡아둔것

		conn_string = ("dbname='kdc' user='kdc' password='1234'")

		conn = pg2.connect(conn_string)

		cur = conn.cursor()
		## ex) create table __name__ (val type primary key, val type, val type, val type, date date NOT NULL)
		tablename = input("type your creating table name\n")
		val_num = input("input your table col num\n")
		arr1 = []
		last = 0
		input_val_num = '{0}'
		for int i = 0 in range(0,(val_num-1)):
			arr1[i] = input("input yout {0} value name\n".format(i)) ##테이블 멤버 이름 입력 받기
			last = i
		for int i = 1 in range(1,(val_num-1)):
			input_val_num = input_val_num+',{i}'
		kdc_sql=("create table ({0})".format(input_val_num))
		cur.execute(kdc_sql)
		table_sql = ("\du")
		cur.execute(table_sql)
		result = cur.fetchall()
		print(kdc_sql)
		print(table_sql)
		conn.commit()

	def Insert_Schedule():

		conn_string = ("dbname='kdc' user='kdc' password='1234'")

		conn = pg2.connect(conn_string)

		cur = conn.cursor()
		name = input("input key_name\n")
		print(name)
		no = input("input yur birth ex)19910731\n")
		no_n2 = input("Priority Value ex)1\n")
		head_sql = ('insert into testkdc values')

		kdc_sql=("{0}('{1}',{2},{3});".format(head_sql,name,no,no_n2))
		cur.execute(kdc_sql)

		sql_string = ("select * from testkdc ;")
		cur.execute(sql_string)
		result = cur.fetchall()
		print(result)
		conn.commit()
