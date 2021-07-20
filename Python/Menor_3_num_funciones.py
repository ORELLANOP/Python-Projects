__author__ = 'Cubo y cuadrado de menor de 3 numeros'

# Subproblema 1: determinar el menor
def menor (n1, n2, n3):
    if n1 < n2 and n1 < n3:
        mn = n1
    else:
        if n2 < n3:
            mn = n2
        else:
            mn = n3
    return mn

# Subproblema 2: Calcular cuadrado y cubo

def calcular(mn):
    c2 = mn ** 2
    c3 = mn ** 3
    return c2, c3

# Programa principal
# Titulos y carga de datos

print("Calculo del cuadrado y cubo del menor ")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))


# Procesos
# Invocar las funciones en el orden correcto de aplicacion
men = menor(a, b, c)
cuad, cub = calcular(men)


# Visualización de los resultados
print("Menor: ", men)
print("Cuadrado: ", cuad)
print("Cubo: ", cub)
