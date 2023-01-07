import numpy as np

qtd_matriz = 2
cont_matriz = 0

matrizA = np.zeros((3,2))
matrizB = np.zeros((3,2))
matrizC = np.zeros((3,2))

i = 0
linhas = 3

colunas = 2


print("Matriz a")
while i < linhas:
    j = 0
    while j < colunas:
        print("Insira o", "[",str(i),"]","[",str(j),"]","número:")
        numero = int(input())
        matrizA[i][j] = numero 
        j+=1
    i+=1

i = 0  

print("Matriz b")
while i < linhas:
    j = 0
    while j < colunas:
        print("Insira o", "[",str(i),"]","[",str(j),"]","número:")
        numero = int(input())
        matrizB[i][j] = numero 
        j+=1
    i+=1

    
for i in range(len(matrizC)):
        for j in range(len(matrizC[i])):
                matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

print("Matriz A")
print(matrizA)
print("Matriz A")
print(matrizB)
print("Matriz C")
print(matrizC)

