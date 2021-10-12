import pyglet
from pyglet.font import add_directory


caminho = 'fonts\digital-7.ttf'
fonte = pyglet.font.add_file(caminho)    


print(pyglet.font.add_file('fonts\digital-7.ttf'))
