import pygame
import time

pygame.mixer.init(frequency=42050)
ch1=pygame.mixer.Channel(0)
a=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav")
ch1.play(a)
pygame.mixer.pause()

pygame.mixer.unpause()


