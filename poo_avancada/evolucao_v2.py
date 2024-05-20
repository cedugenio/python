#!/usr/bin/python3

class Humano(object):
    especie = 'Homo Sapiens'
    
    def __init__(self ,nome):
        self.nome = nome 
    
    def das_cavernas(self):
        self.especie = 'Homo Nearderthalensis'

if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn')
    grokn.das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')

    Humano.especie = 'Homo Sapiens Sapiens'
    print('Especies\n')
    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')