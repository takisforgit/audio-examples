# -*- coding: utf-8 -*-
"""
Spyder Editor
music_player_tutorial-V3.py
"""

import os
import pygame
from hsaudiotag import auto

import tkinter as tk
from tkinter.filedialog import askdirectory

listOfSongs = []
realNames = []
allinfo = []
index = 0
medium_font = "Arial 12 bold" 
normal_font = "Arial 12 "
button_font = "Consolas 11"
song_font = "Consolas 12"

def myVolumeDecrease(event):
     currentVol=pygame.mixer.music.get_volume()
     pygame.mixer.music.set_volume(currentVol-0.10)
     currentVol=pygame.mixer.music.get_volume()
#     print(currentVol)

def myVolumeIncrease(event):
     currentVol=pygame.mixer.music.get_volume()
     pygame.mixer.music.set_volume(currentVol+0.10)
     currentVol=pygame.mixer.music.get_volume()
#     print(currentVol)

def nextSong(event):
    global index, listOfSongs, realNames
    index += 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    listbox1.select_clear(0,tk.END)
    listbox1.select_set(index)
    updateLabels(index)

def previousSong(event):
    global index, listOfSongs, realNames
    index -= 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    listbox1.select_clear(0,tk.END)
    listbox1.select_set(index)
    updateLabels(index)

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


def updateLabels(TuneIndex):
    global index, listOfSongs, realNames, details,  allinfo, index

##    details.set("Album: {}".format(allinfo[TuneIndex][0]) +\
##                "\nArtist : {}".format(allinfo[TuneIndex][1]) +\
##                "\nTitle: {}".format(allinfo[TuneIndex][2])+\
##                "\nStyle: {}".format(allinfo[TuneIndex][3])+\
##                "\nYear: {}".format(str(allinfo[TuneIndex][4]))+\
##                "\nTrack No.: {}".format(allinfo[TuneIndex][5])+\
##                "\nDuration: {:3.2f}".format(float(allinfo[TuneIndex][6]/60.0))+\
##                "\nBitRate: {}Kbps".format(allinfo[TuneIndex][7])+\
##                "\nSize: {:3.2f}MB".format(allinfo[TuneIndex][8])\
##                )

    albumVar.set(allinfo[TuneIndex][0])
    artistVar.set(allinfo[TuneIndex][1])
    titleVar.set(allinfo[TuneIndex][2])
    styleVar.set(allinfo[TuneIndex][3])
    yearVar.set(allinfo[TuneIndex][4])
    trackVar.set(allinfo[TuneIndex][5])
    durationVar.set(allinfo[TuneIndex][6])
    bitrateVar.set(allinfo[TuneIndex][7])
    #sizeVar.set(allinfo[TuneIndex][8])
    
     
def chooseDirectory():
    global details , allinfo,  info
    mydir = askdirectory()
    os.chdir(mydir)

    # Iterate all mp3 files of Directory chosen
    for file in os.listdir(mydir):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            mydir=os.path.dirname(realdir)
##            print(mydir)
##            print(audio)
##            print(file)
            # Get hsaudiotag metadata tags from mp3 file
            myfile = auto.File(file)
            info = [ myfile.album, myfile.artist,  myfile.title, myfile.genre,\
                     myfile.year, myfile.track, myfile.duration, myfile.bitrate,\
                     myfile.size/1024/1000 ]
            allinfo.append(info)
            
            listOfSongs.append(file)

##    print(allinfo)
##    print(listOfSongs)
     
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
    updateLabels(0)


def listItemSelect(event):
    global index, listOfSongs, realNames, index
    # Note here that Tkinter passes an event object to onselect()
    index = listbox1.curselection()[0]
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    listbox1.select_clear(0,tk.END)
    listbox1.select_set(index)
    updateLabels(index)

## ---- MAIN Code ---------------##

root = tk.Tk()
root.wm_geometry("700x700+50+50")
root.title("My Audio Player ( with Pygame & Hsaudiotag modules )")

##frame1 =  tk.Frame(root)
##frame1.grid(row=0,column=0)
label =  tk.Label(root, text="LIST OF TUNES",  font="Arial 12 bold")
label.grid(row=0,column=0, columnspan=7)
listbox1 = tk.Listbox(root,width=75,height=20,bg="light grey",fg="black",\
                      font=song_font , activestyle="none", selectmode=tk.SINGLE )
listbox1.grid(row=1,column=0, columnspan=7)

# left mouse click on a list item to display selection
#6listbox1.bind("<Button-1>", get_item)
listbox1.bind('<<ListboxSelect>>', listItemSelect)
previous_button = tk.Button(root, text="PREVIOUS",  font=button_font)
previous_button.grid(row=2,column=0, sticky=tk.E+tk.W )
next_button = tk.Button(root, text="NEXT",   font=button_font)
next_button.grid(row=2,column=1, sticky=tk.E+tk.W )
pause_button = tk.Button(root, text="PAUSE",  font=button_font)
pause_button.grid(row=2,column=2,sticky=tk.E+tk.W )
resume_button = tk.Button(root, text="RESUME",  font=button_font)
resume_button.grid(row=2,column=3, sticky=tk.E+tk.W)
stop_button= tk.Button(root, text="STOP",  font=button_font)
stop_button.grid(row=2,column=4, sticky=tk.E+tk.W)
vol_button1 = tk.Button(root, text="Volume DOWN",  font=button_font)
vol_button1.grid(row=2,column=5, sticky=tk.E+tk.W)
vol_button2 = tk.Button(root, text="Volume UP",  font=button_font)
vol_button2.grid(row=2,column=6, sticky=tk.E+tk.W)

## ---- Click left mouse button on button image ---- #
next_button.bind("<Button-1>", nextSong)
previous_button.bind("<Button-1>", previousSong)
stop_button.bind("<Button-1>", stopSong)
pause_button.bind("<Button-1>", pauseSong)
resume_button.bind("<Button-1>", resumeSong)
vol_button1.bind("<Button-1>", myVolumeDecrease)
vol_button2.bind("<Button-1>", myVolumeIncrease)

##frame2 =  tk.Frame(root, bg="light grey" ,  width=350)
##frame2.pack(side="top", expand=False )
label2 = tk.Label(root, text="Now Playing", font="Arial 12 bold",\
                  bg="green", fg="white" )
label2.grid(row=3,column=0, columnspan=7,  sticky=tk.E+tk.W )

##frame3 =  tk.Frame(frame2, width=30)
##frame3.pack(side="top", padx = 5 , pady = 5  )
details = tk.StringVar()
##label3 = tk.Label(frame3, textvariable=details,
##                  font="Consolas 12 bold" ,bg="#2B81BA",fg="black")
##label3.pack(side="bottom")

## Create labels and text widgets for MP3 TAGS
albumVar= tk.StringVar()
album_lbl =  tk.Label(root, text="Album     " , font=button_font, bg="light blue" , fg="black")
album_lbl.grid(row=4, column=0, columnspan=1 , sticky=tk.N+tk.S+tk.W,  )
album_txt =  tk.Label(root, textvariable=albumVar, font=button_font,\
                      fg="black")
album_txt.grid(row=4, column=1, columnspan=6 ,sticky=tk.N+tk.S+tk.W )

artistVar= tk.StringVar()
artist_lbl =  tk.Label(root, text="Artist    " ,font=button_font, bg="light blue" ,fg="black")
artist_lbl.grid(row=5, column=0, columnspan=1 , sticky=tk.W)
artist_txt =  tk.Label(root, textvariable=artistVar, font=button_font,\
                      fg="black")
artist_txt.grid(row=5,column=1, columnspan=6,sticky=tk.N+tk.S+tk.W )

titleVar= tk.StringVar()
title_lbl =  tk.Label(root, text="Tune      " ,font=button_font, bg="light blue" , fg="black")
title_lbl.grid(row=6, column=0, columnspan=1, sticky=tk.W)
title_txt =  tk.Label(root, textvariable=titleVar, font=button_font,\
                      fg="black")
title_txt.grid(row=6, column=1, columnspan=6,sticky=tk.N+tk.S+tk.W )

styleVar= tk.StringVar()
style_lbl =  tk.Label(root, text="Style     " ,font=button_font,  bg="light blue" ,fg="black")
style_lbl.grid(row=7, column=0, columnspan=1, sticky=tk.W)
style_txt =  tk.Label(root, textvariable=styleVar, font=button_font,\
                      fg="black")
style_txt.grid(row=7, column=1, columnspan=6,sticky=tk.N+tk.S+tk.W )

yearVar= tk.StringVar()
year_lbl =  tk.Label(root, text="Year      " ,font=button_font,  bg="light blue" ,fg="black")
year_lbl.grid(row=8, column=0, columnspan=1, sticky=tk.W)
year_txt =  tk.Label(root, textvariable=yearVar, font=button_font,\
                      fg="black")
year_txt.grid(row=8, column=1, columnspan=6,sticky=tk.N+tk.S+tk.W )

trackVar = tk.StringVar()
track_lbl =  tk.Label(root, text="Track     " ,font=button_font, bg="light blue" ,fg="black")
track_lbl.grid(row=9, column=0, columnspan=1, sticky=tk.W)
track_txt =  tk.Label(root, textvariable=trackVar , font=button_font,\
                      fg="black")
track_txt.grid(row=9, column=1, columnspan=6,sticky=tk.N+tk.S+tk.W )


durationVar= tk.StringVar()
duration_lbl =  tk.Label(root, text="Duration  " ,font=button_font, bg="light blue" ,fg="black")
duration_lbl.grid(row=10, column=0, columnspan=1, sticky=tk.W)
duration_txt =  tk.Label(root, textvariable=durationVar , font=button_font,\
                      fg="black")
duration_txt.grid(row=10, column=1, columnspan=6,sticky=tk.N+tk.S+tk.W )

bitrateVar= tk.StringVar()
bitrate_lbl =  tk.Label(root, text="BitRate   " ,font=button_font, bg="light blue" , fg="black")
bitrate_lbl.grid(row=11, column=0, columnspan=1, sticky=tk.W)
bitrate_txt =  tk.Label(root, textvariable=bitrateVar , font=button_font,\
                      fg="black")
bitrate_txt.grid(row=11, column=1, columnspan=6,sticky=tk.N+tk.S+tk.W )


chooseDirectory()
pygame.mixer.music.set_volume(0.3)
root.mainloop()

