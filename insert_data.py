import sqlite3

connection = sqlite3.connect("ServingRobotDB.db")
cursor = connection.cursor()

"""
cursor.execute("INSERT INTO menu VALUES('얼큰수제비','메인메뉴',15000,4000)")
cursor.execute("INSERT INTO menu VALUES('쫄지마라탕','메인메뉴',21000,7000)")
cursor.execute("INSERT INTO menu VALUES('치즈라볶이','메인메뉴',14000,5000)")
cursor.execute("INSERT INTO menu VALUES('짜빠구리범벅세트','메인메뉴',13000,3000)")
cursor.execute("INSERT INTO menu VALUES('치즈라볶이범벅세트','메인메뉴',13000,3000)")
cursor.execute("INSERT INTO menu VALUES('짜빠구리','메인메뉴',10000,3000)")
cursor.execute("INSERT INTO menu VALUES('불짬뽕탕','메인메뉴',17000,6000)")
cursor.execute("INSERT INTO menu VALUES('어묵탕','메인메뉴',13000,5000)")
cursor.execute("INSERT INTO menu VALUES('통돈가스김치우동','메인메뉴',19000,6000)")
cursor.execute("INSERT INTO menu VALUES('바질크림파스타','메인메뉴',15000,6000)")
cursor.execute("INSERT INTO menu VALUES('케이준셀러드','메인메뉴',13000,6000)")
cursor.execute("INSERT INTO menu VALUES('고르곤졸라피자','메인메뉴',17000,4000)")
cursor.execute("INSERT INTO menu VALUES('모듬소세지','메인메뉴',17000,3000)")
cursor.execute("INSERT INTO menu VALUES('순살치킨','메인메뉴',18000,7000)")

추가완료 

"""


connection.commit()

connection.close()
