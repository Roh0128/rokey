import pymysql
# 서버연결
conn=pymysql.connect(
    host="localhost",     
    user="root",           
    password="1234",  # MySQL 비밀번호 
    database="exampledb", # 사용할 데이터베이스 명 
    charset='utf8mb4', # UTF-8의 확장 버전 
    cursorclass=pymysql.cursors.DictCursor
) 
# 커서 생성= 명령어 작성
cursor=conn.cursor()
# 명령어 실행
cursor.execute("SELECT DATABASE()")
print("현재 데이터베이스:", cursor.fetchone())
# print("현재 데이터베이스:", cursor.fetchall())
# print("현재 데이터베이스:", cursor.fetchmany(2))
# 연결 해제
conn.close()