import sqlalchemy
import pandas as pd

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    #meta = sqlalchemy.MetaData(bind=con, reflect=True)
    
    return con


engine = connect('kdc', '1234', 'kdc')
print(pd.read_sql("select * from pg_user limit 1", engine))
tk = pd.read_sql("select * from pg_user;",engine)
print(tk)
