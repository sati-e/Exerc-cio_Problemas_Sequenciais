
# verificação de primos em uma lista

lista = [2, 27, 10, 6, 3]

# loop numeros da lista
for num in lista:

    # se o número não for 0 ele verifica se é primo ou não
    if num != 0:
        # loop verificação se é divisível pelos números anteriores ao atual
        # maiores que 1 e menores que o num atual
        for i in range(2, num):
            # se for divisível por algum desses números ele é primo
            if (num % i) == 0:
                print(num, 'não é primo')
                break
        # se a verificação não deu resultado ele vem para esse else e mostra
        # que não é primo
        else:
            print(num, "é primo")
    # mostra se o número for 0
    else:
        print("0")