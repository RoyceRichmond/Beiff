from opencv import *
masked=[]
for a in range(1,4):
  masked.append(process_images(str(a))) #appends the 3 masks of the streets      #a=carreteras        #b=avenida principal       #c=calles secundarias
#for a in range(0,3):
#  for b in range(0,3):
#    resultado = contarArea(masked[a][b])
#    print("pixeles en el area de interes")
#    imprimirResultado(resultado)
#    print('\n')
for a in range(0,3):
  print(distancias(masked[a]))
  print('\n')