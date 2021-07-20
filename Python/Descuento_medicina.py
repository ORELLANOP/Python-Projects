__author__ = 'Catedra Algoritmos y Estructuras de Datos'

#CONSTANTE
DESCUENTO = 0.35

#Titulo y carga de datos
print("Calculo de precio de medicamento con descuento")
precio = float(input("Ingresar el precio del medicamento: "))

#Proceso
precio_descuento = precio * DESCUENTO
precio_final = precio - precio_descuento

#Resultado
print("El precio total del medicamento es: ", precio)
print("El monto descontado del medicamento es: ", precio_descuento)
print("El precio a pagar por el medicamento es: ", precio_final)
