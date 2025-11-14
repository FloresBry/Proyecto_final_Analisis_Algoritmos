import heapq
import busqueda
import time
def huffman_encoding(data):
    freq = {}
    for ch in data:
        freq[ch] = freq.get(ch, 0) + 1
    heap = [[w, [ch, ""]] for ch, w in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for p in left[1:]:
            p[1] = '0' + p[1]
        for p in right[1:]:
            p[1] = '1' + p[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return {ch: code for ch, code in heap[0][1:]}

def compresion(data, diccionario):
    bin_str = ''.join(diccionario[ch] for ch in data)
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
posiciones = busqueda.buscar_patron_binario(bit_grande, bit_patron)
end_time2 = time.time()
print(f"Se encontró el patrón {len(posiciones)} veces en posiciones: {posiciones[:10]}...")
print(f"Tiempo de búsqueda: {end_time2 - start_time2:.6f} segundos")