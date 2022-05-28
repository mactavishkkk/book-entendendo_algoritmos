# Existem duas formas populares para a criação de tabelas hash:
# Usando "dict()" ou "{}"

# Tabela de preços com hash
lista_de_precos = dict()

lista_de_precos["Maca"] = 0.67
lista_de_precos["Abacate"] = 1.30
lista_de_precos["Ovo"] = 0.50
lista_de_precos["Leite"] = 2.34

print(lista_de_precos["Ovo"])

# Lista telefônica com hash
lista_telefonica = {}

lista_telefonica["Mae"] = 981654714
lista_telefonica["Policia"] = 190
lista_telefonica["Eu"] = 981260831

print(lista_telefonica["Mae"])

# Lista de votos com hash
votaram = {}

# Esta função checka se essa tal pessoa ja votou
def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Dispense-o!")
    else:
        votaram[nome] = True
        print("Libere-o!")

verifica_eleitor("Mike")