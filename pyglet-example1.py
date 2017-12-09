import pyglet

mp3 = "Desafinado.mp3"

source = pyglet.media.load(mp3)
player = pyglet.media.Player()

player.queue(source)
player.play()

##music = pyglet.resource.media('Desafinado.mp3')
##music.play()

pyglet.app.run()
