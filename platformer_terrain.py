"""
procedural terrain generation for platformer by Terapixel
addition credits: TheGreatRambler
"""

import pygame
import pygelt
import random

def return_terrain():
terrain_array = []
""" for loop for procedural terrain generation. """
for thing in range(0, 10):
  # Put random platforms in game - first two values is the width and height.
  elementtoconsider = [200, 5, random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)]
  
  addtoarray = true
  # makes sure the terrain doesn't collide with other terrain.
  for lengthindex in range(0, terrain_array.length):
    item = terrain_array[lengthindex]
    if (item[2] < elementtoconsider[2] and item[2] + item[0] > elementtoconsider[2] + elementtoconsider[0] and item[3] < elementtoconsider[3] and item[3] + item[1] > elementtoconsider[3] + elementtoconsider[1]):
      addtoarray = false
  if (addtoarray):
    terrain_array.append(elementtoconsider)
  
  return terrain_array

# call this in platformer_main.py
#return_terrain()
