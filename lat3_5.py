#----------------------
# PACKAGE
#----------------------
'''
Step by step : (hirarky spt pada slide module 3 hal 56)
1. Buat Folder Music
2. Buat Folder Playlist di dalam folder music
3. Buat file __init__.py dlm folder music
4. Buat Module di dalam folder playlist spt pada slide
5. Buat file __init__.py dlm playlist
'''

import Music.Playlist.Play as Play          # panggil module dalam paket satu per satu
import Music.Playlist.Pause as Pause        # panggil module dalam paket satu per satu
import Music.Playlist.Load as Load          # panggil module dalam paket satu per satu

Play.play('Digimon - Butterfly')
Pause.pause('Digimon - Butterfly')
Load.load('Digimon - Butterfly')

# Exercise (ada pada file main_game.py - panggil package di folder game - menu)
# Kembangkanlah modul game yang sudah dibuat sebelumnya menjadi package
# Package tersebut berupa folder yang memuat modul-modul terkait Hero, Item, Enemy, Area dan Rank
# Lalu import package game tersebut ke satu file python bernama main.py
