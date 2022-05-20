import arcade
from  constants import *

def home_sprites(object):
    # Create the ground
    # This shows using a loop to place multiple sprites horizontally
    for x in range(-500, object.background.width + 300, 64):
        wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 32
        object.wall_list.append(wall)

    image_source = "pictures/tree.png"
    tree_sprite = arcade.Sprite(image_source, 0.28)
    tree_sprite.center_x = -200
    tree_sprite.center_y = 315
    tree_sprite.collision_radius = 80
    object.wall_list.append(tree_sprite)
    tree_sprite = arcade.Sprite(image_source, 0.28)
    tree_sprite.center_x = object.background.width
    tree_sprite.center_y = 315
    tree_sprite.collision_radius = 80
    object.wall_list.append(tree_sprite)

    image_source = "pictures/stair.png"
    object.stair_sprite = arcade.Sprite(image_source, 1.1)

    object.stair_sprite.center_x = 275 + 600
    object.stair_sprite.center_y = 142.5
    object.stair_sprite.alpha = 0
    object.coin_list.append(object.stair_sprite)

    sprite = arcade.Sprite(image_source, 1.1, hit_box_algorithm='Detailed')
    sprite.center_x = 275+ 600
    sprite.center_y = 142.5
    sprite.collision_radius = 1
    object.wall_list.append(sprite)

    image_source = "pictures/whiteboard.png"

    object.whiteboard_sprite = arcade.Sprite(image_source, 0.2,)
    object.whiteboard_sprite.center_x = 400
    object.whiteboard_sprite.center_y = 171
    object.whiteboard_sprite.collision_radius = 1
    object.coin_list.append(object.whiteboard_sprite)



def planet_sprites(object):

    # Create the ground
    # This shows using a loop to place multiple sprites horizontally
    for x in range(-400, 2000, 64):
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = x
        wall.center_y = 32
        object.wall_list.append(wall)

    # Create the left wall
    # This shows using a loop to place multiple sprites horizontally
    for y in range(-400, 5000, 64):
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = -150
        wall.center_y = y
        object.wall_list.append(wall)

    for y in range(-400, 5000, 64):
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = 1500
        wall.center_y = y
        object.wall_list.append(wall)

    if object.planet == 'sun':
        tiles = 'lava'
    elif object.planet == 'jupiter':
        tiles = 'sandCenter'
    elif object.planet == 'mars':
        tiles = 'sandCenter'
    else:
        tiles = 'dirtCenter'

    for x in range(800, 900, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 176
        object.wall_list.append(wall)

    for x in range(500, 1000, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 128
        object.wall_list.append(wall)

    for x in range(300, 1200, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 80
        object.wall_list.append(wall)

    for x in range(-500, 2000, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 32
        object.wall_list.append(wall)

    for x in range(0, 250, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        object.wall_list.append(wall)

    for x in range(600, 1000, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 700
        object.wall_list.append(wall)

    for x in range(0, 300, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 1600
        object.wall_list.append(wall)

    for x in range(800, 1200, 64):
        wall = arcade.Sprite(f":resources:images/tiles/{tiles}.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 1600
        object.wall_list.append(wall)

    object.planet_score[object.planet] = 0


    image_source = "pictures/coinGold.png"
    real_size = 0.75

    for tuple in PLANET_STAR_POSITIONS:
        sprite = arcade.Sprite(image_source, 1, hit_box_algorithm='Detailed')
        sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
        sprite.center_x = tuple[0]
        sprite.center_y = tuple[1]
        object.collect_coin_list.append(sprite)




    # image_source = "pictures/elephant.png"
    # real_size = 3.2
    # sprite = arcade.Sprite(image_source, 1, hit_box_algorithm='Detailed')
    # sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    # sprite.center_x = 700
    # sprite.center_y = 64 + sprite.height / 2
    # object.wall_list.append(sprite)
    #
    # image_source = "pictures/palme.png"
    # real_size = 12
    # sprite = arcade.Sprite(image_source, 1)
    # sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    # sprite.center_x = 1600
    # sprite.center_y = 64 + sprite.height / 2
    # object.wall_list.append(sprite)
    #
    # image_source = "pictures/hydrant.png"
    # real_size = 0.9
    # sprite = arcade.Sprite(image_source, 0.1)
    # sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    # sprite.center_x = 300
    # sprite.center_y = 64 + sprite.height / 2
    # sprite.collision_radius = 0
    # object.wall_list.append(sprite)
    #
    # image_source = "pictures/cake.png"
    # real_size = 0.3
    # sprite = arcade.Sprite(image_source, 0.1)
    # sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    # sprite.center_x = 100
    # sprite.center_y = 64 + sprite.height / 2
    # sprite.collision_radius = 100
    # object.wall_list.append(sprite)





def add_planets(object):

    center_x = 270 + 600
    center_y = 200

    image_source = "pictures/mars.png"
    object.mars_sprite = arcade.Sprite(image_source, 0.325)
    object.mars_sprite.center_x = center_x + 250
    object.mars_sprite.center_y = center_y
    object.coin_list.append(object.mars_sprite)

    image_source = "pictures/sun.png"
    object.sun_sprite = arcade.Sprite(image_source, 0.4)
    object.sun_sprite.center_x = center_x + 150
    object.sun_sprite.center_y = center_y +250
    object.coin_list.append(object.sun_sprite)


    image_source = "pictures/moon.png"
    object.moon_sprite = arcade.Sprite(image_source, 0.325)
    object.moon_sprite.center_x = center_x - 150
    object.moon_sprite.center_y = center_y +250
    object.coin_list.append(object.moon_sprite)


    image_source = "pictures/jupiter.png"
    object.jupiter_sprite = arcade.Sprite(image_source, 0.325)
    object.jupiter_sprite.center_x = center_x - 250
    object.jupiter_sprite.center_y = center_y
    object.coin_list.append(object.jupiter_sprite)

def text_sprites(object):
    object.in_conversation = True
    image_source = "pictures/professor.png"
    object.professor_sprite = arcade.Sprite(image_source, 0.6*PROFESSOR_SCALING)

    object.professor_sprite.center_x = 800+object.view_left + 150
    object.professor_sprite.center_y = 190
    object.text_list.append(object.professor_sprite)

    image_source = "pictures/bubble_rb.png"
    bubble_sprite = arcade.Sprite(image_source, 0.4 * PROFESSOR_SCALING)
    bubble_sprite.center_x = object.professor_sprite.center_x - 0.675 * bubble_sprite.width
    bubble_sprite.center_y = object.professor_sprite.center_y + 0.4 * bubble_sprite.height
    object.text_list.append(bubble_sprite)

