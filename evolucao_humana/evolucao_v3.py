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

    def get_idade(self):
        return self._idade
    
    def set_idade(self, idade):
        if idade <= 0:
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade
    
class Neanderthal(EvolucaoHumana):
    especie = EvolucaoHumana.especies()[-2]

class HomoSapiens(EvolucaoHumana):
    especie = EvolucaoHumana.especies()[-1]

if __name__ == '__main__':
    jose = HomoSapiens("José")
    jose.set_idade(40)
    print(f'Nome: {jose.nome} Idade: {jose.get_idade()}')
