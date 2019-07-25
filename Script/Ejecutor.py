import os
import shutil
from peewee import *
from mysql.connector import (connection)
#BaseDeDatos=input('Introduzca el nombre de la Base a usar:')
bd = connection.MySQLConnection(user='root', password='admin123', host='127.0.0.1', database='prueba')
cursor = bd.cursor()
with open('florida.sql','r') as D:
    script = D.read()
cursor.execute(script)
bd.commit();
D.close()
shutil.copy("florida.sql", "PRODflorida.sql")
os.remove("florida.sql")

with open('durazno.sql','r') as F:
    script = F.read()
cursor.execute(script)
bd.commit();
F.close()
bd.close()
shutil.copy("durazno.sql", "PRODdurazno.sql")
os.remove("durazno.sql")

