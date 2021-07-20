__author__ = 'Catedra Algoritmos y Estructuras de Datos'

#CONSTANTE
C = 299792.458

#Titulo y carga de datos
print("Programa que calcula la energía de una masa determinada")
masa = float(input("Ingrese la masa en kg: "))

#Proceso
energia = masa * (C**2)

#Resultado
print("La energia de la masa ingresada es: ", energia)
