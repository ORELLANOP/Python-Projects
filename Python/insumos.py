class Insumo:
    def __init__(self, cod=1, nom='', pre=0.0, cant=0):
        self.codigo = cod
        self.nombre = nom
        self.valor = pre
        self.cantidad = cant

def to_string(insumo):
    r = ''
    r += '{:<15}'.format('Codigo: ' + str(insumo.codigo))
    r += '{:<30}'.format('Nombre: ' + insumo.nombre)
    r += '{:<18}'.format('Precio: ' + str(insumo.valor))
    r += '{:<15}'.format('Cantidad: ' + str(insumo.cantidad))
    return r
