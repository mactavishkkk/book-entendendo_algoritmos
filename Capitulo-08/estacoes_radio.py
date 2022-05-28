# Você passa um array e ele é convertido em um conjunto.
estados_necessarios = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estacoes = {}
estacoes["kone"] = set(["id", "nv", "ut"])
estacoes["ktwo"] = set(["wa", "id", "mt"])
estacoes["kthree"] = set(["or", "nv", "ca"])
estacoes["kfour"] = set(["nv", "ut"])
estacoes["kfive"] = set(["ca", "az"])

estacoes_finais = set()

while estados_necessarios:
  melhor_estacao = None
  estados_abordados = set()
  for estacao, estados_para_estacao in estacoes.items():
    abordados = estados_necessarios & estados_para_estacao
    if len(abordados) > len(estados_abordados):
      melhor_estacao = estacao
      estados_abordados = abordados

  estados_necessarios -= estados_abordados
  estacoes_finais.add(melhor_estacao)

print(estacoes_finais)