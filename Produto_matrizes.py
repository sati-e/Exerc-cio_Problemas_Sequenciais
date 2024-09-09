
# produto matrizes

m1 = [[1, 0],
      [3, 4]]

m2 = [[0,1],
      [2,1]]

m3 = [[0, 0],
      [0, 0]]

# loop contador da linha
for l in range(0,2):
      print("1: ", l)
      # loop contador da coluna
      for c in range(0,2):
            print("2: ", c)
            # armazena os índices da coluna da matriz m1 e o
            # índice da linha da matriz m2
            for valores in range(0,2):
                  print('3: ', valores)
                  m3[l][c] += m1[l][valores] * m2[valores][c]
print(m3)

