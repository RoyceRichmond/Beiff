import cv2
import numpy as np
from matplotlib import cm
from PIL import Image
constant =100/46
#path for the images, this can be changed further
path="D:/Users/Richmond/Desktop/Proyecto.Aire/codigo/fernando/"
img00 = cv2.imread(path+'3.png')
img0 = cv2.imread(path+'2.png')
img1 = cv2.imread(path+'1.png')
img2 = cv2.imread(path+'original.png')
inmasks=[img00,img0,img1]
masked_images=[]
for a in range(0,3):
  #RGB to gray scale
  img2gray = cv2.cvtColor(inmasks[a],cv2.COLOR_BGR2GRAY)
  #binary threshold
  ret, mask = cv2.threshold(img2gray, 120, 255, cv2.THRESH_BINARY_INV)
  #mask operation to separate areas of interest
  masked = cv2.bitwise_and(img2, img2, mask = mask)
  #optional code to display the images, it waits for a user input to proceed with the next image
  cv2.imshow("Mask Applied to Image", masked)
  cv2.waitKey(0)
  #conversion of the image to PILImage format
  im_rgb = cv2.cvtColor(masked, cv2.COLOR_BGR2RGB)
  conv=Image.fromarray(im_rgb)
  masked_images.append(conv)
  
def contarArea(pathImage):
  im = pathImage
  colores = {
    "rapido":  {"RGB": (100,215,104), "contador": 0,"porcentaje":0},
    "medio":  {"RGB": (255,151,76), "contador": 0,"porcentaje":0},
    "disminuido": {"RGB": (243,60,48), "contador": 0,"porcentaje":0},
    "lento": {"RGB": (128,32,32), "contador": 0,"porcentaje":0},
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
    print(color,resultado[color]['contador'])

#Hacemos lectura de las imagenes
for a in range(0,3):
  resultado = contarArea(masked_images[a])
  print("pixeles en el area de interes")
  imprimirResultado(resultado)
  
  print('\n')