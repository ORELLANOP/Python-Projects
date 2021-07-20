__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

#CONSTANTES
ADICIONAL = 0.30

#Titulo y carga de datos
print("Programa que calcula el precio del boleto de un colectivo de media distancia")
costo = float(input("Ingrese el costo del boleto: "))
kilometros = int(input("Ingrese los kilometros a realizar: "))


#Proceso
costo_boleto = costo + (kilometros * ADICIONAL)

#Resultados
print("El costo final del boleto es:", costo_boleto)
