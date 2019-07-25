import os
import shutil
from peewee import *
from mysql.connector import (connection)
#BaseDeDatos=input('Introduzca el nombre de la Base a usar:')
bd = connection.MySQLConnection(user='root', password='admin123', host='127.0.0.1', database='prueba')
cursor = bd.cursor()

try:
    with open('florida.sql','r') as F:
        script = F.read()
        for n in cursor.execute(script, multi=True): pass
        #cursor.execute(script, multi = True)
        bd.commit()
        F.close()
        shutil.copy("florida.sql", "PRODflorida.sql")
        os.remove("florida.sql")
except FileNotFoundError:
            print('No hay Script para Florida')

try:
    with open('durazno.sql','r') as D:
        script = D.read()
        for n in cursor.execute(script, multi=True): pass
        #cursor.execute(script, multi = True)
        bd.commit()
        D.close()
        shutil.copy("durazno.sql", "PRODdurazno.sql")
        os.remove("durazno.sql")
except FileNotFoundError:
            print('No hay Script para Durazno')
bd.close()
