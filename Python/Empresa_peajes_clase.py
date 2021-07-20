import random
import vehiculo


def validate(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio > ' + str(inf) + '... Cargue de nuevo: '))
    return n


def validate_code(mn=0, mx=14):
    cod = int(input('Ingrese codigo (>= ' + str(mn) + ' y <= ' + str(mx) + '): '))
    while cod < mn or cod > mx:
        cod = int(input('Se pidio >= '+str(mn)+' y <= '+str(mx)+')... De nuevo: '))
    return cod


def read(peaje):
    n = len(peaje)
    for i in range(n):
        pat = input('Patente[' + str(i) + ']: ')

        print('Ingrese tipo de vehiculo...')
        tip = validate(0)

        print('Ingrese numero de cabina...')
        cab = validate_code(0, 14)

        print('Ingrese importe pagado...')
        imp = validate(-1)

        peaje[i] = vehiculo.Vehiculo(pat, tip, cab, imp)
        print()


def opcion1(peaje):
    print('Cargue los datos de los vehiculos:')
    read(peaje)


def generate(peaje):
    letras = ('ABC', 'BCD', 'CDE', 'EFG')

    n = len(peaje)
    for i in range(n):
        p1 = random.choice(letras)
        p2 = str(random.randint(100, 1000))
        pat = p1 + p2

        tip = random.randint(1, 20)
        cab = random.randint(0, 14)
        imp = random.randint(0, 50)
        peaje[i] = vehiculo.Vehiculo(pat, tip, cab, imp)
    print('Hecho... el arreglo ha sido generado...')


def opcion2(peaje):
    print('Se precede a la generacion automatica del arreglo... pulse <Enter>...')
    input()
    generate(peaje)


def sort(peaje):
    n = len(peaje)
    for i in range(n-1):
        for j in range(i+1, n):
            if peaje[i].patente > peaje[j].patente:
                peaje[i], peaje[j] = peaje[j], peaje[i]


def display_all(peaje):
    print('Listado completo de socios del peaje:')
    for v in peaje:
        print(vehiculo.to_string(v))


def opcion3(peaje):
    if peaje[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    sort(peaje)
    display_all(peaje)


def display(peaje, x):
    exists = False
    print('Listado de vehiculos que pasaron por la cabina', x, 'sin pagar peaje:')
    for v in peaje:
        if v.importe == 0 and v.cabina == x:
            exists = True
            print(vehiculo.to_string(v))
    if not exists:
        print('No hay vehiculos que hayan pasado sin pagar por esa cabina')


def opcion4(peaje):
    if peaje[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    print('Ingrese numero de cabina para cotrolar...')
    x = validate_code(0, 14)
    display(peaje, x)


def count(peaje):
    vc = 15 * [0]
    va = 15 * [0]
    for v in peaje:
        d = v.cabina
        vc[d] += 1
        va[d] += v.importe

    print('Cantidad de vehiculos e importe acumulado por cada cabina:')
    for i in range(15):
        if vc[i] != 0:
            print('Cabina:', '{:<4}'.format(str(i)), end='')
            print('Cantidad de vehiculos:', '{:<6}'.format(str(vc[i])), end='')
            print('Total recaudado:', '{:<10}'.format(str(va[i])))


def opcion5(peaje):
    if peaje[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    count(peaje)


def search(peaje, pat):
    c = 0
    for v in peaje:
        if v.patente == pat:
            c += 1
            print(vehiculo.to_string(v))
    if c != 0:
        print('Cantidad de pasos registrados para ese vehiculo:', c)
    else:
        print('No esta registrado ese vehiculo')


def opcion6(peaje):
    if peaje[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    pat = input('Ingrese la patente a buscar: ')
    search(peaje, pat)


def test():
    print('Ingrese la cantidad de vehiculos a cargar...')
    n = validate(0)

    peaje = n * [None]

    opc = 0
    while opc != 7:
        print('\nMenu de opciones:')
        print('1. Cargar vehiculos en forma manual')
        print('2. Cargar vehiculos en forma automática')
        print('3. Listado de veiculos ordenado por patente')
        print('4. Vehiculos que pasaron por cabina x sin pagar peaje')
        print('5. Conteo de vehiculos e importe acumulado (por cabina)')
        print('6. Listado de todos los pasos de un vehiculo')
        print('7. Salir')

        opc = int(input('Ingrese su eleccion: '))

        if opc == 1:
            opcion1(peaje)

        elif opc == 2:
            opcion2(peaje)

        elif opc == 3:
            opcion3(peaje)

        elif opc == 4:
            opcion4(peaje)

        elif opc == 5:
            opcion5(peaje)

        elif opc == 6:
            opcion6(peaje)

        elif opc == 7:
            print("--- Programa finalizado ---")


# script principal...
if __name__ == '__main__':
    test()
