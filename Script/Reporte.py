#!/usr/bin/env python
# -*- coding: utf-8
 
import os
import re
Reporte = open('Reporte.txt', 'w')
durazno = open('durazno.sql', 'w')
florida = open('florida.sql', 'w')
Reporte.write('Se ejecitaron los siguientes scripts:'+'\n')
#Variable para la ruta al directorio
path = '.'
 
#Lista vacia para incluir los ficheros
listaArchivos = []
 
#Lista con todos los ficheros del directorio:
listaDirectorio = os.walk(path)   #os.walk()Lista directorios y ficheros
 
 
#Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.

for root, dirs, files in listaDirectorio:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".sql"):
            if 'Dur' in nombreFichero:
                Reporte.write('Script ejecutados en Durazno'+'\n')
                listaArchivos.append(nombreFichero+extension)
                Reporte.write(nombreFichero+extension +'\n')
                script = open(nombreFichero+extension, 'r')
                for i in script.readlines():
                    Reporte.write(i)
                    durazno.write(i)
            elif 'Flo' in nombreFichero:
                Reporte.write('Script ejecutados en Florida'+'\n')
                listaArchivos.append(nombreFichero+extension)
                Reporte.write(nombreFichero+extension +'\n')
                script = open(nombreFichero+extension, 'r')
                for i in script.readlines():
                    Reporte.write(i)
                    florida.write(i)

             
print(listaArchivos)            
print ('Reporte terminado')
print ("Cantidad de scripts en version = ", len(listaArchivos))
Reporte.close()
durazno.close()
florida.close()
script.close()
