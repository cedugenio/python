#!/usr/bin/python3 
from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome}"-"{self.idade}'

    def isAdulto():
        pass

class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

class Cliente(Pessoa):
    compras = []
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def registrar_compra(compra):
        pass

    def get_data_ultima_compra():
        pass

    def total_compras():
        pass

class Compra():
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = datetime.now()
        self.valor = valor

def main():
    pass 

if __name__ == '__main__':
    main()


        