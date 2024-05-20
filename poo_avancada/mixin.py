#!/usr/bin/python3

class HtmlToStringMixin:
    def __str__(self) :
        #Conversao para HTML 
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<spam>{html}</spam>'

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome
    
class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome 
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''
    

class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass

class AnimalHtml(HtmlToStringMixin, Animal):
    pass

if __name__ == '__main__':
    p1 = Pessoa('Ana Beatriz')
    print (p1)

    p2 = PessoaHtml('Lucas Eugenio')
    print (p2)

    a1 = Animal('Beethoven')
    print(a1)

    a2 = AnimalHtml('Pelinho')
    print(a2)    
