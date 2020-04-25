from PIL import Image
image = Image.open('a.png')
image1 = Image.open('a.png')

image_data = image.load()
image_data1 = image1.load()
height,width = image.size

for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = image_data[loop1,loop2]
        r2,g2,b2 = image_data1[loop1,loop2]
        if(r==255 and g==173 and b==31):##grieta
            image_data[loop1,loop2] = r2,g2,b2
            image_data1[loop1,loop2] = 0,0,0
        elif(r==63 and g==158 and b==249):##coladera
            image_data1[loop1,loop2] = r2,g2,b2
            image_data[loop1,loop2] = 0,0,0
        else:
            image_data1[loop1,loop2] = 0,0,0
            image_data[loop1,loop2] = 0,0,0
image1.save('changed.jpeg')
image.save('changedd.jpeg')
