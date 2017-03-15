# Autor: Salamandra
#Url del ejercicio: http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def procedimiento(lista):
    for i in lista:
        print("*"*i)

lista=[1,5,7,12,3,7,9,15]

procedimiento(lista)