"""Programa que determina las letras que nunca aparecen repetidas segun
el diccionario sowpods
Autor: Carlos Da Silva(10-10175)
Last Modified: 8/11/2013.

"""

import sys
import string

abecedario=string.ascii_lowercase  # Procesaremos todas las letras de este abecedario

def procesar_letra(lista,letra):
  """Dada una lista de palabras y una letra, determina
  si dicha letra aparece repetida en al menos una de las palabras de
  la lista.
     
  """
  abuscar=letra+letra #Hacemos el string a buscar
  abuscar=abuscar.upper()
  for a in lista:
    if abuscar in a:
      return True
  return False

def procesar_abecedario(lista):
  """Funcion que dada una lista de palabras, iterara sobre las letras del 
  abecedario y devolvera una lista de aquellas que no aparezcan repetidas
  en ninguna palabra de la lista.
  
  """
  no_repetidas=[]
  for a in abecedario:
    if not (procesar_letra(lista,a)):
      no_repetidas.append(a)
  return no_repetidas
      
#Leemos el archivo que entrara como parametro por la linea de comandos
with open(sys.argv[1]) as data:
  data2 = data.readlines()
  
respuesta=procesar_abecedario(data2)  # Procesamos todas las letras del abecedario


print "-->Las letras que no aparecen repetidas son:"
for a in respuesta:
  print "   >'{}'".format(a)
  
with open('respuesta2.txt','w') as datar:  #Escribimos la solucion en archivo de respuestas
  for a in respuesta:
    temp="'"+a+"' "
    datar.write(temp)