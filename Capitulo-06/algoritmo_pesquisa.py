from collections import deque
# Agora, o algoritmo de pesquisa na pratica para a resolução do problema 

def pessoa_e_vendedor(nome):
    return nome[-1] == 'e'

grafo = {}
grafo["Eu"] = ["Alice", "Bob", "Claire"]
grafo["Bob"] = ["Anuj", "Peggy"]
grafo["Alice"] = ["Peggy"]
grafo["Claire"] = ["Thom", "Jonny"]
grafo["Anuj"] = []
grafo["Peggy"] = []
grafo["Thom"] = []
grafo["Jonny"] = []

def pesquisa(nome):
    fila_pesquisa = deque()
    fila_pesquisa += grafo[nome]
# É assim que você controla as pessoas que já pesquisou.
    procurado = set()
    
    while fila_pesquisa:
        pessoa = fila_pesquisa.popleft()
# Somente pesquise esta pessoa se você ainda não a tiver pesquisado.
        if pessoa not in procurado:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " e um(a) vendedor(a) de mangas! ")
                return True
        else:
            fila_pesquisa += grafo["Eu"]
            # Marca esta pessoa como pesquisada
            procurado.add(pessoa)
            return False

pesquisa("Eu")