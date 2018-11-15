
import os

for root, dirs, files in os.walk("."):  
    for filename in files:
        if filename[-3:] == "png":
            print(filename)
            tagurpidi_kaart_pilt = print(filename)
        