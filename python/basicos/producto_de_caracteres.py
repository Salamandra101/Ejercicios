# Autor: Salamandra
#Url del ejercicio: http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(caracter,cantidad):
    return caracter*cantidad

print("Programa para generar una cantidad de caracteres dados")

caracter=input("Ingrese el caracter: ")
cantidad=int(input("Ingrese la cantidad de veces que quiera el que caracter '" + caracter + "' se desea repetir: "))

print(generar_n_caracteres(caracter,cantidad))
