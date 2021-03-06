from Tkinter import *
from PIL import Image,ImageTk
from subprocess import Popen

root = Tk()
text = Text(root)
HEIGHT = 1000
WIDTH = 1900
canvas = Canvas(root,height=HEIGHT,width=WIDTH).pack()



def linkdatabase():
    import os
    Popen(["python3" , "upImage.py"])

    global root
    root.destroy()
    

labeltexttop = Label(root,text="Water Meter Camera", font='Helvetica 35 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.2,anchor='n')

i=0;
text_file = open('/home/pi/water-meter/nwdata.txt','r')
line = text_file.read().splitlines()    
textdate = line[i]
#textrfid = line[i+1]
textimage = line[i+1]
text_file.close()


photo = Image.open(textimage)
#photo.resize((5, 20), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
label = Label(root,image=img)
label.place(relx=0.3, rely=0.25,anchor='n')

keyframe = Frame(root, bg='#80c1ff', bd=10)
keyframe.place(relx=0.85, rely=0.35, relwidth=0.3, relheight=0.15, anchor='n')

uidlabel = Label(keyframe,foreground='DeepSkyblue3',text="Key Room = hhh ",font='Helvetica 16')
uidlabel.pack(side="bottom",fill="both",expand="yes")


dateframe = Frame(root, bg='#80c1ff', bd=10)
dateframe.place(relx=0.85, rely=0.55, relwidth=0.3, relheight=0.15, anchor='n')

timelabel = Label(dateframe,foreground='DeepSkyblue3',text="Date = ggg",font='Helvetica 16')
timelabel.pack(side="bottom",fill="both",expand="yes")



summitbtn= Button( root,text="SUMMIT", font='Helvetica 30' , background='DeepSkyblue3',foreground='white', command=linkdatabase)
summitbtn.place(relx=0.83, rely=0.83, relheight=0.15, relwidth=0.4)




root.mainloop()
