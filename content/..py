from tkinter import *
import random
import time
from PIL import Image, ImageTk
from classes import *
from time import monotonic as timer

# graphics

root = Tk()
root.title("Flappy Bird")
canvas = Canvas(root, width=360, height=640)
canvas.pack()
image = Image.open('bg_5.png')
photo_image = ImageTk.PhotoImage(image)
game_background = canvas.create_image(180, 320, image = photo_image, anchor = 'c')
# finishes background

#mfunctions that sets up the start screen
def start_screen():
    start_button = Button(root, text="start")
    start_button.pack()

#classes
class Bird:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(165, 305, 205, 345, fill = "yellow")
        self.x = 0
        self.y = 2
        self.canvas.bind_all("<Key-Up>", self.up)# bind up moving function with up key
        self.cord = canvas.coords(self.id)

    def up(self, event):  # use this to move up

        self.y = -3




    def move(self):  # to actually move the bird, this func gets activated
        canvas.move(self.id, self.x, self.y)
        pos = canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 640:
            self.y = 0
        for i in range (0,10):
            self.y += 0.0007



class Pipe:
    def __init__(self,canvas,x,y,x1,y1):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y,x1,y1, fill = "green")



bird = Bird(canvas)
# pipe1 = Pipe(canvas,360,640,290,340)
# pipe2 = Pipe(canvas,360,190,290,0)

def test_draw():

    x = 290
    y = random.randrange(100, 400)
    y1 = y+150
    pipe3 = Pipe(canvas, x, 0, 360, y)
    pipe4 = Pipe(canvas, 360, 640, x, y1)
    canvas.delete(pipe3)
    canvas.delete(pipe4)


start_screen()





while True:
    test_draw()
    bird.move()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()
