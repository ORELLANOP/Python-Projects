__author__ = 'Datos de tres postulantes a un empleo'

def porcentaje(tp, pbc):
    return pbc * 100 / tp

def nivel(p):
    if p >= 90:
        return "Superior"

    if p >= 75:
        return "Medio"

    if p >= 50:
        return "Regular"

    return "Fuera de nivel"


def test():
   # Titulo general y ciclo de carga de datos
   print("Seleccion de nuevo personal para una empresa")
   for i in range(1, 4):
       # carga de datos de UN postulante
       nom = input("Nombre postulante " + str(i) + ": ")
       tp = int(input("Total de preguntas: "))
       cpbr = int(input("Total de preguntas bien respondidas: "))

       # procesos
       pr = porcentaje(tp, cpbr)

       # procesos y visualizacion de resultados
       print("Nombre", i, ":", nom, "- Nivel:", nivel(pr), "- Porc:", pr, "%")


       # determinacion del aspirante con mayor porcentaje
       if i == 1:
           pmay, nmay = pr, nom
       elif pr > pmay:
           pmay, nmay = pr, nom

   # Visualizacion del ganador del puesto
   if pmay > 50:
       print("Ganador: ", nmay, "-con porcentaje de: ", pmay, "%")
   else:
       print("No hay ganador: todos tienen porcentaje menor a 50%")

# Script principal
test()
