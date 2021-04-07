import mysql.connector
import sys

argType = sys.argv[1]
tableName = sys.argv[2]

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pirate0013",
    database="FB_VIEW"
)

mycursor = mydb.cursor()

mycursor.execute(f'''SELECT column_name FROM information_schema.columns WHERE  table_name = '{tableName}' AND table_schema = 'FB_VIEW' ''')
columns = mycursor.fetchall()

insert = ""
update = ""
delete = ""
bindings = ""
binding_types = '"'
binding_values = ""
columns_chain = ""
anonymousvalues = ""

for index, column in enumerate(columns):
    column = column[0]
    if column != "ID" and column != "DATE":
        columns_chain += str(column) + ","
        anonymousvalues += "?, "
        binding_types += 's'
        binding_values += f"$this->{column}, "

columns_chain = columns_chain[:-1]
anonymousvalues = anonymousvalues[:-2]
binding_types +='", '
binding_values = binding_values[:-1]
bindings = binding_types + binding_values
if argType == "insert":
    insert = f'''INSERT INTO FB_VIEW.{tableName} ({columns_chain}) VALUES ({anonymousvalues});'''
    print(insert)
    print(bindings)
if argType == "update":
    update = f'''UPDATE SET '''

if argType == "delete":
    pass
