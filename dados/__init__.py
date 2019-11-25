def validar_dados(caracteristicas, animal):
    resultado = input("[s/n] A resposta esta correta? ")

    if resultado == "s":
        lista = "\n{},{},{},{},{},{},{},{}".format(
            caracteristicas[0],
            caracteristicas[1],
            caracteristicas[2],
            caracteristicas[3],
            caracteristicas[4],
            caracteristicas[5],
            caracteristicas[6],
            animal[0]
        )
        arquivo = open("dados.csv", "a")
        arquivo.write(lista)
        arquivo.close()