class ArmazenamentoLocal:
    def salvar (self,dado):
        print(f"{dado} : foi salvo localmente")

class ArmazenamentoNuvem:
    def salvar(self, dado):
        print(f"{dado} : foi salvo na nuvem")
        
class GerenciaArmazenamento:
    def __new__(cls, armazenamento):
        return armazenamento
    

meuArmazenamento01 = GerenciaArmazenamento(ArmazenamentoLocal())
meuArmazenamento02 = GerenciaArmazenamento(ArmazenamentoNuvem())

print(meuArmazenamento01)
print(meuArmazenamento02.salvar("papel"))