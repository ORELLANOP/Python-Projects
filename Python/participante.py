class Participante:
    def __init__(self, nom, cont, rank, prom, punt):
        self.nombre = nom
        self.continente = cont
        self.ranking = rank
        self.promedio = prom
        self.puntaje = punt


def to_string(participante):
    r = ''
    r += '{:<20}'.format('Nombre: ' + participante.nombre)
    r += '{:<20}'.format('Continente: ' + str(participante.continente))
    r += '{:<25}'.format('Ranking Mundial: ' + str(participante.ranking))
    r += '{:<20}'.format('Promedio: ' + str(participante.promedio))
    r += '{:<20}'.format('Puntaje: ' + str(participante.puntaje))

    return r
