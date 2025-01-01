import os
import pygame

sprites = {}
audios = {}

def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))


def get_sprites(name):
    return sprites[name]

def load_audio():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name):
    audios[name].play()