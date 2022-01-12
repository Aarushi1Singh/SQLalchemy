import sqlalchemy as db
from sqlalchemy import create_engine, engine
from sqlalchemy import text
import sqlalchemy

engine = create_engine("mysql+pymysql://root:134340-a@localhost:3306/employee")

connection = engine.connect()
metadata = db.MetaData()
employee = db.Table('employee', metadata, autoload=True, autoload_with=engine)


result = engine.execute(text("SELECT * FROM employee"))

for i in result:
    print(i)

# OUTPUT
# (101, 'Rahul', 20000, 10)
# (102, 'Shiva', 20000, 20)
# (103, 'Riya', 5000, 40)
# (104, 'Sakshi', 20000, 10)
# (105, 'Pranav', 20000, 10)
# (106, 'Ananya', 20000, 10)
# (107, 'Palak', 20000, 20)
# (108, 'Shiv', 20000, 50)
# (109, 'Tanya', 5000, 40)
# (110, 'Akshat', 5000, 40)

result2 = engine.execute(text("SELECT departmentid, count(*) count FROM employee GROUP BY departmentid"))

for i in result2:
    print(i)

# OUTPUT
# (10, 4)
# (20, 2)
# (40, 3)
# (50, 1)

result3 = engine.execute(text("describe employee"))

for i in result3:
    print(i)

# OUTPUT
# ('id', 'int', 'YES', '', None, '')
# ('name', 'varchar(20)', 'YES', '', None, '')
# ('salary', 'int', 'YES', '', None, '')
# ('departmentid', 'int', 'YES', '', None, '')

result4 = engine.execute(text("select departmentid, sum(salary) from Employee where salary > 10000 group by departmentid"))

for i in result4:
    print(i)

# OUTPUT
# (10, Decimal('80000'))
# (20, Decimal('40000'))
# (50, Decimal('20000'))

result5 = engine.execute(text("SELECT DISTINCT departmentid, salary FROM employee order by salary"))

for i in result5:
    print(i)

# OUTPUT
# (40, 5000)
# (10, 20000)
# (20, 20000)
# (50, 20000)




