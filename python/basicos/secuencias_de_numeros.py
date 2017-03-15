#! /usr/bin/env python

"""
Autor: Salamandra
Url del ejercicio: http://www.iaa.es/python/ejercicios/
Nota: Estos son 5 ejercicios reunidos en uno solo
Imprime por pantalla la secuencia [0, 1, 2, ... 100]
Imprime por pantalla la secuencia [0, 2, 4, ... 200]
Imprime por pantalla la secuencia [86, 84, 82, ... 14]
Imprime por pantalla la secuencia [10, 9, 8, ... 0]
"""""

def genera_secuencia_numeros(inicio,fin,conteo=1):
    secuencia=""
    for i in range(inicio,fin,conteo):
        secuencia+=str(i) + " "
    return secuencia

print("Programa para imprimir en consola diferentes secuencias de numeros")

# Secuencias #
cero_a_cien=genera_secuencia_numeros(0,101)
cero_a_docientos=genera_secuencia_numeros(0,201)
ochenta_y_seis_a_catorce=genera_secuencia_numeros(86,14,-2)
diez_a_cero=genera_secuencia_numeros(10,0,-1)

# Mostrar en consola #
print(cero_a_cien)
print(cero_a_docientos)
print(ochenta_y_seis_a_catorce)
print(diez_a_cero)