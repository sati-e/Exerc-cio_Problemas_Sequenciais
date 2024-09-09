
# matriz transposta

m1 = [[1, 2], [3, 4], [2, 0]]

# inedx linhas e colunas
num_linha = len(m1)
num_coluna = len(m1[0])

# lista matriz transposta vazia
m1_transp = [[] for _ in range(num_coluna)]
print(m1_transp)

# posição linha e coluna
for i in range(num_linha):
    for j in range(num_coluna):

        # adociona os valores a matriz transposta
        m1_transp[j].append(m1[i][j]) 
        
# print matriz
for linha in m1_transp:
    print(linha)