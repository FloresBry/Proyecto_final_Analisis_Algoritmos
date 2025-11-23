#función para generar todas las permutaciones de una lista 
# con programación dinámica
def permutas(lista,memoria={}):
    # Verificar si la permutación ya está en la memoria
    if tuple(lista) in memoria:
        # Devolver la permutación almacenada
        return memoria[tuple(lista)]
    # Caso base: si la lista tiene un solo elemento, es una permutación.
    if len(lista) <= 1:
        return [lista]
    # Lista para almacenar todas las permutaciones
    permutas_totales=[]
    # Recorrer cada elemento de la lista
    for i in range(len(lista)):
        elemento_actual = lista[i]
        # Crear una sub-lista con los elementos restantes
        resto_de_la_lista = lista[:i] + lista[i+1:]
        # Llamada recursiva para obtener las permutaciones de la sub-lista
        permutaciones_del_resto = permutas(resto_de_la_lista, memoria)
        # Iterar sobre las permutaciones de la sub-lista
        for p in permutaciones_del_resto:
            # Añadir el elemento actual al inicio de cada permutación del resto
            nueva_permutacion = [elemento_actual] + p
            permutas_totales.append(nueva_permutacion)
    # Almacenar la permutación en la memoria antes de devolverla
    memoria[tuple(lista)] = permutas_totales
    # Devolver todas las permutaciones encontradas
    return permutas_totales
