# -*- coding: utf-8 -*-
"""
Spyder Editor

music_player_tutorial.py
"""

import os
import pygame
from mutagen.id3 import ID3, TLEN
from mutagen import Tags
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

import tkinter as tk
from tkinter.filedialog import askdirectory

listOfSongs = []
realNames = []
allinfo = []
allinfo2 = []
allinfo3 = []
info3= []
index = 0


def myVolumeDecrease(event):
     currentVol=pygame.mixer.music.get_volume()
     pygame.mixer.music.set_volume(currentVol-0.05)
     currentVol=pygame.mixer.music.get_volume()
#     print(currentVol)

def myVolumeIncrease(event):
     currentVol=pygame.mixer.music.get_volume()
     pygame.mixer.music.set_volume(currentVol+0.05)
     currentVol=pygame.mixer.music.get_volume()
#     print(currentVol)

def nextSong(event):
    global index, listOfSongs, realNames
    index += 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    listbox1.select_clear(0,tk.END)
    listbox1.select_set(index)
    updateLabels()

def previousSong(event):
    global index, listOfSongs, realNames
    index -= 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    listbox1.select_clear(0,tk.END)
    listbox1.select_set(index)
    updateLabels()

def pauseSong(event):
     global index, listOfSongs, realNames
     pygame.mixer.music.pause()

def resumeSong(event):
     global index, listOfSongs, realNames
     pygame.mixer.music.unpause()


def playSong(event):
     global index, listOfSongs, realNames
     pygame.mixer.music.play()
     updateLabels()


def stopSong(event):
     global index, listOfSongs, realNames
     pygame.mixer.music.stop()
     pygame.mixer.music.set_volume(0.5)


def updateLabels():
    global index, listOfSongs, realNames, details,  allinfo


    details.set("Album: "+allinfo[index][3] +
                "\nArtist : "+allinfo[index][1] +
                "\nTitle : "+allinfo[index][0]+
                "\nTrack No. : "+ allinfo[index][2]  +
                "\nDuration : %5.2f"%(float(allinfo[index][4])/60000)+
                "\nFile Location: " + str(allinfo[index][5])
                )
#    print(allinfo[index])

def chooseDirectory():
    global details , allinfo,  info
    mydir = askdirectory()
    os.chdir(mydir)

    for file in os.listdir(mydir):
        if file.endswith(".mp3"):
## ----- get name of audio from metadata  ----- ##
            realdir = os.path.realpath(file)
            mydir=os.path.dirname(realdir)
            print(mydir)
            audio = ID3(realdir)
            print(audio)
            info = [ audio['TIT2'].text[0], audio['TPE1'].text[0], audio['TRCK'].text[0], audio['TALB'].text[0],audio['TLEN'].text[0], mydir ]

            allinfo.append(info)
            listOfSongs.append(file)


## ---- 1st time - FILENAMES in listbox ---- ##
#    listOfSongs.reverse()

#    print(allinfo)
#    print(listOfSongs)
    for song in listOfSongs:
        listbox1.insert(tk.END , song)

## ---- 2nd time - Tune names from ID tags in listbox ---- ##
##for song in realNames:
##        tk.Listbox.insert(tk.END ,song)

    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[0])
    pygame.mixer.music.play()
    listbox1.select_set(0)
    updateLabels()


def listItemSelect(event):
    global index, listOfSongs, realNames
    # Note here that Tkinter passes an event object to onselect()
    index = listbox1.curselection()[0]
#    print(index)
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    listbox1.select_clear(0,tk.END)
    listbox1.select_set(index)
    updateLabels()




## ---- MAIN Code ---------------##

root = tk.Tk()
root.minsize(700,500)
root.title("My Audio Player ( with Pygame & Mutagen modules )")

frame1 =  tk.Frame(root)
frame1.pack(side="top")
label =  tk.Label(frame1, text="LIST OF TUNES")
label.pack()
listbox1 = tk.Listbox(frame1,width=70,height=30,bg="light grey",fg="black", font="Arial 10", activestyle="none", selectmode=tk.SINGLE )
listbox1.pack( fill="x" )

# left mouse click on a list item to display selection
#6listbox1.bind("<Button-1>", get_item)
listbox1.bind('<<ListboxSelect>>', listItemSelect)

previous_button = tk.Button(frame1, text="PREV")
previous_button.pack(side="left")

next_button = tk.Button(frame1, text="NEXT", )
next_button.pack(side="left")



pause_button = tk.Button(frame1, text="PAUSE")
pause_button.pack(side="left")
resume_button = tk.Button(frame1, text="RESUME")
resume_button.pack(side="left")
stop_button= tk.Button(frame1, text="STOP")
stop_button.pack(side="left")
vol_button1 = tk.Button(frame1, text="Volume DOWN")
vol_button1.pack(side="left")
vol_button2 = tk.Button(frame1, text="Volume UP")
vol_button2.pack(side="left")




## ---- Click left mouse button on button image ---- #
next_button.bind("<Button-1>", nextSong)
previous_button.bind("<Button-1>", previousSong)
stop_button.bind("<Button-1>", stopSong)
pause_button.bind("<Button-1>", pauseSong)
resume_button.bind("<Button-1>", resumeSong)
vol_button1.bind("<Button-1>", myVolumeDecrease)
vol_button2.bind("<Button-1>", myVolumeIncrease)



frame2 =  tk.Frame(root, bg="light grey" ,  width=350)
frame2.pack(side="bottom", fill="x" )
label2 = tk.Label(frame2, text="Now Playing", font="Arial 12",  bg="green", fg="white" )
label2.pack()

frame3 =  tk.Frame(frame2,  bg="yellow", height=150 )
frame3.pack(side="bottom", padx = 1 , pady = 1  )
details = tk.StringVar()
label3 = tk.Label(frame3, textvariable=details, width=70, font="Consolas 12" ,bg="#2B81BA",fg="black")


label3.pack(side="bottom",  fill="x" , expand=1)


chooseDirectory()
pygame.mixer.music.set_volume(0.5)

root.mainloop()
