import mysql.connector
import sys
import datetime
now = datetime.datetime.now()
creation_time = now.strftime("%Y-%m-%d %H:%M:%S")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pirate0013",
    database="FB_VIEW"
)

mycursor = mydb.cursor()

mycursor.execute('''
    SELECT column_name
FROM information_schema.columns
WHERE  table_name = 'FB_USERS'
   AND table_schema = 'FB_VIEW'
''')

myresult = mycursor.fetchall()

classname = sys.argv[1]

fullclass = '''
<?php

namespace DAO;

use Kernel\DataBase\MySql;
use Kernel\Config\Constants;
use Kernel\Interfaces\IDataObject;

class {} extends MySql implements  IDataObject *[0]\n 

    CODE *[1]
     
'''
table = 'EKW_BOT_OPTION_ARGUMENTS'
copytobject = ""
protected = ""
setters = ""
getters = ""
code = ""
inserts = f'''INSERT INTO FB_VIEW.{table} ('''
updates = f'''UPDATE FB_VIEW.{table} SET '''
for columns in myresult:
    if len(columns[0]) > 2 or len(columns[0]) > 4:
        inserts += columns[0]+','
        updates += columns[0]+' = ?, '
    protected += "protected ${};\n".format(columns[0])
    setters += '''public function set{}(${})*[0] $this->{} = ${}; *[1]
    '''.format(columns[0],columns[0],columns[0],columns[0])
    getters += '''public function get{}()*[0] return $this->{}; *[1]
    '''.format(columns[0],columns[0])

    copytobject += '''$this->set{}($object["{}"]); 
            '''.format(columns[0],columns[0]);

    setters = setters.replace("*[0]","{").replace("*[1]","}")
    getters = getters.replace("*[0]","{").replace("*[1]","}")
inserts += ') VALUES ('
updates += ' WHERE USER_ID = ?;'
counter =0
for columns in myresult:

    if columns[0] != "ID" or columns[0] != "DATE":
        counter +=1
        inserts += "? , ".format(columns[0])

inserts += ');\n'
print("TOTAL ROW COUNT IS " + str(counter))
protected += """    protected $RETURN_TYPE; 
    public function __construct()
    *[0]
         parent::__construct();
    *[1]
    private function CopyObjects($Result, $certain = true)
    *[0]
        $copy = array();
        if($this->getReturnType() === Constants::JSON)
        {
            foreach ($Result as $object)
            *[0]
               if(!$certain)
               {
                    $id = $object['ID'];
                    $copy[$id] = $object;
               }
               else
               {
                    $copy = $object;
               }
            *[1]
            return $copy;
        *[1]
        foreach ($Result as $object){
            SETTERS;
        }
    }
    
    """
protected = protected.replace("SETTERS;",copytobject);
update = '''
    public function Update()*[0]
        
    *[1]
    public function Remove()*[0]
        
    *[1]
'''.format(classname,classname)
getters = getters + '''public function getReturnType()*[0] return $this->RETURN_TYPE;*[1]
    '''
setters = setters + '''public function setReturnType($type)*[0] $this->RETURN_TYPE = $type;*[1]'''
code = protected + setters + getters + update
fullclass = fullclass.format(classname)
fullclass = fullclass.replace("CODE",code)
fullclass = fullclass.replace("*[0]","{").replace("*[1]","}").replace("CREATEDTIME",creation_time)
print(fullclass)
print(inserts)
print(updates)

with open("../../DAO/"+classname+".php", "w") as writer:
    writer.write(fullclass)
    writer.close()