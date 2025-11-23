import heapq
import busqueda
import time

def huffman_encoding(data):
    # Check for empty input
    if not data:
        return "", None
    frequency = {}
    for char in data:
    # Calculamos la frecuencia de cada caracter
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    # Create a priority queue
    nodo = [[weight, [char, ""]] for char, weight in frequency.items()]
    while len(nodo) > 1:
        # Ordenamos los nodos por frecuencia
        nodo = sorted(nodo)
        # Tomamos los dos nodos con menor frecuencia
        izquierda = nodo[0]
        derecha = nodo[1]
        for par in izquierda[1:]:
            # agregamos '0' al frente de cada código
            par[1] = '0' + par[1]
        for par in derecha[1:]:
            # agregamos '1' al frente de cada código
            par[1] = '1' + par[1]
        nodo = nodo[2:]
        # combinamos los dos nodo
        nodo.append([izquierda[0] + derecha[0]] + izquierda[1:] + derecha[1:])
    # Creamos la lista de códigos Huffman
    huffman_code = sorted(nodo[0][1:], key=lambda p: (len(p[-1]), p))
    # Lo convertimos en un diccionario
    huffman_diccionario = {char: code for char, code in huffman_code}
    return huffman_diccionario

def compresion(data, diccionario):
    bin_str = ''.join(diccionario[char] for char in data)
    return [int(b) for b in bin_str]  # lista de bits

cadena_grande = (
    "hola mundo, este es un ejemplo de texto largo donde quiero probar la compresion. "
    "El algoritmo de Huffman asigna códigos más cortos a los caracteres frecuentes. "
    "hola universo, hola galaxia, hola sistema solar, hola estrella, hola planeta. "
    "Este texto contiene múltiples ocurrencias de la palabra hola para que podamos "
    "buscarla en la versión comprimida. hola hola hola hola hola hola hola hola hola hola. "
    "Además agregamos frases adicionales para aumentar el tamaño del corpus y hacer "
    "que la búsqueda sea más interesante. hola tierra, hola marte, hola jupiter, hola saturno. "
    "Seguimos repitiendo la palabra hola en diferentes contextos: hola amigo, hola vecino, "
    "hola computadora, hola programa, hola algoritmo, hola datos, hola binario, hola bits. "
    "Este texto es suficientemente largo y puede repetirse varias veces para simular un corpus real. "
) * 50
patron = "hola"

diccionario = huffman_encoding(cadena_grande + patron)
bit_grande = compresion(cadena_grande, diccionario)
bit_patron = compresion(patron, diccionario)

print("bit_grande:", bit_grande[:20], "...")
print("bit_patron:", bit_patron)
start_time2 = time.time()
posiciones = busqueda.divide_and_conquer_search(bit_grande, bit_patron,0)
end_time2 = time.time()
print(f"Se encontró el patrón {len(posiciones)} veces en posiciones: {posiciones[:10]} ...")
print(f"Tiempo de búsqueda: {end_time2 - start_time2:.6f} segundos")


