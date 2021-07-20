__author__ = 'Catedra de AED'

op = 0
while op != 11:


    #visualización de las opciones
    print("1_Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.")
    print("2_Edad promedio de los pacientes que pertenecen a grupo de riesgo (para pertenecer al grupo de riesgo el test debe ser negativo y tener más de 60 años).")
    print("3_Cantidad y porcentaje que el personal de salud representa sobre el total de casos.")
    print("4_Edad promedio entre los casos confirmados.")
    print("5_Menor edad entre los casos autóctonos.")
    print("6_Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.")
    print("7_Cantidad de casos confirmados con viaje al exterior.")
    print("8_Cantidad de casos sospechosos en contacto con casos confirmados.")
    print("9_Las regiones sin casos confirmados.")
    print("10_Porcentaje de casos positivos autóctonos sobre el total de positivos.")
    print("11) Salir del programa.")
    op = int(input("Ingrese el numero de la opcion elegida: "))

    if(op > 0) and (op < 12) and (op == int):


        #chequeo de la primera opcion
        if op == 1:
            print("1")


        #chequeo de la segunda opcion
        elif op == 2:
            print ("2")

        #chequeo de la tercera opcion
        elif op == 3:
            print ("3")

        #chequeo de la cuarta opcion
        elif op == 4:
            print ("4")

        #chequeo de la quinta opcion
        elif op == 5:
            print ("5")

        #chequeo de la sexta opcion
        elif op == 6:
            print ("6")

        #chequeo de la septima opcion
        elif op == 7:
            print ("7")

        #chequeo de la octava opcion
        elif op == 8:
            print ("8")

        #chequeo de la novena opcion
        elif op == 9:
            print ("9")

        #chequeo de la décima opcion
        elif op == 10:
            print ("10")
    else:
        print("Opción inválida. Ingrese otra opción que se encuentre en el menú")

print("Programa terminado")
