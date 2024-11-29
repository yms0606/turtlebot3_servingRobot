import sqlite3
import glob
from datetime import datetime,timedelta

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

메뉴 추가완료 ============= 11.27 


cursor.execute("INSERT INTO menu VALUES('오뎅탕','메인메뉴',12000,5000)")
cursor.execute("INSERT INTO menu VALUES('매운오뎅탕','메인메뉴',13000,5000)")
cursor.execute("INSERT INTO menu VALUES('된장술밥','메인메뉴',8000,2000)")
cursor.execute("INSERT INTO menu VALUES('나가사키짬뽕','메인메뉴',11000,4000)")
cursor.execute("INSERT INTO menu VALUES('차돌짬뽕','메인메뉴',13000,3000)")
cursor.execute("INSERT INTO menu VALUES('부대찌개','메인메뉴',12000,3000)")
cursor.execute("INSERT INTO menu VALUES('국물떡볶이','메인메뉴',15000,4000)")
cursor.execute("INSERT INTO menu VALUES('먹태','메인메뉴',11000,5000)")
cursor.execute("INSERT INTO menu VALUES('치킨','메인메뉴',13000,7000)")
cursor.execute("INSERT INTO menu VALUES('닭발','메인메뉴',15000,7000)")

cursor.execute("INSERT INTO menu VALUES('어묵3종세트','사이드메뉴',8000,2000)")
cursor.execute("INSERT INTO menu VALUES('쥐포땅콩','사이드메뉴',7000,2000)")
cursor.execute("INSERT INTO menu VALUES('감자튀김','사이드메뉴',7000,1500)")
cursor.execute("INSERT INTO menu VALUES('과일화채','사이드메뉴',15000,3000)")
cursor.execute("INSERT INTO menu VALUES('황도','사이드메뉴',7000,2000)")
cursor.execute("INSERT INTO menu VALUES('파인샤베트','사이드메뉴',6000,1500)")
cursor.execute("INSERT INTO menu VALUES('계란말이','사이드메뉴',9000,3000)")
cursor.execute("INSERT INTO menu VALUES('라면','사이드메뉴',3000,1000)")

cursor.execute("INSERT INTO menu VALUES('참이슬','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('처음처럼','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('진로','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('새로','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('참이슬오리지널','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('카스','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('테라','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('켈리','주류',4500,500)")
cursor.execute("INSERT INTO menu VALUES('크러시','주류',4500,500)")

cursor.execute("INSERT INTO menu VALUES('콜라','음료',2000,300)")
cursor.execute("INSERT INTO menu VALUES('제로콜라','음료',2000,300)")
cursor.execute("INSERT INTO menu VALUES('사이다','음료',2000,300)")
cursor.execute("INSERT INTO menu VALUES('제로사이다','음료',2000,300)")
cursor.execute("INSERT INTO menu VALUES('환타포도','음료',2000,300)")
cursor.execute("INSERT INTO menu VALUES('환타파인애플','음료',2000,300)")

메뉴 추가 완료 =========== 11.28


img_list = glob.glob("./src/serving_node/serving_node/order_jjh/images/*")

for img in img_list:
    with open(img, 'rb') as file:

        blobimg = file.read()
        
        name = img.split("/")[-1].split(".")[0]
        query = ""INSERT INTO image_file (name,img) VALUES (?, ?)""
        data_tuple = (name,blobimg)

        cursor.execute(query,data_tuple)
        print(name,"insert")

이미지 추가 완료 ============= 11.28


cursor.execute("SELECT * FROM menu")
datas = cursor.fetchall()

for data in datas:
    print(data)

('쥐포땅콩', '사이드메뉴', 7000, 2000)

"""

"""
cursor.execute("INSERT INTO menu VALUES('무구리','메인메뉴',35000,10000)")
img = "/home/yms/rokey_week4_ws/turtlebot3_servingRobot/src/serving_node/serving_node/order_jjh/images/무구리.png"
query = "INSERT INTO image_file (name,img) VALUES (?, ?)"

with open(img, 'rb') as file:
    blobimg = file.read()
    data_tuple = ('무구리',blobimg)
    cursor.execute(query, data_tuple)
    print('insert 무구리')

    
무구리 추가 =============== 11.28
"""

# 일 매출, 월 매출, 메뉴별 판매량, 영업 이익

total_prices = []

for i in range(5):
    today = (datetime.now() + timedelta(day=-i)).strftime("%y%m%d")
    qeury = f"SELECT * FROM menu_order WHERE order_number LIKE '{today}%'"
    cursor.execute(qeury)
    orders = cursor.fetchall()
    if len(orders) == 0 :
        total_prices.append(0)
    else:
        sum = 0
        for order in orders:
            menu_list = order[2]


connection.commit()

connection.close()
