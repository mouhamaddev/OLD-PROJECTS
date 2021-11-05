import cv2
import numpy as np
import pandas as pd
import argparse

img_path = "1.jpg"
try:
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True, help="Image Path")
    args = vars(ap.parse_args())
    img_path = args['image']
except:
    pass
img = cv2.imread(img_path)

clicked = False
r = g = b = xpos = ypos = 0

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        global b, g, r, xpos, ypos, clicked
        
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while (1):

    
    cv2.imshow("image", img)

    cv2.rectangle(img, (20, 20), (750, 60), (255, 0, 0), -1)


    Y = 0.2126*r + 0.7152*g + 0.0722*b

    print(Y)

    if Y > 200:
        text = "Clean teeth"
        cv2.putText(img, text, (50, 50), 2, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    else :
        text2 = "Unclean teeth"
        cv2.putText(img, text2, (50, 50), 2, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
    

    

    if r + g + b >= 600:
        cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
