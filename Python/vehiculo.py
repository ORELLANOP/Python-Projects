class Vehiculo:
    def __init__(self, pat, tip, cab, imp=0.0):
        self.patente = pat
        self.tipo = tip
        self.cabina = cab
        self.importe = imp


def to_string(vehiculo):
    r = ''
    r += '{:<20}'.format('Patente: ' + vehiculo.patente)
    r += '{:<20}'.format('Tipo: ' + str(vehiculo.tipo))
    r += '{:<20}'.format('Cabina: ' + str(vehiculo.cabina))
    r += '{:<20}'.format('Importe: ' + str(vehiculo.importe))

    return r
