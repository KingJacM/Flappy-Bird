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
        self.coord = canvas.coords(self.id)
        self.y = 1 #speed is 3 down
        self.canvas.bind_all("<Key-Up>", self.up)  # bind up moving function with up key
        self.hit_bottom = False

    def fall(self):
        canvas.move(self.id, 0 ,self.y)
        pos = self.canvas.coords(
            self.id)  # this returns the coordinate[x1, y1, x2, y2] of "self id" and store it in a variable
        if pos[1] >= 590:
            self.hit_bottom = True  # if ball hits x=0, hit bottom is now true, note that self hit bottom can be used here
            canvas.create_text(250, 250, text="Game over", font="Times, 30")#simply creates text, no association with class
        return pos

    def up(self, event):
        self.y = -6

    def hit_bottom(self):
        pos = canvas.coords(self.id)
        print(pos)
        if pos[1] >= 0:
            return True







class Pipe:
    def __init__(self,canvas,x,y,x1,y1):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y,x1,y1, fill = "green")
    def move(self):
        canvas.move(self.id, -1 ,0)
        pos = self.canvas.coords(
            self.id)
        return pos

def create_pipes():
    pass


#test
bird = Bird(canvas)
pipe1 = Pipe(canvas, 360, 640, 290, 340)
pipe2 = Pipe(canvas, 360, 190, 290, 0)

score = 0
while True:

    if bird.hit_bottom == False:

        bird.y = bird.y + 0.2
        bird.fall()
        pipe1.move()
        pipe2.move()

    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()

#-------------------------------
