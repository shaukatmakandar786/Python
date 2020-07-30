from sqlalchemy_examples.create_database_and_table_employee import Employee,Engine
from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=Engine)
session=Session()

id=int(input("enter employee id\n"))
name=input("enter employee name\n")
sal=int(input("enter employee salary\n"))

result=Employee(id,name,sal)
session.add(result)
session.commit()
print("data inserted successfully")


