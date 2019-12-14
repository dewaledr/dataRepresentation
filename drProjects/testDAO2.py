"""
This is mySQL DB connection or model code for datarepresentation using mysql-connector using connection pooling
Written by:     Francis ADEPOJU
Date Completed: December 15, 2019
"""
from customerDAO import customerDAO as cdao

# customer = cdao.getAll()
# for cus in customer:
#     print(cus)


c2 = cdao.findByID(20000)
print(c2)