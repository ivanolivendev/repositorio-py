"""

Crie uma classe Conta com:

atributo _saldo (privado por convenção)
método para consultar saldo

"""

class Conta:

    def __init__(self, saldo_inicial):
        
        self.saldo_inicial = saldo_inicial
        self.__saldo = saldo_inicial

    def mostraSaldo (self):
        print(f"O saldo é de {self.__saldo}")        

        
contaIvan = Conta(100)
contaIvan.mostraSaldo()