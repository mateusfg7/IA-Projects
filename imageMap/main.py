from PIL import Image

imagem = Image.open('image.jpg')

pixels = imagem.getdata()

print(pixels)