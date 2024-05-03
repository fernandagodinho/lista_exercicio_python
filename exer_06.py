# Desafio 6: Busca binária
# Escreva um programa que implemente o algoritmo de busca binária.
# Crie uma lista ordenada de números.
# Peça ao usuário para digitar um número a ser buscado na lista.
# Utilize o algoritmo de busca binária para encontrar o número na lista e 
# imprima o resultado na tela.

def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

# Cria uma lista ordenada de números
lista = [1, 3, 5, 7, 9]

# Pede ao usuário para digitar um número a ser buscado na lista
item = int(input("Digite um número a ser buscado na lista: "))

# Utiliza o algoritmo de busca binária para encontrar o número na lista
resultado = busca_binaria(lista, item)

# Imprime o resultado na tela
if resultado != None:
    print(f"O número {item} foi encontrado na posição {resultado} da lista.")
else:
    print(f"O número {item} não foi encontrado na lista.")
