# Create a Python program to use the sqlite database named "q1.db". The query to the database should display information,
# as shown in the example below, including phrases: about the successful connection, the total number of records, the
# actual records, the record of closing the database. From the table of "customers" to deduce all records for which in
# a "grade" field of value more than 200 with sort ordering on id
# For example output:
#
# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001
#
#
# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002
#
#
# The SQLite connection is closed

import sqlite3 as sq

with sq.connect("q1.db") as con:
    print("Connected to SQLite")
    cur = con.cursor()
    lst = cur.execute("""SELECT * FROM customers
                   WHERE grade > 200
                   ORDER BY id""")
    lst_cust = cur.fetchall()
    print(f"Total rows are:   {len(lst_cust)}")
    print("Printing each row")
    for cust in lst_cust:
        print(f"Id:  {cust[0]}", f"Name:  {cust[1]}", f"City:  {cust[2]}",
              f"Grade:  {cust[3]}", f"Seller:  {cust[4]}", "", "", sep='\n')

    cur.close()
print("The SQLite connection is closed")

#Tests

#Expect
# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3004
# Name:  Fabian Johns
# City:  Paris
# Grade:  300
# Seller:  5006
#
#
# Id:  3008
# Name:  Julian Green
# City:  London
# Grade:  300
# Seller:  5002
#
#
# The SQLite connection is closed
