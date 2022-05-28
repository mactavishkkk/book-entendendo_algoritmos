# Tambem com tabelas hash, é possível criar ...
# ... um pequeno sistema de caching

cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_servidor(url)
        cache[url] = dados
        return dados