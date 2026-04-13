class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    # O método precisa estar "dentro" da classe (alinhado com o __init__)
    def apresentar(self):
        print(f"O nome é {self.nome}\n")
        print(f"A idade é: {self.idade}")

# Agora sim, instanciando e chamando
pessoa01 = Pessoa("Ivan", 37)
pessoa01.apresentar()