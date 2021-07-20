import insumos


def validate(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio > ' + str(inf) + '... Cargue de nuevo: '))
    return n


def validate_code(mn=1, mx=20):
    cod = int(input('Ingrese codigo (>= ' + str(mn) + ' y <= ' + str(mx) + '): '))
    while cod < mn or cod > mx:
        cod = int(input('Error... era >='+str(mn)+' y <='+str(mx)+'). De nuevo: '))
    return cod


def read(pieza):
    n = len(pieza)
    for i in range(n):
        nom = input('Nombre[' + str(i) + ']: ')
        cod = validate_code(1, 20)
        val = int(input('Precio: '))
        can = int(input('Cantidad: '))
        pieza[i] = insumos.Insumo(cod, nom, val, can)
        print()


def opcion1(pieza):
    print('Cargue los datos de los insumos de la pieza:')
    read(pieza)


def display_all(pieza):
    for insumo in pieza:
        print(insumos.to_string(insumo))


def opcion2(pieza):
    if pieza[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    print('Listado completo de insumos para la pieza')
    display_all(pieza)


def total_value(pieza):
    tv = 0
    for insumo in pieza:
        monto = insumo.valor * insumo.cantidad
        tv += monto
    return tv


def opcion3(pieza):
    if pieza[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    print('Monto total en insumos para la pieza:', total_value(pieza))


def sort(pieza):
    n = len(pieza)
    for i in range(n-1):
        for j in range(i+1, n):
            if pieza[i].codigo > pieza[j].codigo:
                pieza[i], pieza[j] = pieza[j], pieza[i]


def display(pieza, x):
    print('Insumos con menos de', x, 'unidades en esta pieza: ')
    for insumo in pieza:
        if insumo.cantidad < x:
            print(insumos.to_string(insumo))


def opcion4(pieza):
    if pieza[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    x = int(input('Cantidad x de unidades a controlar: '))
    sort(pieza)
    display(pieza, x)


def change_quantity(pieza, c):
    exists = False
    print('Insumos que pasaron de 0 unidades a', c, 'unidades en esta pieza: ')
    for insumo in pieza:
        if insumo.cantidad == 0:
            exists = True
            insumo.cantidad = c
            print(insumos.to_string(insumo))
    if not exists:
        print('No hay insumos con 0 unidades en esta pieza')


def opcion5(pieza):
    if pieza[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    print('Ingrese la nueva cantidad c para los insumos sin unidades...')
    c = validate(0)
    change_quantity(pieza, c)


def search(pieza, cod):
    for insumo in pieza:
        if insumo.codigo == cod:
            return insumo
    return None


def opcion6(pieza):
    if pieza[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    print('Ingrese el codigo del insumo a buscar...')
    cod = validate_code(1, 20)
    ins = search(pieza, cod)
    if ins is not None:
        print(insumos.to_string(ins))
    else:
        print('No existe un insumo con ese codigo en la pieza')


def test():
    # cargar cantidad de insumos...
    print('Ingrese la cantidad de insumos en la pieza...')
    n = validate(0)

    # crear el arreglo (inicialmente vacio)...
    pieza = n * [None]

    opc = 0
    while opc != 7:
        print('\nMenu de opciones:')
        print('1. Cargar insumos de la pieza')
        print('2. Mostrar todos los insumos de la pieza')
        print('3. Mostrar el valor total de la pieza')
        print('4. Mostrar insumos con menos de x unidades')
        print('5. Cambiar cantidad en insumos con 0 unidades')
        print('6. Buscar un insumo por su codigo')
        print('7. Salir')

        opc = int(input('Ingrese su eleccion: '))

        if opc == 1:
            opcion1(pieza)

        elif opc == 2:
            opcion2(pieza)

        elif opc == 3:
            opcion3(pieza)

        elif opc == 4:
            opcion4(pieza)

        elif opc == 5:
            opcion5(pieza)

        elif opc == 6:
            opcion6(pieza)

        elif opc == 7:
            print("--- Programa finalizado ---")


# script principal...
if __name__ == '__main__':
    test()
