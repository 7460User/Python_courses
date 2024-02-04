import pyautogui
from PIL import Image,ImageGrab
import time
# from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(340, 450):
            for j in range(340, 470):
               if  data[i, j] <100:
                   return True
    return False             
    



if __name__=="__main__":
    time.sleep(2)
    print("this is game will start 3 secound:")
    hit('up')

    while True:
   
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")
        # print(asarray(image))
       
        

            

