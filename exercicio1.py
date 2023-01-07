# exercicio 1
array = []
qtd_item = 6
x = 0

def menorNumero (array):
  menor = array[0]
  for i in array:
      if i < menor:
          menor = i
  return print("Menor número: ",menor, ", Posicao: ",array.index(menor))

def maiorNumero (array):
  maior = array[0]
  for i in array:
      if i > maior:
          maior = i
  return print("Maior número: ",maior, ", Posicao: ",array.index(maior))
      

while x < qtd_item:
  print("Insira o "+str(x+1)+" número:",)
  numero = int(input())
  array.append(numero)
  x = x+1

print("Lista: ", array)
menorNumero(array)
maiorNumero(array)

array.sort()
print("Lista crescente: ",  array)
