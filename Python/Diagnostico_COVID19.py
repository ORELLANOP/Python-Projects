print("\t\t\t\t\t\t\t\t#############################################")
print("\t\t\t\t\t\t\t\t##         Diagnóstico de covid-19         ##")
print("\t\t\t\t\t\t\t\t#############################################\n")

# Variable bandera
sosp = False

# Primera carga de datos
print("\n\t\t\t\t\t\t\t\t\t\t\t---------------------")
print("\t\t\t\t\t\t\t\t\t\t\t| Ingrese sus datos |")
print("\t\t\t\t\t\t\t\t\t\t\t---------------------")

nombre = input("\nIngrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
temperatura = float(input("Ingrese su temperatura corporal en °C: "))
neumonia = input("\n¿Posee usted un diagnóstico clínico y radiológico de neumonia? Responda si/no: ")

# Diagnostico de neumonía

if neumonia == "si":
    print("\n\t\t\t\t\t\t\t--------------------------------------------------------")
    print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso SOSPECHOSO de Covid-19.|")
    print("\t\t\t\t\t\t\t--------------------------------------------------------")

# No tiene neumonía, por lo tanto continua la carga de datos y pregunta por la temperatura corporal.

# Segunda carga de datos

elif temperatura > 37:
    print("\n\t\t\t\t\t\t\t\t\t--------------------------------------")
    print("\t\t\t\t\t\t\t\t\t| Ingrese sus síntomas y actividades |")
    print("\t\t\t\t\t\t\t\t\t--------------------------------------")
    print("\n¿Posee usted alguno de los siguientes sintomas respiratorios? Responda por si/no:  ")
    tos = input("\t\tTos: ")
    odinofagia = input("\t\tOdinofagia: ")
    prob_resp = input("\t\tProblemas respiratorios: ")


# En este punto la persona ya tiene fiebre y si tiene 1 o más sintomas respiratorios por lo tanto continuamos con la carga de datos.

# Tercera carga de datos
    if tos == "si" or odinofagia == "si" or prob_resp == "si":

        pac_salud = input("\n¿Es usted personal de salud? Responda por si/no: ")
        print("\nResponda por si/no si realizó usted alguna de las siguientes actividades en los últimos 14 dias: ")

        casos_conf = input("\t\t¿Ha estado usted en contacto con casos confirmados de COVID-19?: ")
        viaje_ext = input("\t\t¿Ha realizado usted algún viaje fuera del país?: ")
        zonas_transm = input("\t\t¿Ha usted viajado o se ha alojado en zonas de transmisión local de COVID-19 en Argentina?: ")

# Hasta acá es la carga de datos ordenada según el enunciado.
# --------------------------------------------------------------------------------------------------------------------------------
        if pac_salud == "si":
            sosp = True
        elif casos_conf == "si" or viaje_ext == "si" or zonas_transm == "si":
            sosp = True
        elif edad > 60:
            print("\n\t\t\t\t\t\t\t--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso NO SOSPECHOSO de Covid-19 pero pertenece al grupo de riesgo.|")
            print("\t\t\t\t\t\t\t---------------------------------------------------------------------------------------------")
        else:
            print("\n\t\t\t\t\t\t\t--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso NO SOSPECHOSO de Covid-19 y NO pertenece al grupo de riesgo.|")
            print("\t\t\t\t\t\t\t--------------------------------------------------------------------------------------------")

# Hasta acá la condición de ser sospechoso
# ----------------------------------------------------------------------------------------------------------------------------------
        if (tos == "si" and odinofagia == "si") or (prob_resp == "si" and tos == "si") or (prob_resp == "si" and odinofagia == "si"):
            if casos_conf != "si" and viaje_ext != "si" and zonas_transm == "si" and pac_salud != "si":
                print("\n\t\t\t\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso AUTOCTONO de Covid-19.|")
                print("\t\t\t\t\t\t\t-------------------------------------------------------")
            elif sosp:
                print("\n\t\t\t\t\t\t\t--------------------------------------------------------")
                print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso SOSPECHOSO de Covid-19.|")
                print("\t\t\t\t\t\t\t--------------------------------------------------------")
        elif sosp:
                print("\n\t\t\t\t\t\t\t--------------------------------------------------------")
                print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso SOSPECHOSO de Covid-19.|")
                print("\t\t\t\t\t\t\t--------------------------------------------------------")

# Hasta acá la condición de ser Autóctono.
# ----------------------------------------------------------------------------------------------------------------------------------
    elif edad > 60:
        print("\n\t\t\t\t\t\t\t--------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso NO SOSPECHOSO de Covid-19 pero pertenece al grupo de riesgo.|")
        print("\t\t\t\t\t\t\t---------------------------------------------------------------------------------------------")
    else:
        print("\n\t\t\t\t\t\t\t--------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso NO SOSPECHOSO de Covid-19 y NO pertenece al grupo de riesgo.|")
        print("\t\t\t\t\t\t\t---------------------------------------------------------------------------------------------")
elif edad > 60:
    print("\n\t\t\t\t\t\t\t--------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso NO SOSPECHOSO de Covid-19 pero pertenece al grupo de riesgo.|")
    print("\t\t\t\t\t\t\t---------------------------------------------------------------------------------------------")
else:
    print("\n\t\t\t\t\t\t\t--------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t| Diagnóstico: Usted es un caso NO SOSPECHOSO de Covid-19 y NO pertenece al grupo de riesgo.|")
    print("\t\t\t\t\t\t\t---------------------------------------------------------------------------------------------")

# Notar que en solamente cuando la persona es NO SOSPECHOSO se determina si esta dentro del grupo de riesgo.
# ---------------------------------------------------------------------------------------------------------------------------------
# Fin del programa
