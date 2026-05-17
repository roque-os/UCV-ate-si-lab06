import heapq

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristica = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def a_star(inicio, objetivo):
    cola = [(0, inicio)]
    visitados = set()
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        _, actual = heapq.heappop(cola)

        if actual == objetivo:
            break

        visitados.add(actual)

        for vecino, costo in grafo[actual]:
            nuevo_costo = costos[actual] + costo

            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica[vecino]
                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = actual

    return padres

resultado = a_star('A', 'F')
print(resultado)

# Reconstruir ruta
def reconstruir_ruta(padres, objetivo):
    ruta = []
    actual = objetivo
    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]
    ruta.reverse()
    return ruta

ruta = reconstruir_ruta(resultado, 'F')
print("Ruta encontrada:", ruta)