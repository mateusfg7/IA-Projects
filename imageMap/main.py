from sklearn.svm import LinearSVC
modelo = LinearSVC()

from PIL import Image

quadrado = Image.open('quadrado.jpeg')
circulo = Image.open('circulo.jpeg')

pixelsQuadrado = list(quadrado.getdata())
pixelsCirculo = list(circulo.getdata())

quadradoImage = []
circuloImage = []

for pixel in pixelsQuadrado:
    for value in pixel:
        quadradoImage.append(value)

for pixel in pixelsCirculo:
    for value in pixel:
        circuloImage.append(value)


treino_x = [quadradoImage, circuloImage]
treino_y = [1, 2]

modelo.fit(treino_x, treino_y)


# 1 > CACHORRO
# 2 > GATO
print(modelo.predict(treino_x))