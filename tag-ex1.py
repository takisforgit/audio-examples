from hsaudiotag import auto

##mymp3= 'Narthis.mp3'
mymp3='Desafinado.mp3'


myfile = auto.File(mymp3)
print("MP3 tags of: '{}'\n".format(mymp3))
print("Artist   :",myfile.artist)
print("Album    :",myfile.album)
print("Title    :",myfile.title)
print("Style    :",myfile.genre)
print("Year     :",myfile.year)
print("Track    :",myfile.track)
print("Duration : {:3.2f} (mins.secs)".format(myfile.duration/60.0))
print("BitRate  : {} Kbps".format(myfile.bitrate))
print("Size     : {:3.2f} Mb".format(myfile.size/1024/1000))
print("AudioSize: {:3.2f} Mb".format(myfile.audio_size/1024/1000))

##print(type(myfile.artist))
