#!/usr/bin/env python
import pymedia.audio.acodec as acodec
import pymedia.audio.sound as sound
import pymedia.muxer as muxer

file_name = 'thesong.ogg'
dm = muxer.Demuxer(str.split(file_name, '.')[-1].lower())
f = open(file_name, 'rb')
snd = dec = None
s = f.read( 32000 )
while len(s):
    frames = dm.parse(s)
    if frames:
        for fr in frames:
            if dec == None:
                dec = acodec.Decoder(dm.streams[fr[0]])

            r = dec.decode(fr[1])
            if r and r.data:
                if snd == None:
                    snd = sound.Output(
                        int(r.sample_rate),
                        r.channels,
                        sound.AFMT_S16_LE)
                data = r.data
                snd.play(data)
    s = f.read(512)

while snd.isPlaying():
    time.sleep(.05)
