import numpy as np
from PIL import Image

#First we will define the 2 levels of grayscale we will use :)

grayscale1 = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`". '
grayscale2 = '@%#*+=-:. '


#Now we will compute the average brightness HEEEEEEEEEEEEEEEEELLLLLLLLLLLPPPPPPPPP

def getAverageL(image):
    im = np.array(image)
    w,h = im.shape
    return np.average(im.reshape(w*h))  #Yaaaiii

#Now we will create the ASCII content FROM the image (i <3 technologia)

def image_to_ascii(fileName, cols=80, scale=0.5, moreLevels=False, color=False):
    imageOriginal = Image.open(fileName) 
    imageGray = imageOriginal.convert("L") #We convert the image to a grayscale image
    imageRGB = imageOriginal.convert("RGB") #We convert the image to a RGB image
    W, H = imageGray.size[0], imageGray.size[1]
    w = W/cols
    h = w/scale
    rows = int(H/h)

    aimg = []

    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        if j == rows-1:
            y2 = H

        aimg.append("")
        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)

            if i == cols-1:
                x2 = W

            img = imageGray.crop((x1, y1, x2, y2))
            avg = int(getAverageL(img))
            if moreLevels:
                gsval = grayscale1[int((avg*69)/255)]
            else:
                gsval = grayscale2[int((avg*9)/255)]
            if color:
                imgRGB = imageRGB.crop((x1, y1, x2, y2))
                imRGB = np.array(imgRGB)
                r, g, b = np.mean(imRGB, axis= (0,1))
                r, g, b = int(r), int(g), int(b)
                colorCode = f"\033[38;2;{r};{g};{b}m"
                gsval = colorCode + gsval
            aimg[j] += gsval
        if color:
            aimg[j] += "\033[0m"
    return aimg