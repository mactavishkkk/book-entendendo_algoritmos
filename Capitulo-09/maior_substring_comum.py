# Pseudocódigo
# Maior substring comum
if palavra_a[i] == palavra_b[i]:
    celula[i][j] = celula [i-1][j-1] + 1
    else:
        celula [i][j] = 0

# Pseudocódigo
# Maior subsequência comum
if palavra_a[i] == palavra_b[i]:
    celula[i][j] = celula [i-1][j-1] + 1
    else:
        celula [i][j] = max(celula[i-1][j], celula[i1][j-1])