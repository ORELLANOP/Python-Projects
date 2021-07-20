import random
import participante



def validate(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio > ' + str(inf) + '... Cargue de nuevo: '))
    return n


def validate_code(mn=0, mx=15):
    cod = int(input('Ingrese codigo (>= ' + str(mn) + ' y <= ' + str(mx) + '): '))
    while cod < mn or cod > mx:
        cod = int(input('Se pidio >= '+str(mn)+' y <= '+str(mx)+')... De nuevo: '))
    return cod


def read(pais):
    n = len(pais)
    for i in range(n):
        nom = input('Nombre[' + str(i) + ']: ')

        print('Ingrese Continente...')
        cont = validate(0)

        print('Ingrese numero de Ranking...')
        rank = validate_code(0, 15)

        punt = 0
        prom = 0

        pais[i] = participante.Participante(nom, cont, rank, punt, prom)
        print()


def opcion1(pais):
    print('Cargue los datos de los participantes:')
    read(pais)


def generate(pais, pais1):
    jugadores = (['Argentina', 'Brasil', 'Colombia', 'Ecuador', 'Chile', 'Uruguay', 'Cuba',
                  'EEUU', 'Canada', 'Peru', 'Bolivia', 'Inglaterra', 'Francia', 'Alemania',
                  'Japon', 'China', 'Mexico', 'Grecia', 'España', 'Portugal', 'Australia',
                  'Iran', 'Corea', 'Dinamarca', 'Turquia', 'Polonia', 'Suecia', 'Sudafica',
                  'Croacia', 'Serbia', 'Rusia', 'Islandia', 'Ghana', 'Nigeria', 'Italia'])

    n = len(pais)

    for i in range(n):

        nom = random.choice(jugadores)
        cont = random.randint(0, 4)
        rank = random.randint(1, 16)
        punt = 0
        prom = 0

        pais[i] = participante.Participante(nom, cont, rank, punt, prom)
        pais1[i] = participante.Participante(nom, cont, rank, punt, prom)
        print('El numero de ranking es: ', pais[i].ranking)
        print('El nombre del equipo es: ', pais[i].nombre)
        j = 0
        j2 = 0

        norepe = True

        while norepe:
            # print("ingreso al ciclo")
            if i > 0:
                while j < i:

                    if pais[i].ranking == pais[j].ranking:
                        print("Numero igual")
                        pais[i].ranking = random.randint(1, 16)
                        print("Numero cambiado, el nuevo numero es: ", pais[i].ranking)
                        pais1[i].ranking = pais[i].ranking
                        cambio = True

                    else:
                        norepe = False
                        print("Numero distinto")
                        cambio = False

                    if cambio:
                        j = 0
                    else:
                        j += 1
            else:
                norepe = False
                print("Primer numero")

        norepe2 = True

        while norepe2:
            print("ingreso al ciclo")
            if i > 0:
                while j2 < i:

                    if pais[i].nombre == pais[j2].nombre:
                        print("Nombre igual")
                        pais[i].nombre = random.choice(jugadores)
                        print("Nombre cambiado, el nuevo nombre es: ", pais[i].nombre)
                        pais1[i].nombre = pais[i].nombre
                        cambio2 = True
                    else:
                        norepe2 = False
                        print("Nombre distinto")
                        cambio2 = False

                    if cambio2:
                        j2 = 0
                    else:
                        j2 += 1
            else:
                norepe2 = False
                print("Primer nombre")

    print('Hecho... el arreglo ha sido generado...')


def opcion2(pais, pais1):
    print('Se precede a la generacion automatica de los equipos... pulse <Enter>...')
    input()
    generate(pais, pais1)


def sort(pais):
    n = len(pais)
    for i in range(n-1):
        for j in range(i+1, n):
            if pais[i].ranking > pais[j].ranking:
                pais[i], pais[j] = pais[j], pais[i]


def sort2(pais):
    n = len(pais)
    for i in range(n-1):
        for j in range(i+1, n):
            if pais[i].puntaje < pais[j].puntaje:
                pais[i], pais[j] = pais[j], pais[i]


def match(pais, contador):
    n = len(pais)
    mitad = n // 2
    contador += 1

    if contador == 1:
        print("\n\nOctavos de Final de la copa")
        sort(pais)
        pais = enfrentamiento(pais, n, mitad, contador)
        pais = pais[0:mitad]
        sort2(pais)
        display_all(pais)

    elif contador == 2:
        print("\n\nCuartos de Final de la copa")
        sort2(pais)
        pais = enfrentamiento(pais, n, mitad, contador)
        pais = pais[0:mitad]
        sort2(pais)
        display_all(pais)

    elif contador == 3:
        print("\n\nSemifinal de la copa")
        sort2(pais)
        pais = enfrentamiento(pais, n, mitad, contador)
        # pais = pais[mitad:4]
        # print("Los paises que jugaran el 3er y 4to puesto son: ")
        # display_all(pais)
        # pais = pais[0:mitad]
        print('\n\nLos equipos que jugaran la final son:  ' + pais[0].nombre, 'vs ' + pais[1].nombre)
        print('\n\nLos equipos que jugaran 3er y 4to puesto son:  ' + pais[2].nombre, 'vs ' + pais[3].nombre)
        display_all(pais)
        pais[3], pais[1] = pais[1], pais[3]
        display_all(pais)

    elif contador == 4:
        print("\n\nFinal de la copa")
        # pais[3], pais[1] = pais[1], pais[3]
        pais = enfrentamiento(pais, n, mitad, contador)
        print("\n\n#####     GANADOR:", pais[0].nombre)
        print("\n\n#####     Segundo puesto:", pais[3].nombre)
        print("\n\n#####     Tercer puesto:", pais[1].nombre)
        # display_all(pais)
        pais[1], pais[2] = pais[2], pais[1]
        pais[3], pais[1] = pais[1], pais[3]
        # display_all(pais)
        pais = pais[0:3]
        # sort2(pais)
        display_all(pais)

    elif contador > 4:
        print("\n\nEl torneo finalizo, si desea jugar otro Mundial seleccione la opcion 8 del Menu")

    return pais, contador


def enfrentamiento(pais, n, mitad, contador):

    for i in range(mitad):

        print('\n\nSe enfrentan los equipos:  ' + pais[i].nombre, 'vs ' + pais[n-1-i].nombre)

        eq1 = random.randint(20, 100)
        print('El equipo:  ' + pais[i].nombre, 'obtuvo: '+str(eq1), 'puntos')

        eq2 = random.randint(20, 100)
        print('El equipo:  ' + pais[n-1-i].nombre, 'obtuvo: '+str(eq2), 'puntos')

        if eq1 > eq2:
            print('El equipo  ' + pais[i].nombre, '  pasa de ronda')
            pais[i].puntaje = eq1
            print("El puntaje es entonces :", pais[i].puntaje)
            pais[i].promedio += eq1
            print("y la acumulacion es entonces :", pais[i].promedio)
            variable = pais[i].promedio / contador
            print("y el promedio :", variable)

        else:
            print('El equipo  ' + pais[n-1-i].nombre, '  pasa de ronda')
            pais[i], pais[n-1-i] = pais[n-1-i], pais[i]
            pais[i].puntaje = eq2
            print("El puntaje es entonces :", pais[i].puntaje)
            pais[i].promedio += eq2
            print("y la acumulacion es entonces :", pais[i].promedio)
            variable = pais[i].promedio / contador
            print("y el promedio :", variable)

    return pais


def display_all(pais):
    print('\n\nListado completo de equipos son:')
    for v in pais:
        print(participante.to_string(v))


def opcion3(pais, pais1):
    if pais[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    sort(pais)
    display_all(pais)

    sort(pais1)
    display_all(pais1)


def count(pais):
    vc = 10 * [0]
    for v in pais:
        d = v.continente
        vc[d] += 1

    print('Cantidad de participantes en cada continente:')
    for i in range(10):
        if vc[i] != 0:
            print('Codigo de continente:', i, 'Cantidad de participantes:', vc[i])


def opcion4(pais):
    if pais[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    count(pais)


def opcion5(pais, contador):
    if pais[0] is None:
        print('No hay datos cargados en el arreglo...')
        return pais, contador

    pais, contador = match(pais, contador)
    return pais, contador


def opcion6(pais1):
    if pais1[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    sort(pais1)
    display_all(pais1)


def search(pais1, nom1, nom2, nom3):
    c = 0
    for v in pais1:
        if v.nombre == nom1:
            c += 1
            v.ranking += 25

        elif v.nombre == nom2:
            c += 1
            v.ranking += 15

        elif v.nombre == nom3:
            c += 1
            v.ranking += 5

    if c == 3:
        print('Se le aumentaron los rankings a los paises del podio')
        display_all(pais1)
    else:
        print('No se encontro alguno de los 3 paises')


def opcion7(pais1, pais):
    if pais1[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    nom1 = pais[0].nombre
    nom2 = pais[1].nombre
    nom3 = pais[2].nombre

    search(pais1, nom1, nom2, nom3)


def test():

    print('Ingrese los 16 de equipos que participarán en el Mundial de fútbol:')

    n = 16
    pais = n * [None]
    pais1 = n * [None]
    contador = 0

    opc = 0
    while opc != 9:
        print('\nMenu de opciones:')
        print('1. Cargar los 16 equipos en forma manual')
        print('2. Cargar los 16 equipos en forma automática')
        print('3. Listado de equipos ordenados por ranking y cantidad de participantes por continente')
        print('4. Cantidad de participantes por continente')
        print('5. Avanzar a la siguiente fase del Mundial')
        print('6. Observar la fase 1 nuevamente')
        print('7. Buscar los paises del podio y sumarle pts al ranking')
        print('8. Resetear')
        print('9. Salir')

        opc = int(input('\nIngrese su eleccion: '))

        if opc == 1:
            opcion1(pais)

        elif opc == 2:
            opcion2(pais, pais1)

        elif opc == 3:
            opcion3(pais, pais1)

        elif opc == 4:
            opcion4(pais)

        elif opc == 5:
            pais, contador = opcion5(pais, contador)

        elif opc == 6:
            opcion6(pais1)

        elif opc == 7:
            opcion7(pais1, pais)

        elif opc == 8:
            print('Mundial de fútbol:')
            n = 16
            pais = n * [None]
            pais1 = n * [None]
            contador = 0

        elif opc == 9:
            print("--- Programa finalizado ---")


# script principal...
if __name__ == '__main__':
    test()
