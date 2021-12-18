import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'postgres',
    password = 'test123',
    db = 'tztest',
    charset = 'utf8'
)

cur = conn.cursor() #创建一个游标对象

# #创建数据表
cur.execute('DROP TABLE if EXISTS product')
sql = '''
CREATE TABLE product(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(20),
brand VARCHAR(20),
category VARCHAR(20)
);
'''
cur.execute(sql)
#添加数据
insertSql = '''
INSERT INTO product (name,brand,category) VALUES ('QQ','Tencent','IT'),('STEAM','Valve','GAME'),('WINDOWS','Microsoft','IT');
'''
try:
    cur.execute(insertSql)
    conn.commit()
except:
    conn.rollback()

#查询
selectSql = '''
SELECT * FROM product;
'''
try:
    cur.execute(selectSql)
    results = cur.fetchall()
    for row in results:
        p_id = row[0]
        p_name = row[1]
        p_brand = row[2]
        p_category = row[3]
        print(p_id,p_name,p_brand,p_category)
except:
    print("Error Sql")

#更新
updateSql = '''
UPDATE product SET product.name = 'WeGame',product.category = 'Game' WHERE id = 1;
'''
try:
    cur.execute(updateSql)
    conn.commit()
except:
    conn.rollback()

#查询更新的那一条
selectSql1 = '''
SELECT * FROM product WHERE id = 1;
'''
try:
    cur.execute(selectSql1)
    results = cur.fetchall()
    for row in results:
        p_id = row[0]
        p_name = row[1]
        p_brand = row[2]
        p_category = row[3]
        print(p_id,p_name,p_brand,p_category)
except:
    print("Error Sql")

#删除
deleteSql = '''
DELETE FROM product WHERE id = 3; 
'''
try:
    cur.execute(deleteSql)
    conn.commit()
except:
    conn.rollback()

#查询删除的那一条
selectSql2 = '''
SELECT * FROM product WHERE id = 3;
'''
try:
    count = cur.execute(selectSql2)
    if count == 0:
        print("delete this")
except:
    print("Error Sql")

#关闭数据库
conn.close()

