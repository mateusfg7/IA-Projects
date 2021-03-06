try:
    from sklearn.svm import LinearSVC
    from sklearn.model_selection import train_test_split
except ModuleNotFoundError:
    print("Biblioteca sklearn.svm não encontrada!")
    print("execute no terminal\n $ python3.7 -m pip install -U sklearn")
    exit()

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Biblioteca pandas não encontrada!")
    print("execute no terminal\n $ python3.7 -m pip install -U pandas")
    exit()

from caracteristicas import caracteristicas
from info_analise import analise
from dados import validar_dados

import_csv = "dados.csv"
dados = pd.read_csv(import_csv)

treino_x = dados[["pelo","late","lama","banho","carne","legume","gatos"]]
treino_y = dados["animal"]

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)

ser = caracteristicas()

predicao = modelo.predict([ser])

animal = analise(predicao)

print("Isso é um {}".format(animal))
validar_dados(ser, predicao)
