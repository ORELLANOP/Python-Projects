class Socio:
    def __init__(self, num, nom='', ara=0.0, cod=0):
        self.numero = num
        self.nombre = nom
        self.arancel = ara
        self.codigo = cod


def to_string(socio):
    r = ''
    r += '{:<15}'.format('Numero: ' + str(socio.numero))
    r += '{:<30}'.format('Nombre: ' + socio.nombre)
    r += '{:<18}'.format('Arancel: ' + str(socio.arancel))
    r += '{:<15}'.format('Codigo: ' + str(socio.codigo))
    return r
