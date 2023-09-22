listaBase = [0, 1, 2, 3, 4, 5]
def criaNovaLista():
    novaLista = []

    for elemento in listaBase:
        novaLista.append(elemento)
    return novaLista

def geraNovaLista():
    for elemento in listaBase:
        yield elemento

novaLista = criaNovaLista()
listaGerada = geraNovaLista()

print(f" Criou uma nova Lista: {novaLista}")

for item in listaGerada:
    print(item)

