import pygame
f=12050
pygame.mixer.init(frequency=f)
ch1=pygame.mixer.Channel(0)
a=pygame.mixer.Sound(r"C:\Users\utkarsh kumar\Desktop\envisage\Ketsa_-_02_-_Seeing_You_Again.wav")
ch1.play(a)
