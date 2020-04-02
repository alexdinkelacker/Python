# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 00:18:48 2020

@author: alexd
"""

from PIL import Image

alexIm = Image.open("Guido.jpg")

width, height = alexIm.size

alexHalfRed = alexIm.copy()
alexElimRed = alexIm.copy()
alexDubGB = alexIm.copy()
alexNeg = alexIm.copy()

for row in range(height):
    for col in range(width):
        colorPixel = alexIm.getpixel((col,row))
        halfRed = colorPixel[0] - (255//2)
        elimRed = colorPixel[0] - 255
        doubleGreen = colorPixel[1]*2
        doubleBlue = colorPixel[2]*2
        negRed = 255 - colorPixel[0]
        negGreen = 255 - colorPixel[1]
        negBlue = 255 - colorPixel[2]
        red = colorPixel[0]
        green = colorPixel[1]
        blue = colorPixel[2]
        alexHalfRed.putpixel((col,row),(halfRed,green,blue))
        alexElimRed.putpixel((col,row),(elimRed,green,blue))
        alexDubGB.putpixel((col,row),(red,doubleGreen,doubleBlue))
        alexNeg.putpixel((col,row),(negRed,negGreen,negBlue))
    

        
alexHalfRed.save("guidoHalfRed.jpg")
alexElimRed.save("guidoElimRed.jpg")
alexDubGB.save("guidoDubGB.png")
alexNeg.save("guidoNeg.png")


guidoIm = Image.open("Guido.jpg")

width0, height0 = guidoIm.size

#CREATE BACKGROUND TO PASTE INTO 
backG = Image.new('RGBA',(width0*2,height0),(231,225,206,225))
backG.save("blank.png")

#CREATE A HORIZONTALLY FLIPPED IMAGE 
horzFlip = guidoIm.transpose(Image.FLIP_LEFT_RIGHT)
horzFlip.save("guidoFlipped.png")

backG.paste(guidoIm,(0,0))
backG.paste(horzFlip, (width0,0))

backG.save("backToBack.png")

alex = Image.open("Guido.jpg")

width1, height1 = alex.size

backG2 = Image.new('RGBA',(width1*2,height1*2),(255,255,255,255))
backG2.save("blank0.png")

alexA = alex.copy()
alexB = alex.copy()
alexC = alex.copy()
alexD = alex.copy()
alexGray = alex.copy()

for row in range(height1):
    for col in range(width1):
        colorPixel = alex.getpixel((col,row))
        redA = 255 - colorPixel[2]
        greenA = colorPixel[0]
        blueA = colorPixel[1]
        redB = colorPixel[1]
        greenB = colorPixel[2]
        blueB = 255 - colorPixel[0]
        redC = colorPixel[1]
        greenC = colorPixel[0]
        blueC = colorPixel[2]
        redD = colorPixel[2]
        greenD = 50 - colorPixel[1]
        blueD = 255 - colorPixel[1]
        alexA.putpixel((col,row),(redA,greenA,blueA))
        alexB.putpixel((col,row),(redB,greenB,blueB))
        alexC.putpixel((col,row),(redC,greenC,blueC))
        alexD.putpixel((col,row),(redD,greenD,blueD))
        red = colorPixel[0]
        green = colorPixel[1]
        blue = colorPixel[2]
        gray = (red+green+blue)//3
        alexGray.putpixel((col,row),(gray,gray,gray))

alexA.save("guidoA.png")
alexB.save("guidoB.png")
alexC.save("guidoC.png")
alexD.save("guidoD.png")
alexGray.save("guidoGray.png")

backG2.paste(alexA,(0,0))
backG2.paste(alexB,(width1,0))
backG2.paste(alexC,(0,height1))
backG2.paste(alexD,(width1,height1))

backG2.save("guidoWarhol.png")
backG2.show()
