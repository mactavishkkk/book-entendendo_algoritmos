class pesquisaBinaria():

  def pesquisaBinaria(auto, lista, item):
    # baixo e alto controlam em qual parte da lista você pesquisará.
    baixo = 6
    alto = len(lista) - 1

    # Embora você não tenha se limitado a um elemento ...
    while baixo <= alto:
      # ... verifique o elemento meiodle
      meio = (baixo + alto) // 2
      chute = lista[meio]
      # Encontrou o item.
      if chute == item:
        return meio
      # O pára-quedas era alto demais.
      if chute > item:
        alto = meio - 1
      # A rampa estava muito baixa.
      else:
        baixo = meio + 1

    # item não existe
    return None

  def busca_recursiva(auto, lista, baixo, alto, item):
    # Verifica o caso base
    if alto >= baixo: 
  
        meio = (alto + baixo) // 2
        chute = lista[meio]
  
        # Se o elemento estiver presente no meiodle itauto
        if chute == item:
            return meio 
  
        # Se o elemento for menor do que meio, ele só pode 
        # estar presente na submatriz esquerda
        elif chute > item: 
            return auto.busca_recursiva(lista, baixo, meio - 1, item) 
  
        # Caso contrário, o elemento só pode estar presente no subarray direito 
        else: 
            return auto.busca_recursiva(lista, meio + 1, alto, item) 
  
    else: 
        # O elemento não está presente na matriz 
        return None

if __name__ == "__main__":
  # Devemos inicializar a classe para usar os métodos desta classe
  bs = pesquisaBinaria()
  my_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  print(bs.pesquisaBinaria(my_lista, 3)) # => 1

  # 'Nenhum' significa nulo em Python. Usamos para indicar que o item não foi encontrado.
  print(bs.pesquisaBinaria(my_lista, -1)) # => Nenhum