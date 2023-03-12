def ordenar_fichas(fichas):
    if not fichas:
        return []
    rojas = []
    verdes = []
    no_ordenadas = []
    azules = []
    for ficha in fichas:
        if ficha == "R":
            rojas.append(ficha)
        elif ficha == "V":
            verdes.append(ficha)
        elif ficha == "A":
            azules.append(ficha)
        else:
            no_ordenadas.append(ficha)

    ordenadas_no_ordenadas = ordenar_fichas(no_ordenadas)
    return rojas + verdes + ordenadas_no_ordenadas + azules
