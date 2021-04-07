import mysql.connector
import sys
import datetime
now = datetime.datetime.now()
creation_time = now.strftime("%Y-%m-%d %H:%M:%S")

fullclass = '''

import json

from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.Security.Global import levels
from Core.DataOperations.StringBuilder import StringBuilder


class CLASSNAME:
    
    CONSTRUCTOR
    
    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                EMPTY_DICT
        except KeyError as KeyErr:
            pass # print (True, 3, levels.Error) 

    def __repr__(self):
        buffer = StringBuilder()
        REPR_CONTENT 
'''


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SILICON"
)

mycursor = mydb.cursor()
classname = sys.argv[1]
tablename = sys.argv[2]
mycursor.execute('''
    SELECT column_name,data_type
FROM information_schema.columns
WHERE  table_name = '{}'
   AND table_schema = 'SILICON'
'''.format(tablename))

myresult = mycursor.fetchall()


init_arguments_pack = ''
init_setters = ''
empty_dict = 'return cls(**{RETURNS})'
empty_dict_returns = ''
repr = '''buffer.append("<{}:")'''.format(classname)

for column in myresult:
    type = column[1]
    if type == 'int':
        init_arguments_pack  += '''{}: int, '''.format(column[0])
    else:
        init_arguments_pack  += '''{}: str, '''.format(column[0])
    init_setters += '''         self.{} = {}\r\n'''.format(column[0],column[0])
    empty_dict_returns += ''''{}': 'empty', '''.format(column[0])

    if type == 'int':
        repr += '''        buffer.append(" {}=" + str(self.{}))\n'''.format(column[0],column[0])
    else:
        repr += '''        buffer.append(" {}=" + self.{})\n'''.format(column[0],column[0])

repr += '''        buffer.append(">")
        return buffer.string
'''
init_arguments_pack = init_arguments_pack[:len(init_arguments_pack)-2]
init = '''def __init__(self,{}):
{}
        '''.format(init_arguments_pack,init_setters)
empty_dict = empty_dict.replace('RETURNS', empty_dict_returns[:len(empty_dict_returns)-2])
fullclass = fullclass.replace("CONSTRUCTOR", init).replace("REPR_CONTENT",repr).replace("CLASSNAME",classname).replace("EMPTY_DICT", empty_dict)
print(fullclass)
