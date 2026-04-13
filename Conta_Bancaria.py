
class ContaBancaria :
    def __init__(self,cpf,saldo):
        self.cpf = cpf
        self.saldo = saldo

    def depositar(self,valor):
       
        self.saldo = self.saldo + valor
        return self.saldo
    

contaIvan = ContaBancaria("00453683258", 100)
print(contaIvan.depositar(100))
