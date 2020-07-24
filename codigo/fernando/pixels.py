from PIL import Image
constant =100/46
path="D:/Users/Richmond/Desktop/Proyecto.Aire/codigo/fernando/"
def contarArea(pathImage):
  mask = Image.open(pathImage+'1.png')
  im = Image.open(pathImage+'original.png')
  colores = {
    "gris":  {"RGB": (228,227,223), "contador": 0,"porcentaje":0},
    "azul":  {"RGB": (0,18,252), "contador": 0,"porcentaje":0},
    "blanco": {"RGB": (252,252,252), "contador": 0,"porcentaje":0},
    "amarillo": {"RGB": (255,240,0), "contador": 0,"porcentaje":0},
  }
  counterPixels = 0
  tolerancia = 5
  for pixel in im.getdata():
    for color in colores:
      verificador = True
      for valueRGB in range(3):
        if not (pixel[valueRGB] <= colores[color]["RGB"][valueRGB]+tolerancia and pixel[valueRGB] >= colores[color]["RGB"][valueRGB]-tolerancia):
          verificador = False
          break
      if verificador:
        colores[color]["contador"] += 1 
    counterPixels += 1
  #Añadir porcentaje
  for color in colores:
    colores[color]["porcentaje"] = 100*colores[color]["contador"]/counterPixels 
  return colores

def imprimirResultado(resultado):
  for color in resultado:
    print(color,resultado[color])

#Hacemos lectura de las imagenes
resultado = contarArea(path)
#resultado = contarArea(path+"{}.png".format(i))
imprimirResultado(resultado)