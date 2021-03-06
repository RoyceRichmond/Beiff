import cv2
import numpy as np
from matplotlib import cm
from PIL import Image
#a=carreteras
#b=avenida principal
#c=calles secundarias
def process_images(path):
  img00 = cv2.imread(path+'a.png')
  img0 = cv2.imread(path+'b.png')
  img1 = cv2.imread(path+'c.png')
  img2 = cv2.imread(path+'.png')
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
    #cv2.imshow("Mask Applied to Image", masked)
    #cv2.waitKey(0)
    #conversion of the image to PILImage format
    im_rgb = cv2.cvtColor(masked, cv2.COLOR_BGR2RGB)
    conv=Image.fromarray(im_rgb)
    masked_images.append(conv)
  return masked_images 

def contarArea(pathImage):
  im = pathImage
  colores = {
    "rapido":     {"RGB": (100,215,104), "contador": 0},
    "medio":      {"RGB": (255,151,76),  "contador": 0},
    "disminuido": {"RGB": (243,60,48),   "contador": 0},
    "lento":      {"RGB": (128,32,32),   "contador": 0},
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
  return colores

def imprimirResultado(resultado):
  for color in resultado:
    print(color,resultado[color]['contador'])

def distancias(vector):
  c =100/46
  equivalences=[c/4,c/3,c/1]  
  rapido=0
  medio=0
  disminuido=0
  lento=0
  for b in range(0,3):
    resultado = contarArea(vector[b])
    rapido+=resultado['rapido']['contador']*equivalences[b]
    medio+=resultado['medio']['contador']*equivalences[b]
    disminuido+=resultado['disminuido']['contador']*equivalences[b]
    lento+=resultado['lento']['contador']*equivalences[b]
  return [rapido*0.9,medio*0.9,disminuido*0.9,lento*0.9]