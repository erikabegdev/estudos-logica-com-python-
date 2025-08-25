# Desafio: Ordenar uma lista sem usar sorted()
lista = [int(x) for x in input("Digite números separados por espaço: ").split()]
# Bubble sort
for i in range(len(lista)):
    for j in range(0, len(lista)-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print("Lista ordenada:", lista)