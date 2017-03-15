#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
Recibe una lista de enteros y calcula la media aritmetica
"""""

print("Programa para calcular la media(promedio) aritmetica de una lista de enteros")

from random import randint

def genera_lista_entero(longitud=0):
    lista=[]
    if(longitud<1):
        longitud=randint(1,30)
    for i in range(longitud):
        lista.append(randint(1,10))
    return lista

def genera_promedio_lista(lista):
    promedio=0
    for i in lista:
        promedio+=i
    promedio/=len(lista)
    return promedio

lista_enteros=genera_lista_entero()
promedio=genera_promedio_lista(lista_enteros)

print("Lista de enteros:")
print(lista_enteros)
print("")
print("El promedio de la lista dada es " + str(promedio))


