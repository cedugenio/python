#!/usr/bin/python3

class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')
    
class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teias', 'andar pelas paredes')
    
class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')

class HomemAranha(Homem,Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandidos', 'atirar teias entre os prédios')

if __name__ == '__main__': 
    john = Homem()
    print(f'John: {john.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')
    
    parker = HomemAranha()
    print(f'Parker: {parker.capacidades}')
    
    
