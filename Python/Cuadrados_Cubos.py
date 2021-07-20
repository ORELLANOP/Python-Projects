__author__ = 'Catedra Algoritmos y Estructuras de Datos'

#Titulo y carga de datos
print("Calculo de cuadrado y cubo de dos numeros")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#Proceso
sum_cuad = num1**2 + num2**2
prom_cub = (num1**3 + num2**3)/2

#Resultado
print("La suma del cuadrado de los numeros ingresados es:", sum_cuad)
print("El promedio de los numeros ingresados es:", prom_cub)
