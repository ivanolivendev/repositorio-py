class Exemplo:

    def __new__(cls, *args, **k):
        objeto = super().__new__(cls)
        print("Objeto criado com Sucesso")
        return objeto
    

    def __init__(self, nome):
        self.nome = nome
        print("O objeto criado anteriormente foi personalizado")


exemplo01 = Exemplo("Ivan")
print (exemplo01.nome)