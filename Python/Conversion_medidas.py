__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

#Titulo y carga de datos
print("Programa que convienrte unidades de medidas")
pies = float(input("Ingrese una medida en pies: "))

#Procesos
pulgadas = 12 * pies
yarda = pies / 3
centimetros = pulgadas * 2.54
metro = centimetros / 100

#Presentacion de los resultados

print( pies, "pies corresponde a: ", pulgadas, "pulgadas ",yarda, "yardas ", centimetros, "centimetros y ", metro, "metros")
