tabla = [1, 2, 3, 4, 5, 6, 7, 8]
valor_buscado = int(input('Introduzca el valor que desea encontrar: '))

indice_inicial = 0
indice_final = len(tabla) - 1
while indice_inicial <= indice_final:
    indice_medio = (indice_inicial + indice_final) // 2
    if tabla[indice_medio] == valor_buscado:
        print(f'El valor {valor_buscado} se encuentra en la posición {indice_medio}')
        break
    elif tabla[indice_medio] < valor_buscado:
        indice_inicial = indice_medio + 1
    else:
        indice_final = indice_medio - 1
else:
    print(f'El valor {valor_buscado} no se encuentra en la lista')
