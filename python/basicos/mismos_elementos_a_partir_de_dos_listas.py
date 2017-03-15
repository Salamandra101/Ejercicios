#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
A partir de dos listas de enteros, 'numeros1' y 'numeros2', crea una lista que contiene aquellos valores de la
primera que tambien estan en la segunda e imprimela por pantalla. Es decir, calcula la interseccion de ambas listas.
"""""

lista1=[1,2,3,4,5,6,7,8,9]
lista2=[11,22,33,44,55,6,1,2]

nueva_lista=[]

for i in lista1:
    for j in lista2:
        if(i==j):
            nueva_lista.append(i)

print("La lista que se creo a partir de las dos listas dadas es la siguiente: ")
print(nueva_lista)

