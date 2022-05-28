# Grafos basicamente são formados por vértices e arestas
# Bastantes usados na que é chamado de "Pesquisa em largura"
# Uma das forma de se construir um grafo e com Tabelas hash

# A princípio voce consegue solucionar 2 problemas com grafos
# Se existe um caminho entre A e B e qual o menor caminho entre os mesmo

# Vamos supor que voce seja o dono de uma fazenda de mangas e esteja procurando um vendedor de mangas que possa vender sua colheita.
# Voce conhece algum vendedor de mangas no Facebook? Bem, voce pode procurar entre seus amigos

# Primeiro voce faz uma pesquisa de 1° que teria ai mais ou menos a resolução do problema com 1° Passo
# Que seria procurar dentre seus amigos

grafo = {}

grafo["Eu"] = ["Alice", "Bob", "Claire"]
print(grafo["Eu"])

# Voce também pode faze pesquisa de 2° grau que da mesma forma que a de 1° grau, simboliza a resolução do problema em 2 passos ou mais

grafoA = {}
grafoA["Eu"] = ["Alice", "Bob", "Claire"]
grafoA["Bob"] = ["Anuj", "Peggy"]
grafoA["Alice"] = ["Peggy"]
grafoA["Claire"] = ["Thom", "Jonny"]
grafoA["Anuj"] = []
grafoA["Peggy"] = []
grafoA["Thom"] = []
grafoA["Jonny"] = []

print(grafoA["Claire"])
