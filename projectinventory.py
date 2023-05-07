import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='anish@123ANISH',database= 'INVENTORY_MANAGEMENT')
cur = mydb.cursor()

# CREATING MANUFACTURE TABLE

M_table = 'CREATE TABLE MANUFACTURE (PRODUCT_ID integer(4) not null, PRODUCT_NAME varchar(30) not null, MANUFACTURED_COMPANY varchar(30)not null, MANUFACTURED_DATE date not null, NEED_TO_BE_MANUFACTURED varchar(30) not null,NO_OF_ITEMS_MANUFACTURED integer(4) not null, NO_OF_DEFECTIVE_ITEMS integer(4) not null, MANUFACTURED_AMOUNT integer(4) not null);'
cur.execute(M_table)

# CREATING GOODS TABLE

G_table = 'CREATE TABLE GOODS (PRODUCT_ID integer(4) not null,PRODUCT_NAME varchar(30)not null,MANUFACTURED_COMPANY varchar(30)not null,MANUFACTURED_DATE date not null,AVAILABLE_QUANTITY integer(4) not null,COST_OF_EACH_ITEM integer(4) not null);'

# CREATING PURCHASE TABLE

P_table = 'CREATE TABLE PURCHASE (PRODUCT_ID integer(4) not null,PRODUCT_NAME varchar(30) not null,PURCHASE_ID integer(4) not null,PURCHASE_DATE date NOT NULL,PURCHASE_STORE varchar(30) not null,PURCHASE_MODE varchar(30) not null,PURCHASE_QUANTITY integer(4) not null,PURCHASE_AMOUNT integer(4) not null,DEFECTIVE integer(4) not null);'

# CREATING SALES TABLE

S_table = 'CREATE TABLE SALES (PRODUCT_ID integer(4) not null,PRODUCT_NAME varchar(30) not null,SALES_QUANTITY integer(4) not null,SALES_DATE date NOT NULL,SALES_AMOUNT integer(4) not null,PROFIT_MARGIN integer(4) not null);'

cur.execute(G_table)
cur.execute(P_table)
cur.execute(S_table)

# COST OF ITEMS
# -- WOODEN CHAIR - 500
# -- WOODEN TABLE - 1000
# -- RED-COLORED-TOYS - 200
# -- SHIRTS - 800


# INSERTING DATA INT MANUFACTURE TABLE

Z = "INSERT INTO MANUFACTURE VALUES (111,'Wooden Chair','SS Exports','2023-04-29',100,100,5,50000),(112,'Wooden Table','SS Exports','2023-04-29',100,100,7,100000),(113,'red-colored-toys','ABC Exports','2023-04-29',200,200,15,40000),(114,'shirt','AHSH Exports','2023-04-29',300,300,3,240000)";
cur.execute(Z)    

Z1 = "INSERT INTO MANUFACTURE VALUES (111,'Wooden Chair','SS Exports','2023-04-30',100,100,5,50000),(112,'Wooden Table','SS Exports','2023-04-30',100,100,7,100000),(113,'red-colored-toys','ABC Exports','2023-04-30',200,200,15,40000),(114,'shirt','AHSH Exports','2023-04-30',300,300,3,240000);"
cur.execute(Z1)


Z2 = "INSERT INTO MANUFACTURE VALUES (111,'Wooden Chair','SS Exports','2023-05-01',100,100,3,50000),(112,'Wooden Table','SS Exports','2023-05-01',100,100,11,100000),(113,'red-colored-toys','ABC Exports','2023-05-01',200,200,6,40000),(114,'shirt','AHSH Exports','2023-05-01',300,300,18,240000);"

Z3 = "INSERT INTO MANUFACTURE VALUES (111,'Wooden Chair','SS Exports','2023-05-02',100,100,3,50000),(112,'Wooden Table','SS Exports','2023-05-02',100,100,11,100000),(113,'red-colored-toys','ABC Exports','2023-05-02',200,200,6,40000),(114,'shirt','AHSH Exports','2023-05-02',300,300,18,240000);"


Z4 = "INSERT INTO MANUFACTURE VALUES (111,'Wooden Chair','SS Exports','2023-05-03',100,100,3,50000),(112,'Wooden Table','SS Exports','2023-05-03',100,100,11,100000),(113,'red-colored-toys','ABC Exports','2023-05-03',200,200,6,40000),(114,'shirt','AHSH Exports','2023-05-03',300,300,18,240000);"

cur.execute(Z2)
cur.execute(Z3)
cur.execute(Z4)
mydb.commit()


# INSERTING DATA INT GOODS TABLE

g1 = "INSERT INTO GOODS VALUES (111,'Wooden Chair','SS Exports','2023-04-29',80,500),(112,'Wooden Table','SS Exports','2023-04-29',60,1000), (113,'red-colored-toys','ABC Exports','2023-04-29',90,200), (114,'shirt','AHSH Exports','2023-04-29',80,800);"

g2 = "INSERT INTO GOODS VALUES (111,'Wooden Chair','SS Exports','2023-05-01',60,500),(112,'Wooden Table','SS Exports','2023-05-01',40,1000), (113,'red-colored-toys','ABC Exports','2023-05-01',70,200), (114,'shirt','AHSH Exports','2023-04-30',60,800);"

g3 = "INSERT INTO GOODS VALUES (111,'Wooden Chair','SS Exports','2023-05-02',50,500),(112,'Wooden Table','SS Exports','2023-05-02',30,1000), (113,'red-colored-toys','ABC Exports','2023-05-02',60,200), (114,'shirt','AHSH Exports','2023-05-02',50,800);"

g4 = "INSERT INTO GOODS VALUES (111,'Wooden Chair','SS Exports','2023-05-03',40,500),(112,'Wooden Table','SS Exports','2023-05-03',20,1000), (113,'red-colored-toys','ABC Exports','2023-05-03',50,200), (114,'shirt','AHSH Exports','2023-05-03',40,800);"

cur.execute(g1)
cur.execute(g2)
cur.execute(g3)
cur.execute(g4)
mydb.commit()


# # INSERTING DATA INT PURCHASE TABLE

p1 = "INSERT INTO PURCHASE VALUES (111,'Wooden Chair',511,'2023-05-05','MyCare','online',70,35000,0),(112,'Wooden Table',512,'2023-05-05','MyCare','offline',60,60000,0),(113,'red-colored-toys',513,'2023-05-05','MyKids','offline',80,16000,0),(114,'shirt',514,'2023-05-05','ORay','online',65,52000,0);"

p2 = "INSERT INTO PURCHASE VALUES (111,'Wooden Chair',511,'2023-05-05','MyCare','online',10,500,1),(112,'Wooden Table',512,'2023-05-05','MyCare','offline',20,20000,1),(113,'red-colored-toys',513,'2023-05-05','MyKids','offline',30,6000,1),(114,'shirt',514,'2023-05-05','ORay','online',20,16000,1);"

p3 = "INSERT INTO PURCHASE VALUES (111,'Wooden Chair',511,'2023-05-06','MyCare','online',70,35000,0),(112,'Wooden Table',512,'2023-05-06','MyCare','offline',60,60000,0),(113,'red-colored-toys',513,'2023-05-06','MyKids','offline',80,16000,0),(114,'shirt',514,'2023-05-06','ORay','online',65,52000,0),(111,'Wooden Chair',511,'2023-05-06','MyCare','online',10,500,1),(112,'Wooden Table',512,'2023-05-06','MyCare','offline',20,20000,1),(113,'red-colored-toys',513,'2023-05-06','MyKids','offline',30,6000,1),(114,'shirt',514,'2023-05-06','ORay','online',20,16000,1);"

p4 = "INSERT INTO PURCHASE VALUES (111,'Wooden Chair',511,'2023-05-07','MyCare','online',70,35000,0),(112,'Wooden Table',512,'2023-05-07','MyCare','offline',60,60000,0),(113,'red-colored-toys',513,'2023-05-07','MyKids','offline',80,16000,0),(114,'shirt',514,'2023-05-07','ORay','online',65,52000,0),(111,'Wooden Chair',511,'2023-05-07','MyCare','online',10,500,1),(112,'Wooden Table',512,'2023-05-07','MyCare','offline',20,20000,1),(113,'red-colored-toys',513,'2023-05-07','MyKids','offline',30,6000,1),(114,'shirt',514,'2023-05-07','ORay','online',20,16000,1);"

cur.execute(p1)
cur.execute(p2)
cur.execute(p3)
cur.execute(p4)
mydb.commit()


#  INSERTING DATA INT SALES TABLE

s1 = "INSERT INTO SALES VALUES (111,'Wooden Chair',70,'2023-05-10',49000,14000),(112,'Wooden Table',60,'2023-05-10',72000,12000),(113,'red-colored-toys',80,'2023-05-10',24000,8000),(114,'shirt',65,'2023-05-10',65000,13000);"


s2 = "INSERT INTO SALES VALUES (111,'Wooden Chair',70,'2023-05-11',49000,14000),(112,'Wooden Table',60,'2023-05-11',72000,12000),(113,'red-colored-toys',80,'2023-05-11',24000,8000),(114,'shirt',65,'2023-05-11',65000,13000);"

s3 = "INSERT INTO SALES VALUES (111,'Wooden Chair',70,'2023-05-12',49000,14000),(112,'Wooden Table',60,'2023-05-12',72000,12000),(113,'red-colored-toys',80,'2023-05-12',24000,8000),(114,'shirt',65,'2023-05-12',65000,13000);"

cur.execute(s1)
cur.execute(s2)
cur.execute(s3)
mydb.commit()


# EXECUTING QUERIES
# 1)FIRST QUERY

# -- Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, 
# -- manufactured on the date ‘01-04-23’.
query1 = "DELETE P FROM PURCHASE P JOIN MANUFACTURE M ON M.PRODUCT_ID = P.PRODUCT_ID WHERE PURCHASE_STORE='ORay' AND DEFECTIVE=1 AND M.MANUFACTURED_DATE='2023-04-29';"
cur.execute(query1)


# 2)SECOND QUERY

# -- Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
query2 = "UPDATE MANUFACTURE M JOIN PURCHASE P ON P.PRODUCT_ID = M.PRODUCT_ID SET NEED_TO_BE_MANUFACTURED = NEED_TO_BE_MANUFACTURED+PURCHASE_QUANTITY WHERE M.PRODUCT_NAME = 'red-colored-toys' AND P.PURCHASE_STORE='MyKids' ;"


# 3)THIRD QUERY

# -- Display all the “wooden chair” items that were manufactured before the 1st May 2023. 
query3 = "SELECT * FROM MANUFACTURE WHERE PRODUCT_NAME='Wooden Chair' AND MANUFACTURED_DATE<='2023-05-01';"
cur.execute(query3)
dis = cur.fetchall()
for i in dis:
    print(i)


# 4)FOURTH QUERY

# -- Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, 
# -- manufactured by the “SS Export” company.
query4 = "SELECT DISTINCT SUM(PROFIT_MARGIN) AS PROFIT_MARGIN FROM SALES S JOIN PURCHASE P ON P.PRODUCT_ID = S.PRODUCT_ID JOIN MANUFACTURE M ON M.PRODUCT_ID = S.PRODUCT_ID WHERE S.PRODUCT_NAME='Wooden Table' AND P.PURCHASE_STORE = 'MyCare' AND M.MANUFACTURED_COMPANY = 'SS Exports' GROUP BY SALES_DATE;"
cur.execute(query4)
dis = cur.fetchall()
for i in dis:
    print(i)


mydb.commit()
print("PROJECT COMPLETED SUCCESSFULLY")