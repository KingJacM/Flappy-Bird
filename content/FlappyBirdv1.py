from tkinter import *
import random
import time
from PIL import Image, ImageTk
from classes import *
from time import monotonic as timer

# graphics: create canvas and background

root = Tk()
root.title("Flappy Bird")
canvas = Canvas(root, width=360, height=640)
canvas.pack()
image = Image.open('bg_5.png')
photo_image = ImageTk.PhotoImage(image)
game_background = canvas.create_image(180, 320, image = photo_image, anchor = 'c')
# finishes background


#classes
class Bird:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(165, 305, 205, 345, fill = "yellow")



class Pipe:
    def __init__(self,canvas,x,y,x1,y1):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y,x1,y1, fill = "green")


#test
bird = Bird(canvas)
pipe1 = Pipe(canvas,360,640,290,340)
pipe2 = Pipe(canvas,360,190,290,0)


while True:

    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()
