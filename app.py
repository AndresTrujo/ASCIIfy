import sys
from PIL import Image

# Escala de brillo usando caracteres gráficos extendidos, ordenados de oscuro a claro
ASCII_CHARS = (
    "█"  # 219 Full block
    "▓"  # 178 Dark shade
    "╬" "╫" "╪"  # Box drawings dense cross
    "▒"  # 177 Medium shade
    "╩" "╦" "╠" "╣" "╬"  # Box corners/double joints
    "║" "═"  # Double vertical/horizontal
    "╚" "╔" "╩" "╦"  # Corners
    "╡" "╢" "╞" "╟"  # Box joins
    "│" "─"  # Light lines
    "┼" "┤" "├" "┬" "┴"  # Light box joins
    "░"  # 176 Light shade
    "·" " "  # Dots and space (lightest)
)

# Mapeo de brillo a carácter ASCII
def map_brightness_to_ascii(brightness):
    scale = len(ASCII_CHARS) - 1
    index = int((brightness / 255) * scale)
    return ASCII_CHARS[index]

# Cálculo de brillo
def get_brightness(pixel, method=1):
    r, g, b = pixel[:3]
    if method == 1:
        return (r + g + b) // 3
    elif method == 2:
        return (max(pixel) + min(pixel)) // 2
    elif method == 3:
        return int(0.21 * r + 0.72 * g + 0.07 * b)
    else:
        return (r + g + b) // 3

# Convertir imagen a ASCII
def image_to_ascii(image_path, method=1, width=100):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return

    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width * 0.5)  # Ajuste visual
    img = img.resize((width, new_height))
    img = img.convert("RGB")

    for y in range(img.height):
        for x in range(img.width):
            brightness = get_brightness(img.getpixel((x, y)), method)
            char = map_brightness_to_ascii(brightness)
            print(char * 2, end="")  # Duplicamos para aspecto proporcional
        print()

# Uso desde línea de comandos
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <nombre_imagen> [metodo]")
        sys.exit(1)

    image_file = f"img/in/{sys.argv[1]}"
    method = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 1
    image_to_ascii(image_file, method, width=100)