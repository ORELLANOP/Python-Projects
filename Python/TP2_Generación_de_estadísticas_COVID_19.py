__author__ = 'Nombres de alumnos'


# Definición de bibliotecas
import random
import time

# Definición de las funciones


def promedio(m, n):
    if n != 0:
        prom = m / n
    else:
        prom = 0
    return prom


def porcentaje(m, n):
    if n != 0:
        porc = int((m * 100) / n)
    else:
        porc = 0
    return porc


def ingreso_usuario():

    # Inicialización de flags y contadores
    cl = 0
    csinp = 0
    ca = 0
    fcar = 0
    i = 0
    usu = 0

    while i < 3:
        # Carga del texto completo
        cadena = input("Cargue el nombre de usuario: ")

        # Ciclo for iterador para procesar el texto
        for car in cadena:
            # Contar la letra actual
            cl += 1

            tamano = len(cadena)

            if car == "@":
                fcar += 1
            if (cl == 1 and car == "@") or (cl == tamano and car == "@"):
                ca += 1
            elif (cl == 1 and car == ".") or (cl == tamano and car == "."):
                ca += 1
            elif car == ".":
                csinp += 1
                if csinp == 2:
                    ca += 1
                    csinp = 0

        if (ca != 0)or (fcar == 0) or (fcar > 1):
            print("Usuario invalido")
            i += 1
            cl = 0
            ca = 0
            fcar = 0
            csinp = 0
        else:
            usu += 1
            break

    if usu != 0:
        print("Sigue el programa")
        return True
    else:
        print("No debe seguir el programa")
        return False


def pacientes():
    print("Programa que genera estadísticas de COVID_19")
    eneable = ingreso_usuario()
    if eneable:

        # Definición de tuplas
        test = "Positivo", "Negativo"
        region = "Capital", "Gran Cordoba", "Norte", "Sur"
        contacto = "Si contacto", "No contacto"
        salud = "Es personal de salud", "No es personal de salud"
        viaje = "Viajo", "No viajo"

        # Definición e inicialización de contadores y acumuladores
        cedad_neg = 0
        cedad_pos = 0
        acedad_pos = 0
        acedad_neg = 0

        ctest = 0

        ccapital = 0
        cnorte = 0
        csur = 0
        cgcordoba = 0
        ccapital_neg = 0
        cnorte_neg = 0
        csur_neg = 0
        cgcordoba_neg = 0

        ccontacto = 0
        cper = 0
        cviajo = 0

        cautoc = 0

        minimo = 111
        num_pac = int(input("Ingrese la cantidad de pacientes a procesar: "))

        for pac in range(1, num_pac + 1):
            print("\n\nPaciente número: ", pac)

            edad = random.randint(1, 110)
            print("Edad: ", edad)

            test_1 = test[random.randint(0, 1)]
            print("El resultado del test es: ", test_1)
            ctest += 1
            if test_1 == "Positivo":
                cedad_pos += 1
                acedad_pos += edad
            elif edad > 60:
                cedad_neg += 1
                acedad_neg += edad

            region_1 = region[random.randint(0, 3)]
            print("La región del paciente es: ", region_1)
            if region_1 == "Capital":
                if test_1 == "Positivo":
                    ccapital += 1
                else:
                    ccapital_neg += 1

            elif region_1 == "Gran Cordoba":
                if test_1 == "Positivo":
                    cgcordoba += 1
                else:
                    cgcordoba_neg += 1

            elif region_1 == "Norte":
                if test_1 == "Positivo":
                    cnorte += 1
                else:
                    cnorte_neg += 1

            elif region_1 == "Sur":
                if test_1 == "Positivo":
                    csur += 1
                else:
                    csur_neg += 1

            contacto_1 = contacto[random.randint(0, 1)]
            print("El resultado del contacto es: ", contacto_1)
            if contacto_1 == "Si contacto":
                ccontacto += 1

            salud_1 = salud[random.randint(0, 1)]
            print("Personal de salud: ", salud_1)
            if salud_1 == "Es personal de salud":
                cper += 1

            viaje_1 = viaje[random.randint(0, 1)]
            print("Viaje al exterior: ", viaje_1)
            if (viaje_1 == "Viajo") and (test_1 == "Positivo"):
                cviajo += 1

            # Se trata de un caso autóctono?
            if(test_1 == "Positivo") and (contacto_1 == "No contacto") and (salud_1 == "No es personal de salud") and (viaje_1 == "No viajo"):
                print("El paciente: ", pac, " es un caso autoctono")
                cautoc += 1
                if minimo > edad:
                    minimo = edad

            else:
                print("El paciente: ", pac, " NO es un caso autoctono")

        # Menú de opciones
        op = 0
        while op != 11:

            # Visualización de las opciones
            time.sleep(5)
            print("\n\n\n\t\t\tMenu de opciones")
            print("\n1) Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.")
            print("2) Edad promedio de los pacientes que pertenecen a grupo de riesgo.")
            print("3) Cantidad y porcentaje que el personal de salud representa sobre el total de casos.")
            print("4) Edad promedio entre los casos confirmados.")
            print("5) Menor edad entre los casos autóctonos.")
            print("6) Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.")
            print("7) Cantidad de casos confirmados con viaje al exterior.")
            print("8) Cantidad de casos sospechosos en contacto con casos confirmados.")
            print("9) Las regiones sin casos confirmados.")
            print("10) Porcentaje de casos positivos autóctonos sobre el total de positivos.")
            print("11) Salir del programa.")
            op = int(input("\n\nIngrese el número de la opción elegida: "))

            if(op > 0) and (op < 12):

                # Chequeo de la primera opcion
                if op == 1:
                    print("\nOpción 1")
                    print("Cantidad de casos confirmados: ", cedad_pos)
                    pp = porcentaje(cedad_pos, num_pac)
                    print("El porcentaje sobre el total de casos es: ", pp, "%")

                # Chequeo de la segunda opcion
                elif op == 2:
                    print("\nOpción 2")
                    p = promedio(acedad_neg, cedad_neg)
                    print("Edad promedio de los pacientes de riesgo: ", p)

                # Chequeo de la tercera opcion
                elif op == 3:
                    print("\nOpción 3")
                    print("Cantidad de personal de salud: ", cper)
                    pp = porcentaje(cper, num_pac)
                    print("El porcentaje sobre el total de casos testeados es: ", pp, "%")

                # Chequeo de la cuarta opcion
                elif op == 4:
                    print("\nOpción 4")
                    p = promedio(acedad_pos, cedad_pos)
                    print("Edad promedio de los casos confirmados: ", p)

                # Chequeo de la quinta opcion
                elif op == 5:
                    print("\nOpción 5")
                    if minimo == 111:
                        print("No hay casos autoctonos")
                    else:
                        print("La menor edad entre los casos autoctonos es: ", minimo)

                # Chequeo de la sexta opcion
                elif op == 6:
                    print("\nOpción 6")
                    pp1 = porcentaje(ccapital, num_pac)
                    pp2 = porcentaje(cnorte, num_pac)
                    pp3 = porcentaje(csur, num_pac)
                    pp4 = porcentaje(cgcordoba, num_pac)
                    print("La cantidad de casos positivos en Capital es: ", ccapital, "y porcentaje es: ", pp1, "%")
                    print("La cantidad de casos positivos en Norte es: ", cnorte, "y porcentaje es: ", pp2, "%")
                    print("La cantidad de casos positivos en Sur es: ", csur, "y porcentaje es: ", pp3, "%")
                    print("La cantidad de casos positivos en el Gran Córdoba es: ", cgcordoba, "y porcentaje es: ", pp4, "%")

                # Chequeo de la septima opcion
                elif op == 7:
                    print("\nOpción 7")
                    print("La cantidad de casos confirmados que viajaron al exterior es de: ", cviajo)

                # Chequeo de la octava opcion
                elif op == 8:
                    print("\nOpción 8")
                    print("La cantidad de casos sospechosos en contacto con casos confirmados es: ", ccontacto)

                # Chequeo de la novena opcion
                elif op == 9:
                    print("\nOpción9")

                    if ccapital == 0:
                        print("En Cordoba Capital no hay casos confirmados")
                    elif cnorte == 0:
                        print("En el Norte no hay casos confirmados")
                    elif csur == 0:
                        print("En el Sur no hay casos confirmados")
                    elif cgcordoba == 0:
                        print("En Gran Cordoba no hay casos confirmados")
                    else:
                        print("No hay regiones sin casos confirmados")

                # Chequeo de la décima opcion
                elif op == 10:
                    print("\nOpción 10")
                    pp = porcentaje(cautoc, cedad_pos)
                    print("El porcentaje de casos positivos autóctonos sobre el total de positivos es: ", pp, "%")
            else:
                print("\nOpción no válida. Seleccione una opción que se encuentre en el menú.")

        print("Función terminada")

# Funcion principal


pacientes()
print("Fin del programa")
