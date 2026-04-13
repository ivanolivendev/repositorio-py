"""

2. Construtor (__init__)

Crie a classe Carro com:

marca, modelo, ano
inicialize via construtor


"""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def apresentar (self):
        print(f"O carro é da marca {self.marca}, ano: {self.ano}, modelo: {self.modelo}")



carrp01 = Carro("corsa", "gol", 1997)
carrp01.apresentar()