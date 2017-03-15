#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
Lee una cadena de texto del usuario y para cada letra indica si es una vocal o una consonante
"""""

def es_vocal(caracter):
    if(caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u"):
        return True
    return False


cadena=input("Ingrese el texto: ").lower()

for i in cadena:
    print("El caracter \"" + i + "\"")
    if(i.isalpha()):
        if(es_vocal(i)):
            print(" es una vocal")
        else:
            print(" es una consonante")
    else:
        print(" no es una consonante ni vocal")