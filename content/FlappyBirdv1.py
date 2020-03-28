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
        self.id = canvas.create_oval(165, 305, 205, 345, fill = "yellow",outline="orange")
        self.coord = canvas.coords(self.id)
        self.y = 1 #speed is 3 down
        self.canvas.bind_all("<Key-Up>", self.up)  # bind up moving function with up key
        self.hit_bottom = False

    def fall(self):
        canvas.move(self.id, 0 ,self.y)
        self.pos = self.canvas.coords(
            self.id)  # this returns the coordinate[x1, y1, x2, y2] of "self id" and store it in a variable
        if self.pos[1] >= 590:
            self.hit_bottom = True  # if ball hits x=0, hit bottom is now true, note that self hit bottom can be used here
            canvas.create_text(250, 250, text="Game over", font="Times, 30")#simply creates text, no association with class

    def position(self):
        return self.fall()

    def up(self, event):
        self.y = -5

    def hit_bottom(self):
        pos = canvas.coords(self.id)
        print(pos)
        if pos[1] >= 0:
            return True







class Pipe:
    def __init__(self,canvas,x,y,x1,y1):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y,x1,y1, fill = "green",outline="green")
        self.pos = self.pos = self.canvas.coords(
            self.id)
    def move(self):
        canvas.move(self.id, -2 ,0)
        self.pos = self.canvas.coords(
            self.id)


def create_pipes():
    pass
#
# def check_overlap():
#     global pipe1, pipe2, bird
#     x1, y1, x2, y2 = pipe1.pos
#     x3,y3,x4,y4 = pipe2.pos
#     result = canvas.find_overlapping(x1, y1, x2, y2)
#     result2 = canvas.find_overlapping(x3, y3, x4, y4)
#     print(result)

#test
bird = Bird(canvas)
pipe1 = Pipe(canvas, 360, 640, 290, 340)
pipe2 = Pipe(canvas, 360, 190, 290, 0)
x1= 360+70
x2 = 290+70

score = 0
while True:

    if bird.hit_bottom == False:

        bird.y = bird.y + 0.2
        bird.fall()
        pipe1.move()
        pipe2.move()
        if  pipe1.pos[0] == -70:
            y1 = random.randrange(100,400)
            y2 = y1+150
            score += 1
            pipe1 = Pipe(canvas, x1, 640, x2, y2)
            pipe2 = Pipe(canvas, x1, y1,x2, 0)
        # x = pipe1.pos[0]
        # y = pipe1.pos[1]
        # x1 = pipe1.pos[2]
        # y1 = pipe1.pos[3]
        # x2 = pipe2.pos[0]
        # y2 = pipe2.pos[1]
        # x3 = pipe2.pos[2]
        # y3 = pipe2.pos[3]
        # print(x,y,x1,y1)






        # check_overlap()









    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()


