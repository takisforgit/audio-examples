# -*- coding: utf-8 -*-
"""
Spyder Editor

music_player_tutorial.py
"""

import os
import pygame
from mutagen.id3 import ID3
from tkinter import *
from tkinter.filedialog import askdirectory

listOfSongs = []
realNames = []
index = 0

def nextSong(event):
    global index, listOfSongs, realNames
    index += 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updateLabel()

def previousSong(event):
    global index, listOfSongs, realNames
    index -= 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updateLabel()

def stopSong(event):
     global index, listOfSongs, realNames
     pygame.mixer.music.stop()
     title.set("")
##     return songname

def updateLabel():
    global index, listOfSongs, realNames
    title.set(listOfSongs[index])
    myindex.set(index)
##    return songname
    

    
def chooseDirectory():
    mydir = askdirectory()
    os.chdir(mydir)

    for file in os.listdir(mydir):
        if file.endswith(".mp3"):
## get name of audio from metadata
            realdir = os.path.realpath(file)
            audio = ID3(realdir)
            realNames.append(audio['TIT2'].text[0])
            listOfSongs.append(file)
            print(file)
##    print(realNames)

# 1st time - FILENAMES in listbox
##    print(listOfSongs)
##    listOfSongs.reverse()
    for song in listOfSongs:
        listbox.insert(END,song)

# 2nd time - Tune names from ID tags in listbox
##realNames.reverse()
##for song in realNames:
##        listbox.insert(END,song)
##    
##updateLabel()

        
    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[0])
    pygame.mixer.music.play()
    updateLabel()
    


root = Tk()
root.minsize(500,400)
root.title("My Audio Player ( with Pygame & Mutagen modules )")
label =  Label(root, text="LIST OF TUNES")
label.pack()
listbox = Listbox(root,width=50,height=20,bg="light grey",fg="black", font="Arial 10")
listbox.pack()


next_button = Button(root, text="Next Song", )
next_button.pack()
previous_button = Button(root, text="Previous Song")
previous_button.pack()
stop_button= Button(root, text="STOP")
stop_button.pack()

## Click left mouse button on button image
next_button.bind("<Button-1>", nextSong) 
previous_button.bind("<Button-1>", previousSong) 
stop_button.bind("<Button-1>", stopSong) 
title=StringVar()
songLabel = Label(root, textvariable=title, width=35, font="Arial 12")
songLabel.pack(side="left")
myindex=StringVar()
songIndex = Label(root, textvariable=myindex, width=3, font="Arial 12")
songIndex.pack(side="left")


chooseDirectory()





root.mainloop()
