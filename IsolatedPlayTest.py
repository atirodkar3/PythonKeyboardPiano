import pyglet
song = pyglet.resource.media('g.wav', streaming = False)
win = pyglet.window.Window()
song.play()
pyglet.app.run()
pyglet.app.exit()
