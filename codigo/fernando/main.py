from opencv import *
masked=[]
for a in range(1,5):
  masked.append(process_images(str(a))) #appends the 3 masks of the streets      #a=carreteras        #b=avenida principal       #c=calles secundarias
#for a in range(0,4):
#  for b in range(0,3):
#    resultado = contarArea(masked[a][b])
#    print("pixeles en el area de interes")
#    imprimirResultado(resultado)
#    print('\n')
for a in range(0,4):
  print(distancias(masked[a]))
  print('[rapido, medio, disminuido ,lento]')