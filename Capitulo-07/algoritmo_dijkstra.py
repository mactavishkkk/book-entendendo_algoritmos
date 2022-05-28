# O grafo
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# a tabela de custos
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# a mesa dos pais
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

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