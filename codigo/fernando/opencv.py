import cv2
import numpy as np
from PIL import Image
from matplotlib import cm
path="D:/Users/Richmond/Desktop/Proyecto.Aire/codigo/fernando/"
img00 = cv2.imread(path+'3.png')
img0 = cv2.imread(path+'2.png')
img1 = cv2.imread(path+'1.png')
img2 = cv2.imread(path+'original.png')
inmasks=[img00,img0,img1]
masked_images=[]
for a in range(0,3):
    img2gray = cv2.cvtColor(inmasks[a],cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY_INV)
    masked = cv2.bitwise_and(img2, img2, mask = mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)
    conver=Image.fromarray(masked)
    masked_images.append(conver)
    
    
    
constant =100/46
def contarArea(imagedata):
  colores = {
    "rapido":  {"RGB": (99,214,104), "contador": 0,"porcentaje":0},
    "medio":  {"RGB": (255,163,100), "contador": 0,"porcentaje":0},
    "disminuido": {"RGB": (230,0,0), "contador": 0,"porcentaje":0},
    "lento": {"RGB": (243,60,48), "contador": 0,"porcentaje":0},
  }
  counterPixels = 0
  tolerancia = 5
  for pixel in imagedata.getdata():
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
for ind in range(0,3):
  resultado = contarArea(masked_images[ind])
  imprimirResultado(resultado)