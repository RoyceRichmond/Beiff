from opencv import *
#path for the images, this can be changed further
path="D:/Users/Richmond/Desktop/Proyecto.Aire/codigo/fernando/"
index='1'
masked=process_images(path+index)
for a in range(0,3):
  resultado = contarArea(masked[a])
  print("pixeles en el area de interes")
  imprimirResultado(resultado)
  print('\n')