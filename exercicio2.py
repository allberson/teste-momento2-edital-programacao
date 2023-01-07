# exercicio 2
matriz = [
  [0, 0, 0],
  [0, 2, 0],
  [0, 0, 0],
]

for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                matriz[i][j] = i + j 

print(matriz[0])
print(matriz[1])
print(matriz[2])