pessoas = [
    {"nome": "Ana", "cidade": "SP"},
    {"nome": "João", "cidade": "RJ"},
    {"nome": "Maria", "cidade": "SP"}
]

cidades = {}
pessoaCidade=[]

for pessoa in pessoas:  
    if pessoa["cidade"] == "SP":
        cidades["SP"] = pessoaCidade.append(pessoa["nome"])


print(cidades)