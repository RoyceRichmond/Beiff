from opencv import *
import schedule
import time
from get_image_streets import *
number_stations=4 #this value is changed accordign to the number of stations

def taskk():
  save_images()
  #a=carreteras
  #b=avenida principal
  #c=calles secundarias
  #the script and the images should be in the same folder in order to work properly.
  masked=[]
  for a in range(1,number_stations+1):
    masked.append(process_images(str(a))) #appends the 3 masks of the streets      #a=carreteras        #b=avenida principal       #c=calles secundarias
  for a in range(0,number_stations):
    f=distancias(masked[a])#this vector return the total distance of the traffic state in the map
    print(f)
    #the next line is for demostrative purposes, it can be commented
    print('[rapido, medio, disminuido ,lento]')#this is the order of the distances presented in the above line

schedule.every(1).minutes.do(taskk)
while True:
  schedule.run_pending()
  time.sleep(1)