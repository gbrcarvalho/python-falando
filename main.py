"""
Fazendo o python falar
gTTS 2.3.2 
playsound 1.3.0
"""
import gtts
from playsound import playsound

with open("frase.txt", "r") as file:
    for linha in file:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save("frase.mp3")
        playsound("frase.mp3")
