# import os
#  os.startfile('C:\\Users\\Manu\\Desktop\\09 - Cecília.mp3')

# from playsound import playsound
# playsound('cecilia.mp3')


from pygame import mixer

mixer.init()
mixer.music.load('cecilia.mp3')
mixer.music.play()

# pygame.event.wait()
# nome = input('Nome: ')
# print(nome)

import time

time.sleep(360)
