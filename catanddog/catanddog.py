from sympy import true
from ultralytics import YOLO
import svgutils.transform as sg
import svgwrite
import sys
import re

# Load a model
model = YOLO("yolov8n.pt")

#képek amelyeken végezzük a képfelismerést
results = model(['2dogs2cats.jpg'])

#háttér betöltése
background = sg.fromfile('empty.svg')
print("Háttér mérete:", background.get_size())


#svg tömb inicializálása
svg_files = []

#háttérhez átszámítom az eredeti svg fájlokat
cicaarany = 273/384
kutyaarany = 273/332


#képeken végigmegy
for result in results:
    #felismert objektumok adatai
    boxes = result.boxes.xywhn.tolist()
    classes = result.boxes.cls.tolist()
    names = result.names
    i = 0

    for cls in classes:
        if(cls == 15):
            #cat.svg betöltése
            cat1 = sg.fromfile('cat.svg')
            catboxes1 = boxes[i]
            print("Macska.svg mérete:", cat1.get_size())
            print("Macska koordináták:", catboxes1)
            #külön kiszedem a tömbből az adatokat
            x1 = (catboxes1[0])
            y1 = (catboxes1[1])
            scalex = (catboxes1[2])
            scaley = (catboxes1[3])
            #új x és y koordináták
            newX1 = 300 * x1 - ((cicaarany*scalex)*300) / 2
            newY1 = 273 * y1 - ((cicaarany*scaley)*273) / 2
            print("Átszámolt koordináták:", newX1, newY1)
            #háttérre rárakom
            root1 = cat1.getroot()
            root1.moveto(newX1, newY1,  cicaarany*scalex, cicaarany*scaley)
            background.append([root1])
            background.save('output.svg')



        if(cls == 16):
            dog = sg.fromfile('dog.svg')
            dogboxes = boxes[i]
            print("Kutya mérete:", dog.get_size())
            print("Kutya koordináták:", dogboxes)
            # külön kiszedem a tömbből az adatokat
            x1 = (dogboxes[0])
            y1 = (dogboxes[1])
            # új x és y koordináták
            scalex = (dogboxes[2])
            scaley = (dogboxes[3])
            newX1 = 300 * x1 - ((kutyaarany*scalex)*300) / 2
            newY1 = 273 * y1 - ((kutyaarany*scaley)*384) / 2
            print("Átszámolt koordináták:", newX1, newY1)
            #hátérre rárakom
            root = dog.getroot()
            root.moveto(newX1, newY1, kutyaarany*scalex, kutyaarany*scaley)
            background.append([root])
            background.save('output.svg')

        i+=1
