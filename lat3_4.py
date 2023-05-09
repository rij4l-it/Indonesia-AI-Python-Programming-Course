#------------------------------
# MODULE
#------------------------------
# link build in module in python : https://docs.python.org/3/py-modindex.html

import playlist                         # file ada di folder yg sama bernama playlist.py

playlist.play('Digimon - Butterfly')


import playlist as pl                   # import file nama file di ubah / alias jadi pl

pl.play("Naruto - Flow")
pl.pause("Naruto - Flow")

print(pl.GENRE)                         # memanggil variable


#from playlist import *                      # import semua variable
from playlist import GENRE, DURATION, TYPE  # import spesifik variable bertujuan utk meringankan proses agar tidak terlalu berat
print(DURATION)
print(TYPE)


#build in module
import os
import math

from math import pi
from math import pi, e
from math import *

print("Nilai pi adalah", math.pi)

print()
# Exercise
# Buatlah sebuah modul game
# Modul tersebut memiliki fungsi terkait Hero, Item, Enemy, Area dan Rank
# Lalu import modul game tersebut ke satu file python bernama main.py

import game
game.Hero("Nama Hero")
game.Item("Pilihan Item")
game.Enemy("Nama Enemy")
game.Area("Pilihan Area")
game.Rank("Pilihan Rank")

