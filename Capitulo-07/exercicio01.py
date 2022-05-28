# O grafo
graph = {}

graph["inicio"] = {}
graph["inicio"]["a"] = 10
graph["inicio"]["b"] = 30

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fim"] = 30

graph["c"] = {}
graph["c"]["a"] = 1

graph["fim"] = {}

# a tabela de custos
infinity = float("inf")
costs = {}
costs["a"] = 10
costs["b"] = 30
costs["c"] = 31
costs["fim"] = infinity

# a mesa dos pais
parents = {}
parents["a"] = "inicio"
parents["b"] = "a"
parents["c"] = "b"
parents["fim"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Passe por cada nó.
    for node in costs:
        cost = costs[node]
        # Se é o menor custo até agora e ainda não foi processado ...
        if cost < lowest_cost and node not in processed:
            # ... defina-o como o novo nó de menor custo.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Encontre o nó de custo mais baixo que você ainda não processou.
node = find_lowest_cost_node(costs)
# Se você processou todos os nós, este loop while está concluído.
while node is not None:
    cost = costs[node]
    # Passe por todos os vizinhos deste nó.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Se for mais barato chegar a este vizinho passando por este nó ...
        if costs[n] > new_cost:
            # ... atualize o custo para este nó.
            costs[n] = new_cost
            # Este nó se torna o novo pai para este vizinho.
            parents[n] = node
    # Marque o nó como processado.
    processed.append(node)
    # Encontre o próximo nó a processar e faça um loop.
    node = find_lowest_cost_node(costs)

print("Custo desde o inicio ate cada no:")
print(costs)