def contagem_regressiva(i):
  # Caso base
  if i <= 0:
    return 0
  # Caso recursivo
  else:
    print(i)
    return contagem_regressiva(i-1)

contagem_regressiva(10)