# -*- coding: utf-8 -*-
"""
Spyder Editor

music_player_tutorial.py
"""

import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory



def chooseDirectory():
    mydir = askdirectory()
    os.chdir(mydir)

    for file in os.listdir(mydir):
        if file.endswith(".mp3"):
            listOfSongs.append(file)
            print(file)



    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[0])
    pygame.mixer.music.play()



root = Tk()
root.minsize(500,400)
root.title("My Audio Player ( with Pygame & Mutagen modules )")

listOfSongs = []
index = 0

chooseDirectory()



root.mainloop()
