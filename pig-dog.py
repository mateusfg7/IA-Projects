try:
    from sklearn.svm import LinearSVC
except ModuleNotFoundError:
    print("Biblioteca sklearn.svm não encontrada!")
    print("execute no terminal\n $ python3.7 -m pip install -U sklearn")
    exit()

from caracteristicas import caracteristicas

cao1 = [1,1,0,1,1,0,1]
cao2 = [1,1,1,0,1,0,1]
cao3 = [0,0,0,1,1,1,0]



pig1 = [0,0,1,0,0,1,0]
pig2 = [0,0,1,0,1,0,0]
pig3 = [0,0,0,1,1,1,0]

treino_x = [cao1,cao2,cao3,pig1,pig2,pig3]
treino_y = [1,1,1,0,0,0]

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
ser = caracteristicas()


teste_x = [ser]
predicao = modelo.predict(teste_x)
print(predicao)
