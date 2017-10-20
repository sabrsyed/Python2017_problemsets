#!/usr/bin/env python3
#Python_05 question 2

file = open("../python_05.txt", "r")
file_write = open ("../Python_05_uc.txt", "w")

contents = file.read()
print (contents)

song_upper = contents.upper()
print (song_upper)

file_write.write(song_upper)

file.close()
file_write.close()
