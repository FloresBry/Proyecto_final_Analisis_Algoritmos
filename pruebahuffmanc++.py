import heapq
import time
import busqueda
from bitarray import bitarray

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
    ba = bitarray(bin_str)   # empaquetar bits
    return ba

# Texto grande y patrón
cadena_grande = "hola hola hola hola " * 100
patron = "hola"

# Diccionario Huffman
diccionario = huffman_encoding(cadena_grande + patron)

# Compresión en bitarray
bit_grande = compresion(cadena_grande, diccionario)
bit_patron = compresion(patron, diccionario)

# Convertir a bytes para C++
data_bytes = bit_grande.tobytes()
pattern_bytes = bit_patron.tobytes()

# Llamada al módulo C++
start_time = time.time()
posiciones = busqueda.buscar_patron_binario(
    list(data_bytes), list(pattern_bytes), len(bit_patron)
)
end_time = time.time()

print(f"Se encontró el patrón {len(posiciones)} veces en posiciones: {posiciones[:10]}...")
print(f"Tiempo de búsqueda: {end_time - start_time:.6f} segundos")
