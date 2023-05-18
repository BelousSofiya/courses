# Given a database with (at least) two tables: customers and orders as shown below, write an SQL query that returns the
# order_num, order amount and customer name for all orders between $500 and $2000 inclusive, ordered by order_num.
#
# FIRST 5 ROWS OF CUSTOMERS TABLE, ORDERED BY ID
# id      name             city          grade   salesperson_id
# ------  ---------------  ------------  ------  --------------
# 3001    Brad Guzan       London        100     5005
# 3002    Nick Rimando     New York      100     5001
# 3003    Jozy Altidore    Kyiv          200     5007
# 3004    Fabian Johns     Paris         300     5006
# 3005    Graham Zusi      California    200     5002
# FIRST 5 ROWS OF ORDERS TABLE ORDERED BY ORDER_NUM
# order_num   amount     date        customer_id  saleperson_id
# ----------  ---------  ----------  -----------  -------------
# 70001       150.5      2022-10-05  3005         5002
# 70002       65.26      2022-10-05  3002         5001
# 70003       2480.4     2022-10-10  3009         5003
# 70004       110.5      2022-08-17  3009         5003
# 70005       2400.6     2022-07-27  3007         5001
# For example:
#
# Test	Result
# -- Testing with original db
# order_num   amount      name
# ----------  ----------  ---------------
# 70007       948.5       Graham Zusi
# 70010       1983.43     Fabian Johns

# SELECT order_num, amount, name
# FROM customers JOIN orders ON customer_id = customers.id
# WHERE amount >= 500 AND amount <= 2000
# ORDER BY order_num
#
# #Tests
#
# -- Testing with original db
# order_num   amount      name
# ----------  ----------  ---------------
# 70007       948.5       Graham Zusi
# 70010       1983.43     Fabian Johns
#
# -- Testing with extra rows
# order_num   amount      name
# ----------  ----------  ---------------
# 69007       500.0       Graham Zusi
# 70007       948.5       Graham Zusi
# 70010       1983.43     Fabian Johns
# 70014       2000.0      Jozy Altidore

