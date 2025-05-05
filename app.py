import sys
from PIL import Image

mapeo = int(sys.argv[2]) if len(sys.argv) > 1 and sys.argv[2].isdigit() else 1 # leer argumento de la línea de comandos o asignar valor predeterminado

pic = Image.open(f"img/in/{sys.argv[1]}") # leer imagen
newpic = pic.resize((300, 278)) # redimensionar imagen a 100x100 píxeles
pixels = newpic.load()
width, height = newpic.size # obtener dimensiones de la imagen, pic.size devuelve una tupla (width, height) que se descompone en dos variables
ASCII_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # caracteres ASCII para representar el brillo de los píxeles
pixel_RGB_list = [] # lista para almacenar los píxeles

for y in range(height):
    row = [] # lista para almacenar los píxeles de  la fila actual
    for x in range(width):
        pixel = pixels[x, y]
        row.append(pixel) # agregar píxel a la fila        
    pixel_RGB_list.append(row) # agregar píxel a la lista

 # imprimir la lista de píxeles
pixel_brightness_list = [] # lista para almacenar el brillo de los píxeles
for RGBrow in pixel_RGB_list:
    bright_row = [] # lista para almacenar el brillo de los píxeles de la fila actual
    for pixel in RGBrow:
        if mapeo == 1:
            brightness = int((pixel[0] + pixel[1] + pixel[2]) / 3)
            bright_row.append(brightness)
        elif mapeo == 2:
            lightness = (max(pixel) + min(pixel)) / 2
            bright_row.append(lightness)
        elif mapeo == 3:
            luminosity = int((pixel[0] * 0.21 + pixel[1] * 0.72 + pixel[2] * 0.07))
            bright_row.append(luminosity)
    pixel_brightness_list.append(bright_row)
pixels__ASCII = []
for bright_row in pixel_brightness_list:
    ASCII_row = [] # lista para almacenar los caracteres ASCII de la fila actual
    for brightness in bright_row:
        # mapear el brillo a un carácter ASCII
        index = int((brightness / 255) * (len(ASCII_characters) - 1)) # calcular el índice del carácter ASCII
        ASCII_row.append(ASCII_characters[index]) # agregar carácter ASCII a la fila
    pixels__ASCII.append(ASCII_row) # agregar fila a la lista

# imprimir la lista de caracteres ASCII
for ASCIIrow in pixels__ASCII:
    for ASCII in ASCIIrow:
        print(ASCII, end="")
        print(ASCII, end="")
        print(ASCII, end="")# imprimir carácter ASCII sin salto de línea
    print() # imprimir salto de línea al final de la fila
    
