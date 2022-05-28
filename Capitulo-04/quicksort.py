def quicksort(array):
  if len(array) < 2:
    # caso base, matrizes com 0 ou 1 elemento já estão "classificadas"
    return array
  else:
    # Caso recursivo
    pivo = array[0]
    # submatriz de todos os elementos menores que o pivo
    menores = [i for i in array[1:] if i <= pivo]
    # submatriz de todos os elementos maiores que o pivo
    maiores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))