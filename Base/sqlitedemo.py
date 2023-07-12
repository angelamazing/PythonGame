import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# table_sql = """
# create table user(
#   id INTEGER PRIMARY KEY autoincrement NOT NULL ,
#   name text NOT NULL,
#   age INTEGER NOT NULL
# )
# """
# cursor.execute(table_sql)
# conn.commit()  # 一定要提交,否则不会执行sql
# conn.close()

# sql_lst = [
#     "insert into user(name, age)values('lili', 18)",
#     "insert into user(name, age)values('poly', 19)",
#     "insert into user(name, age)values('lilei', 30)"
# ]
# for sql in sql_lst:
#     cursor.execute(sql)
#     conn.commit()
# conn.close()


sql = "select * from user"
cursor.execute(sql)
rows = cursor.fetchall()  # 获取全部数据
for row in rows:
    print(row.keys(), tuple(row))

conn.close()