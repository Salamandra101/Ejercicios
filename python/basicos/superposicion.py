# Autor: Salamandra
#Url del ejercicio: http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
# Definir una función superposicion.py() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.


def superposicion(lista1,lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if(elemento1==elemento2):
                return True
    return False

primera_lista=[2,3,5,767,"a","b","z"]
segunda_lista=[10,111,22,33,44,"f","AA"]

print(superposicion(primera_lista,segunda_lista))