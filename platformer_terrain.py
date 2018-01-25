import pygame
import pygelt
import random

def return_terrain():
""" for loop for procedural terrain generation. """
terrain_array = []
for i in range(0, 10):
  # Put random platforms in game
  # level.append([random.randrange(100, 200), random.randrange(100, 200), random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)])
  # first two values is the width and height.
  terrain_array.append([200, 5, random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)])
  
  return terrain_array

# call this in platformer_main.py
#return_terrain()
