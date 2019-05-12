import Tkinter
import picamera
from threading import Thread
import time
from PIL import Image,ImageTk
import RPi.GPIO as GPIO
import io
import sys
from subprocess import Popen
import os

RQS_0=0
RQS_QUIT=1
RQS_CAPTURE=2
rqs=RQS_0


             
root = Tkinter.Tk()
                         
HEIGHT = 1000
WIDTH = 1900
canvas = Tkinter.Canvas(root,height=HEIGHT,width=WIDTH).pack()

def camHandler():
    global rqs
    rqs = RQS_0
    
    camera = picamera.PiCamera()
    camera.video_stabilization = False
    camera.rotation = 270
    camera.crop = (0.0, 0.0, 1.0, 1.0)
    #camera.resolution = (1024, 768)
    #camera.resolution = (400, 300)
    text_file = open('/home/pi/water-meter/data.txt','a')

    while rqs != RQS_QUIT:
        if rqs == RQS_CAPTURE:
            #print("Capture")
            rqs=RQS_0
            timeStamp = time.strftime("%Y%m%d-%H%M")
            jpgFile='img_'+timeStamp+'.jpg'
            camera.resolution = (900, 500)    #set photo size
            camera.capture(jpgFile)
            #camera.resolution = (1280, 989)   #resume preview size
            labelCapVal.set(jpgFile)
            button.configure(text="Next",command=linkshow )
            rqs = RQS_QUIT
            text_file.write(jpgFile)
            text_file.close()

               

        else:
            stream = io.BytesIO()
            camera.capture(stream,format='jpeg')
            stream.seek(0)
            tmpImage = Image.open(stream)
            tmpimg = ImageTk.PhotoImage(tmpImage)
            frame.configure(image = tmpimg)
            frame.image = tmpimg
            
            #sleep(0.5)
                
   # print("Quit")        
    #camera.stop_preview()
    
    
    
def startCam():
    camThread = Thread(target=camHandler)
    camThread.start()
    

def capture():
    global rqs
    rqs = RQS_CAPTURE
    labelCapVal.set("capturing")
    
   

def linkshow():
    rqs = RQS_CAPTURE

    Popen(["python" , "guishow.py"])

    global root
    root.destroy()


f = Tkinter.Frame(root)
f.place(relx=0.5,rely=0.02,relwidth=0.8,relheight=0.8,anchor='n')

frame = Tkinter.Label(f)
frame.pack(side="bottom",fill="both",expand = "yes")

labelCapVal = Tkinter.StringVar()
Tkinter.Label(frame, textvariable=labelCapVal).pack()

button = Tkinter.Button(root,text="Capture", font=40, command=capture,background='DeepSkyblue3',foreground='white')
button.pack()         
button.place(relx=0.3, rely=0.6, relheight=0.3, relwidth=0.4)
 
#button = Tkinter.Button(root,text="yes", font=40, command=linkshow)
#button.pack()         
#button.place(relx=0.7, rely=0.85, relheight=0.1, relwidth=0.15)


startCam()
root.mainloop()
