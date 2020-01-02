from PIL import Image

imagem = Image.open('image.jpg')

pixels = list(imagem.getdata())

pixels = str(pixels).replace('251', '1').replace('249', '1').replace('248', "1").replace('250', '1').replace('252', '1')
pixels = pixels.replace('1','')

print(pixels)