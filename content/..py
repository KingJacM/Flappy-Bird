from tkinter import *
import random
import time
from PIL import Image, ImageTk
from classes import *
from time import monotonic as timer

root = Tk()
root.title("Flappy Bird")
canvas = Canvas(root, width=360, height=640)
canvas.pack()

image = Image.open('bg_5.png')
photo_image = ImageTk.PhotoImage(image)
game_background = canvas.create_image(180, 320, image = photo_image, anchor = 'c')
# finishes background


def change_background():
    image2 = Image.open('start_menu.png')
    photo2 = ImageTk.PhotoImage(image2)
    canvas.itemconfig(game_background, image=photo2)

button = Button(root, text = "", command=lambda: change_background())
button.pack()


root.mainloop()





