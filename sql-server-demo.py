import _mssql
conn = _mssql.connect(server='localhost', user='SA', \
password='Password1', database='pubs')

conn.execute_query('SELECT title FROM titles')
for row in conn:
    print("TITLE=" + row['title'])

conn.close()
