""" for loop for procedural terrain generation. """
for i in range(0, 10):
  # Put random platforms in game
  # level.append([random.randrange(100, 200), random.randrange(100, 200), random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)])
  # first two values is the width and height.
  level.append([200, 5, random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)])
  level.append([200, 5, random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)])
  level.append([200, 5, random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)])
  level.append([200, 5, random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)])
