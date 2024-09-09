
# Contagem de Caracteres em Palavras

lista = ['banana', 'peixe', 'violino']

# loop cada posição = palavra da lista
for palavra in range(len(lista)):
    soma = 0
    # loop conta numero da posição de cada letra da palavra
    for n in lista[palavra]:
        soma += 1
    print(soma)

