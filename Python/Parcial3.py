# El puerto de una ciudad pide un programa para procesar los datos de los barcos que estan siendo cargados
#  en sus muelles. Por cada barco se conoce su patente (una cadena), empresa a la que pertenece, tipo de carga
#  que llevará (un valor del 0 al 14, por ejemplo: 0: Soja, 1: Maiz, 2: Gas Licuado etc.) y la cantidad de dias
#  que estará en puerto. Se desea almacenar la información referida a los n barcos  en un arreglo de registros
# de tipo Barco (definir el tipo Barco  y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:
#
# 1) Cargar el arreglo con los datos de los n barcos. Valide que la cantidad de dias que estará en puerto sea mayor a cero
#    y que el tipo de carga esté en el rango especificado. Puede hacer la carga en forma manual, o puede generar los datos
#    en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
# 2) Mostrar todos los datos de todos barcos, en un listado ordenado de mayor a menor según las patentes de los barcos.
# 3) Determinar la cantidad total de barcos por cada tipo de carga que se carga en el puerto, 15 contadores en total enn un vcetor
#    de conteo.
# 4) Determinar el barco con menor cantidad de días en el puerto entre los barcos cuyo tipo de carga es 0, 1, o 2.
# 5) Determinar si existe un barco cuya empresa propietaria sea igual x y su tipo de carga sea 8, siendo x un valor que se carga
#    por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe mas de un registro que coincida
#    con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.

import random
import transporte


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


def read(barco):

    n = len(barco)
    for i in range(n):
        pat = input('Patente[' + str(i) + ']: ')

        print('Ingrese Nombre de la empresa...')
        emp = input('Empresa[' + str(i) + ']: ')

        print('Ingrese el tipo de carga...')
        car = validate_code(0, 14)

        print('Ingrese el numero de dias que el barco estuvo en el puerto...')
        cant = validate(0)

        barco[i] = transporte.Transporte(pat, emp, car, cant)
        print()


def opcion1(barco):
    print('Cargue los datos de los barcos:')
    read(barco)


def generate(barco):
    letras = ('ABC', 'BCD', 'CDE', 'EFG')
    empresas_navales = (['Hyundai Merchant Marine', 'Pacific International Lines',
                         'Yang Ming Marine Transport Corp', 'Evergreen Marine Corp',
                         'Ocean Network Express (ONE)', 'Hapag-Lloyd', 'COSCO Shipping Co. Ltd',
                         'Grupo CMA CGM', 'Mediterranean Shipping Company', 'A.P. Moller-Maersk Group'])

    n = len(barco)
    for i in range(n):
        p1 = random.choice(letras)
        p2 = str(random.randint(100, 1000))
        pat = p1 + p2

        emp = random.choice(empresas_navales)
        car = random.randint(0, 14)
        cant = random.randint(1, 30)

        barco[i] = transporte.Transporte(pat, emp, car, cant)
    print('Hecho... el arreglo ha sido generado...')


def opcion2(barco):
    print('Se precede a la generacion automatica del arreglo... pulse <Enter>...')
    input()
    generate(barco)


def sort(barco):
    n = len(barco)
    for i in range(n-1):
        for j in range(i+1, n):
            if barco[i].patente > barco[j].patente:
                barco[i], barco[j] = barco[j], barco[i]


def display_all(barco):
    print('Listado completo de barcos:')
    for v in barco:
        print(transporte.to_string(v))


def opcion3(barco):
    if barco[0] is None:
        print('No hay datos cargados en el arreglo...')
        return

    sort(barco)
    display_all(barco)


def opcion4(barco):
    if barco[0] is None:
        print('No hay datos cargados en el arreglo...')
        return
    count(barco)


def count(barco):
    vc = 15 * [0]
    for v in barco:
        d = v.carga
        vc[d] += 1

    print('Cantidad de barcos por tipo de carga:')
    for i in range(15):
        if vc[i] != 0:
            print('Codigo de carga:', i, 'Cantidad de barcos:', vc[i])


def test():
    print('Ingrese la cantidad de barcos a cargar...')
    n = validate(0)

    barco = n * [None]

    opc = 0
    while opc != 5:
        print('\nMenu de opciones:')
        print('1. Cargar barcos en forma manual')
        print('2. Cargar barcos en forma automática')
        print('3. Listado de barcos ordenado por patente (mayor a menor)')
        print('4. Cantidad total de barcos por cada tipo de carga')
        print('5. Salir')

        opc = int(input('Ingrese su eleccion: '))

        if opc == 1:
            opcion1(barco)

        elif opc == 2:
            opcion2(barco)

        elif opc == 3:
            opcion3(barco)

        elif opc == 4:
            opcion4(barco)

        elif opc == 5:
            print("--- Programa finalizado ---")


# script principal...
if __name__ == '__main__':
    test()
