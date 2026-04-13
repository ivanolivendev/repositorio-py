
"""nome_aluna={'nome': 'Ivan', 'sobrenome': 'Cavalcante', 'idade': 37, 'cidade': 'Belem'}

for chave,valor in nome_aluna.items():
    print(chave + ": " + str(valor))

dados ={"nome":"Ivan", "idade":37}

print(dados['idade'])

novoDado = {}
novoDado.update({"idade": 38})
novoDado.pop("idade")
del dados['idade']

if "email" in dados:
    print("Email existe no dicionário.")
else:
    print("Email não existe no dicionário.")

    if "Ivan" in dados.values():
        print("Ivan existe no dicionário.")

pessoa = {"nome": "Ivan", "idade": 30, "cidade": "Belém"}


for valor in pessoa.values():
    print(valor)    

total = 0
notas = {"mat": 8, "port": 7, "bio": 9}


for valor in notas.values():
    total += valor
    
print("A média é "+str(total/len(notas)))
"""

texto = "python python java python c java"
palavras = texto.split()  # Transforma em ['python', 'python', 'java', ...]

contagem = {}

for p in palavras:
    print(p)

