__author__ = 'Cubo y cuadrado de menor de 3 numeros'

# Titulos y carga de datos
print('Determinacion del cuadrado y el cubo del menor')
a = int(input('Primer numero: '))
b = int(input('Segundo numero: '))
c = int(input('Tercer numero: '))


#Procesos
#Subproblema 1: Determinar el menor
if a < b and a < c:
    men = a
else:
    if b < c:
        men = b
    else:
        men = c

#Subproblema 2: calcular el cubo y el cuadrado del menor
cuad = men ** 2
cubo = men ** 3

#Visualizacion de los resultados
print("El menor es: ", men)
print("Su cuadrado es: ", cuad)
print("Su cubo es: ", cubo)

