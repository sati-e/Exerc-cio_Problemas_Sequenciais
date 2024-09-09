
# busca em lista de numeros

lista = [2, 5, 6, 1, 0, 7]

# alvo determinado
alvo = 0

print("alvo: ", alvo)
print('lista: ', lista)

# loop em busca do numero
for num in range(0, len(lista)):
    # se o numero da lista for igual ao alvo
    if lista[num] == alvo:
        print("posição do número alvo: ", num)

