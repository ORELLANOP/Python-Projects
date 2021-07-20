class Transporte:
    def __init__(self, pat, emp, car, cant):
        self.patente = pat
        self.empresa = emp
        self.carga = car
        self.dias = cant


def to_string(transporte):
    r = ''
    r += '{:<20}'.format('Patente: ' + transporte.patente)
    r += '{:<20}'.format('Tipo de carga: ' + str(transporte.carga))
    r += '{:<25}'.format('Cantidad de dias: ' + str(transporte.dias))
    r += '{:<20}'.format('Empresa: ' + transporte.empresa)


    return r
