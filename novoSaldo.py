"""
Getter e Setter
Crie métodos get_saldo() e set_saldo()
Impedir saldo negativo

"""

class Saldo:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial


    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor>0:
            self.__saldo+=valor
        print(f"Saldo atualziado para {self.__saldo}")
        


conta01 = Saldo(100)
conta01.set_saldo(100)
