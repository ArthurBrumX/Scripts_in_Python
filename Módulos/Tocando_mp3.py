import pygame

pygame.init()
pygame.mixer.music.load('Tocando')
pygame.mixer.music.play()
pygame.event.wait()