__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

#Titulo y carga de datos
print("Programa que separa el ultimo y los dos ultimos digitos de un entero")
numero = int(input("Ingrese un numero entero: "))

#Proceso
ultimo_digito = numero % 10
ultimo_dos_digitos = numero % 100

#Presentacion de datos

print("El ultimo digito del numero entero ingresado es:", ultimo_digito)
print("Los ultimos digitos del numero entero ingresado son:", ultimo_dos_digitos)

