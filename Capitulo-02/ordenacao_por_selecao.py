 # Encontra o menor valor em uma matriz
def buscaMenor(arr):
  # Armazena o menor valor
  menor = arr[0]
  # Armazena o índice do valor menor
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor_indice = i
      menor = arr[i]      
  return menor_indice

# Classificar matriz
def ordenacaoPorSelecao(arr):
  novoArr = []
  for i in range(len(arr)):
      # Encontra o menor elemento na matriz e adiciona-o à nova matriz
      menor = buscaMenor(arr)
      novoArr.append(arr.pop(menor))
  return novoArr

print(ordenacaoPorSelecao([235, 325, 243, 32, 4, 5]))