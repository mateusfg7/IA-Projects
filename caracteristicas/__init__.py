def caracteristicas():
    lista_de_caracteristicas = []
    # tem pelo?
    pelo = input("[s/n] tem pelos? ").replace("s", "1").replace("n", "0")
    lista_de_caracteristicas.append(pelo)
    
    # late?
    late = input("[s/n] late? ").replace("s", "1").replace("n", "0")
    lista_de_caracteristicas.append(late)
    
    # gosta de lama?
    lama = input("[s/n] gota de lama? ").replace("s", "1").replace("n", "0")
    lista_de_caracteristicas.append(lama)
    
    # toma banho?
    banho = input("[s/n] toma banho? ").replace("s", "1").replace("n", "0")
    lista_de_caracteristicas.append(banho)
    
    # gosta de carne?
    carne = input("[s/n] gosta de carne? ").replace("s", "1").replace("n", "0")
    lista_de_caracteristicas.append(carne)
    
    # come legumes?
    legumes = input("[s/n] come legumes? ").replace("s", "1").replace("n", "0")
    lista_de_caracteristicas.append(legumes)
    
    # corre atras de gatos?
    gatos = input("[s/n] corre atras de gatos? ").replace("s", "1").replace("n", "0")
    lista_de_caracteristicas.append(gatos)

    caracteristicas_binario = []

    for i in lista_de_caracteristicas:
        caracteristicas_binario.append(int(i))
    
    # CÃO = 1
    # PIG = 0
    return caracteristicas_binario

