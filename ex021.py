#fup que reproduza um arquivo mp3
from pygame import mixer
mixer.init()
mixer.music.load('msc.mp3.mp3')
mixer.music.play()
x = input('digite algo para parar..')