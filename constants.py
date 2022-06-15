
# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.055
CROSSHAIR_SCALING = 0.15
TILE_SCALING = 0.5
COIN_SCALING = 0.5
PROFESSOR_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
ROCKET_SPEED = 1

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
LEFT_MOVEMENT_MARGIN = 350
RIGHT_MOVEMENT_MARGIN = 350
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

PLANET_STAR_POSITIONS = [(-10, 140), (50, 140), (150, 140),(300, 170) ,(360, 170),(420,170) ,(480, 220)
                        ,(540, 220) ,(600, 220),(660, 220),(720, 220), (780, 270),(840, 270),(900, 270), (960, 220),
                        (1080, 170), (1140, 170),(1200, 170),(1260, 170),(0, 500),(90, 500),(180, 500),(620, 800)
                         , (680, 800),(740, 800),(800, 800),(860, 800),(920, 800), (980, 800), (0, 1700),
                        (80, 1700),(160, 1700),(240, 1700),(800, 1700),(880, 1700),(960, 1700),(1040, 1700),(1120, 1700),
                         (400, 350),(400, 550),(400, 750),(400, 950),(400, 1150),(400, 1350),(400, 1550),(400, 1750),
                         (400, 1950),(400, 2150),(400, 2350),(400, 2550),(400, 2750), (1400, 350),(1400, 550),(1400, 750)
                        ,(1400, 950),(1400, 1150),(1400, 1350),(1400, 1550),(1400, 1750)]
PLANET_SCORE_POSITIONS = {'moon': (695, 435), 'sun': (695, 515), 'jupiter': (310, 435), 'mars': (310, 515)}
TASK1_POSITION = (1050, 610)
CLASSIFICATION_SCORE_POSITION = (450, 265)
TASK2_POSITION = (1050, 330)
PLANET_VISIT_SCORE_POSITION = (450, 125)
TASK3_POSITION = (1050, 190)

PIC_PLANET_TILES_POSITIONS = [[(0, 0), (64, 0), (128, 0)], [(0, 0), (64, 0), (128, 0), (192, 0), (256, 0), (320, 0)],
                              [(0, 0),  (128, 0), (256, 0), (384, 0)], [(0, 0), (64, 0),(64, 64), (128, 0)],
                              [(0, 0), (64, 0),(64, 64),(64, -64), (128, 0)], [(0, 0), (0, 64), (0, 128)],
                              [(0, 0), (0, 64), (0, 128), (0, 192), (0, 256), (0, 320)], [(0, 0),  (0, 128), (0, 256), (0,384)],
                              [(0, 0)], [(0, 0), (64, 0), (64, 64)], [(0, 0), (64, 0), (64, 64), (128, 64), (128, 128), (128, 0)]]