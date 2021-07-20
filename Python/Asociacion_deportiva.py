import socios


def validate(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def validate_code(mn=0, mx=9):
    cod = int(input('Ingrese codigo (>= ' + str(mn) + ' y <= ' + str(mx) + '): '))
    while cod < mn or cod > mx:
        cod = int(input('Se pidio >='+str(mn)+' y <='+str(mx)+'). De nuevo: '))
    return cod


def read(club):
    n = len(club)
    for i in range(n):
        nom = input('Nombre[' + str(i) + ']: ')
        print('Ingrese numero de socio...')

        num = validate(0)
        print('Ingrese arancel...')

        ara = validate(0)
        print('Ingrese código de deporte...')

        cod = validate_code(0, 9)
        club[i] = socios.Socio(num, nom, ara, cod)
        print()


def opcion1(club):
    print('Cargue los datos de los socios del club:')
    read(club)


def display(club, p):
    print('Listado de socios que pagan arancel mayor a', p, ':')
    for socio in club:
        if socio.arancel > p:
            print(socios.to_string(socio))


def opcion2(club):
    if club[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    print('Ingrese arancel para cotrolar...')
    p = validate(0)
    display(club, p)


def count(club):
    vc = 10 * [0]
    for socio in club:
        d = socio.codigo
        vc[d] += 1

    print('Cantidad de socios en cada deporte deporte disponible:')
    for i in range(10):
        if vc[i] != 0:
            print('Codigo de deporte:', i, 'Cantidad de socios:', vc[i])


def opcion3(club):
    if club[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    count(club)


def sort(club):
    n = len(club)
    for i in range(n-1):
        for j in range(i+1, n):
            if club[i].numero > club[j].numero:
                club[i], club[j] = club[j], club[i]


def display_all(club):
    print('Listado completo de socios del club:')
    for socio in club:
        print(socios.to_string(socio))


def opcion4(club):
    if club[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    sort(club)
    display_all(club)


def search(club, nom):
    for socio in club:
        if socio.nombre == nom:
            return socio
    return None


def opcion5(club):
    if club[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    nom = input('Ingrese el nombre del socio a buscar: ')
    socio = search(club, nom)

    if socio is not None:
        socio.arancel += 100
        print('Socio encontrado... se incremento en $100 su arancel...')
        print('Datos modificados del socio:')
        print(socios.to_string(socio))
    else:
        print('No existe un socio registrado con ese nombre')


def test():
    # cargar cantidad de socios...
    print('Ingrese la cantidad de socios del club...')
    n = validate(0)

    # crear el arreglo (inicialmente vacio)...
    club = n * [None]
    opc = 0

    while opc != 6:
        print('\nMenu de opciones:')
        print('1. Cargar socios')
        print('2. Mostrar socios que pagan arancel mayor a p')
        print('3. Conteo de socios por cada deporte')
        print('4. Listado ordenado de socios')
        print('5. Buscar socio y ajustar su arancel')
        print('6. Salir')

        opc = int(input('Ingrese su eleccion: '))

        if opc == 1:
            opcion1(club)

        elif opc == 2:
            opcion2(club)

        elif opc == 3:
            opcion3(club)

        elif opc == 4:
            opcion4(club)

        elif opc == 5:
            opcion5(club)

        elif opc == 6:
            print("--- Programa finalizado ---")


# script principal...
if __name__ == '__main__':
    test()
