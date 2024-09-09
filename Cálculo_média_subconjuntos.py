
# Cálculo de Média de Subconjuntos

lista = [1, 2, 3, 4]

# loop posição numeros dentro da lista
for num in range(len(lista)):

    # loop posição dentro da lista dentro do loop
    for i in range(len(lista)):

        # regra para não repetir pares
        if lista[i] >= lista[num]:
            sub = [lista[num], lista[i]]
            print(sub)

            # calculo da media
            media = (sub[0] + sub[1])/len(sub)
            print("media: ", media)