#Programa que determina las letras que nunca aparecen repetidas segun
#el diccionario sowpods
#Autor: Carlos Da Silva(10-10175)
#Last Modified: 8/11/2013

import sys
import string

#Abecedario sobre el cual determinaremos si cada letra cumple la propiedad
#deseada
abecedario=string.ascii_lowercase
abecedario=list(abecedario)


#Leemos el archivo que entrara como parametro por la linea de comandos
data = open(sys.argv[1])
data2 = list(data) #Listamos cada linea del documento 

#Funcion que dada una lista de palabras y una letra, determina
#si dicha letra aparece repetida en al menos una de las palabras de
#la lista
def procesar_letra(lista,letra):
  abuscar=letra+letra #Hacemos el string a buscar
  abuscar=abuscar.upper()
  for a in lista:
    if abuscar in a:
      return True
  return False

#Funcion que dada una lista de palabras, iterara sobre las letras del 
#abecedario y devolvera una lista de aquellas que no aparezcan repetidas
#en ninguna palabra de la lista
def procesar_abecedario(lista):
  no_repetidas=[]
  for a in abecedario:
    if procesar_letra(lista,a):
      pass
    else:
      no_repetidas.append(a)
  return no_repetidas
      
#Leemos el archivo que entrara como parametro por la linea de comandos
data = open(sys.argv[1])
data2 = list(data) #Listamos cada linea del documento 

#Llamamos a la funcion que procesara todas las letras del abecedario
respuesta=procesar_abecedario(data2)

#Salida de datos: Escribimos aquellas que hayan cumplido con lo deseado
print "-->Las letras que no aparecen repetidas son:"
for a in respuesta:
  print "   >","'",a,"'"
  
#Adicionalmente escribimos la respuesta en un archivo
f = open('respuesta.txt', 'w')
for a in respuesta:
  temp="'"+a+"' "
  f.write(temp)
f.close()
data.close()