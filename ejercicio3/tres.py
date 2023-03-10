def ordenar_fichas(fichas):
    rojas= []
    verdes= []
    azules = []
    for ficha in fichas:
        if ficha== "rojo":
            rojas.append(ficha)
        elif ficha == "verde":
            verdes.append(ficha)
        elif ficha == "azul":
            azules.append(ficha)
    return rojas + verdes + azules 
print(ordenar_fichas(["rojo","azul","azul","rojo","verde","azul","azul","rojo","azul","rojo","rojo","verde","rojo","rojo","azul","verde","verde"]))