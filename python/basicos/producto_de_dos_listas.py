#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
A partir de dos listas de enteros, 'numeros1' y 'numeros2', crea una lista que contiene aquellos valores de la
primera que tambien estan en la segunda e imprimela por pantalla. Es decir, calcula la interseccion de ambas listas.
"""""

from random import randint

def genera_lista_entero(longitud=0):
    lista=[]
    if(longitud<1):
        longitud=randint(1,30)
    for i in range(longitud):
        lista.append(randint(1,10))
    return lista

def genera_lista_producto_listas(lista1,lista2):
    nueva_lista=[]
    for i in range(len(lista1)):
        nueva_lista.append(lista1[i]*lista2[i])
    return nueva_lista

lista1=genera_lista_entero()
lista2=genera_lista_entero(len(lista1))
producto_lista=genera_lista_producto_listas(lista1,lista2)

print("Primera lista:")
print(lista1)
print("Segunda lista:")
print(lista2)
print("")
print("El producto de cada uno de los item de las dos lista son:")
print(producto_lista)