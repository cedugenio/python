#!/usr/bin/python3

class ClasseSimples:
    contador = 0

    def __init__(self) -> None:
        self.contar()
    
    @classmethod
    def contar(cls):
        cls.contador += 1
    

if __name__ ==  '__main__':
    lista = [ClasseSimples(),ClasseSimples(),ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)
