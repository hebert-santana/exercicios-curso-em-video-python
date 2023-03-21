# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import os

# a versão do professor estava gerando erro porque o script não estava encontrando o mp3 no diretório
print(os.getcwd()) # mostra o diretório atual
# verifiquei o diretório e deixei o .mp3 no diretório que o script usa

pygame.mixer.init()

pygame.mixer.music.load('flowespacial.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue # voltar ao inicio do loop



