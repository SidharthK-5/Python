import sqlite3

connection = sqlite3.connect("example1.db")
c = connection.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY,NAME TEXT,SALARY REAL)"""
)

"""All statements should be commented once it is run successfully"""

# c.execute("""INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,"ABC",80000)""")
# c.execute("""INSERT INTO EMP(ID,NAME,SALARY) VALUES(102,"PQR",70000)""")
# c.execute("""INSERT INTO EMP(ID,NAME,SALARY) VALUES(103,"XYZ",45000)""")
# c.execute("""INSERT INTO EMP(ID,NAME,SALARY) VALUES(104,"RST",30000)""")
# connection.execute("COMMIT")

# c.execute("SELECT * FROM EMP")
# for row in c:
#     print(row)

# c.execute("UPDATE EMP SET SALARY=65000 WHERE ID=102")
# connection.execute("COMMIT")

c.execute("DELETE FROM EMP WHERE ID=103")
connection.execute("COMMIT")
