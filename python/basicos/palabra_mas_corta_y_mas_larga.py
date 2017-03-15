#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
Para cada una de las cadenas de texto almacenadas en una lista, imprimir por pantalla el indice y
la cadena en si e indicar si la palabra es demasiado corta (cinco o menos caracteres)
o larga (mas de cinco caracteres)
"""""

print("Program para calcular a partir de una cadena de texto si las palabra son cortas(menos de cinco caracteres) o largas( mas de cinco caracteres)")

texto=input("Ingrese el texto: ")
lista_de_palabras=texto.split()

for i in lista_de_palabras:
    print("La palabra \"" + i + "\" es:")
    if len(i)<5:
        print("Corta")
    else:
        print("Larga")
