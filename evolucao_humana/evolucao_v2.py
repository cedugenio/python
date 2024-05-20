#!/usr/bin/python3

class EvolucaoHumana(object):
    especie = ''

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Nearderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)
    
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]
    
    def __init__(self ,nome):
        self.nome = nome 
    
class Neanderthal(EvolucaoHumana):
    especie =  EvolucaoHumana.especies()[-2]

class HomoSapiens(EvolucaoHumana):
    especie =  EvolucaoHumana.especies()[-1]

if __name__ == '__main__':
    jose = EvolucaoHumana('José')
    grokn = EvolucaoHumana('Grokn')

    print(f'Evolução (a partir da classe): {",".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {",".join(jose.especies())}')

    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
    print(f'José evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluido? {grokn.is_evoluido()}')