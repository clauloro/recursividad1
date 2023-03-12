def busqueda_numérica(tabla, n, i, j):
    if i > j:
        return 'No se encontró el valor'
    else:
        m = (i + j) // 2
        if tabla[m] == n:
            return m
        elif tabla[m] < n:
            return busqueda_numérica(tabla, n, m + 1, j)
        else:
            return busqueda_numérica(tabla, n, i, m - 1)

tabla = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input('Introduzca el valor que desea encontrar: '))
resultado = busqueda_numérica(tabla, n, 0, len(tabla) - 1)
print(resultado)

