#!/usr/bin/python3

class Humano(object):
    especie = 'Homo Sapiens'
    
    def __init__(self ,nome):
        self.nome = nome 
        self._idade = None
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser maior que 0')
        self._idade = idade
       
    def das_cavernas(self):
        self.especie = 'Homo Nearderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Nearderthalensis', 'Sapiens')
        return ('Astrelopitecus',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]
    
if __name__ == '__main__':
    jose =  HomoSapiens('José')
    jose.idade = 40

    print(f'Nome: {jose.nome} Idade: {jose.idade}')
