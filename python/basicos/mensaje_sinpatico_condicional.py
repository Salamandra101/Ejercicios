#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
Lee una cadena de texto del usuario e imprime por pantalla un mensaje simpatico si y solo si contiene todas las vocales
"""""

def tiene_todas_las_vocales(texto):
    if(("a" in texto or "á" in texto) and ("e" in texto or "é" in texto) and ("i" in texto or "í" in texto) and ("o" in texto or "ó" in texto) and ("u" in texto or "ú" in texto)):
        return True
    return False

print("Programa para imprimir un mensaje simpatico si un texto ingresado tiene todas las vocales")

texto_ingresado=input("Ingrese el texto: ")

if(tiene_todas_las_vocales(texto_ingresado)):
    print("¡Muy bien hecho!")