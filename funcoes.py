def nome_funcao():
    print("Olá, esta é a minha função!")

nome_funcao()

def saudacao(nome):
    print("Olá, " + nome + "! Bem-vindo(a) à minha função!")

saudacao("Ivan")

list_numeros = [1, 2, 3, 4, 5]

def lista_numeros_funcao(lista):
    for i in lista:
        print(i*2)

lista_numeros_funcao(list_numeros)


def lista_dobro(lista):
    return[i*2 for i in lista]

print(lista_dobro(list_numeros))