#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
Lee valores del usuario hasta que teclee un numero par, utilizando un bucle while
"""""

es_par=True
while es_par:
    ingreso=input("Ingrese un caracter: ")
    if(ingreso.isdigit() and int(ingreso)%2==0):
        print("¡Numero par!")
        es_par=False
    else:
        print("!Recuerda para finalizar ingrese un numero par!")

print("Adios.")