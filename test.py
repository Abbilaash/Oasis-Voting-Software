import mysql.connector
conn = mysql.connector.connect(user='root', password='', host='localhost', database='voting_result')
cursor = conn.cursor()
sql_pallava=" SELECT * FROM pallava ;"
cursor.execute(sql_pallava)
result=cursor.fetchall()
for pallava in result:
    pallava_res1=list(pallava)
    print(pallava_res1)
    pallava_res1=pallava_res1[0],'=',pallava_res1[1]
    print(pallava_res1)
conn.close()