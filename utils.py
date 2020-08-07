import arcade
from  constants import *

def home_sprites(object):
    # Create the ground
    # This shows using a loop to place multiple sprites horizontally
    for x in range(-400, object.background.width + 300, 64):
        wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 32
        object.wall_list.append(wall)

    image_source = "pictures/tree.png"
    tree_sprite = arcade.Sprite(image_source, 1.1)
    tree_sprite.center_x = -200
    tree_sprite.center_y = 315
    tree_sprite.collision_radius = 80
    object.wall_list.append(tree_sprite)
    tree_sprite = arcade.Sprite(image_source, 1.1)
    tree_sprite.center_x = object.background.width
    tree_sprite.center_y = 315
    tree_sprite.collision_radius = 80
    object.wall_list.append(tree_sprite)

    image_source = "pictures/stair.png"

    stair_sprite = arcade.Sprite(image_source, 1.1, hit_box_algorithm='Detailed')

    stair_sprite.center_x = 275
    stair_sprite.center_y = 142.5
    stair_sprite.collision_radius = 1
    object.wall_list.append(stair_sprite)
    
def planet_sprites(object):

    # Create the ground
    # This shows using a loop to place multiple sprites horizontally
    for x in range(-400, object.background.width + 300, 64):
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = x
        wall.center_y = 32
        object.wall_list.append(wall)

    # Create the ground
    # This shows using a loop to place multiple sprites horizontally
    for y in range(-400, object.background.width + 300, 64):
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = -200
        wall.center_y = y
        object.wall_list.append(wall)

    image_source = "pictures/elephant.png"
    real_size = 3.2
    sprite = arcade.Sprite(image_source, 1, hit_box_algorithm='Detailed')
    height = object.player_sprite.height
    factor = real_size * object.player_sprite.height / sprite.height
    # sprite.height = sprite.height*factor
    # sprite.width = sprite.width*factor
    sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    sprite.center_x = 700
    sprite.center_y = 64 + sprite.height / 2
    object.wall_list.append(sprite)

    image_source = "pictures/palme.png"
    real_size = 12
    sprite = arcade.Sprite(image_source, 1)
    height = object.player_sprite.height
    factor = real_size * object.player_sprite.height / sprite.height
    # sprite.height = sprite.height*factor
    # sprite.width = sprite.width*factor
    sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    sprite.center_x = 1600
    sprite.center_y = 64 + sprite.height / 2
    object.wall_list.append(sprite)

    image_source = "pictures/hydrant.png"
    real_size = 0.9
    sprite = arcade.Sprite(image_source, 0.1)
    height = object.player_sprite.height
    factor = real_size * object.player_sprite.height / sprite.height
    # sprite.height = sprite.height*factor
    # sprite.width = sprite.width*factor
    sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    sprite.center_x = 300
    sprite.center_y = 64 + sprite.height / 2
    sprite.collision_radius = 0
    object.wall_list.append(sprite)

    image_source = "pictures/cake.png"
    real_size = 0.3
    sprite = arcade.Sprite(image_source, 0.1)
    height = object.player_sprite.height
    factor = real_size * object.player_sprite.height / sprite.height
    # sprite.height = sprite.height*factor
    # sprite.width = sprite.width*factor
    sprite.scale = real_size * object.player_sprite.height / sprite.height * sprite.scale
    sprite.center_x = 100
    sprite.center_y = 64 + sprite.height / 2
    sprite.collision_radius = 100
    object.wall_list.append(sprite)

def add_planets(object):

    center_x = 270
    center_y = 200

    image_source = "pictures/mars.png"
    object.mars_sprite = arcade.Sprite(image_source, 0.5)
    object.mars_sprite.center_x = center_x + 250
    object.mars_sprite.center_y = center_y
    object.coin_list.append(object.mars_sprite)

    image_source = "pictures/sun.png"
    object.sun_sprite = arcade.Sprite(image_source, 0.5)
    object.sun_sprite.center_x = center_x + 150
    object.sun_sprite.center_y = center_y +250
    object.coin_list.append(object.sun_sprite)


    image_source = "pictures/moon.png"
    object.moon_sprite = arcade.Sprite(image_source, 0.475)
    object.moon_sprite.center_x = center_x - 150
    object.moon_sprite.center_y = center_y +250
    object.coin_list.append(object.moon_sprite)


    image_source = "pictures/jupiter.png"
    object.jupiter_sprite = arcade.Sprite(image_source, 0.45)
    object.jupiter_sprite.center_x = center_x - 250
    object.jupiter_sprite.center_y = center_y
    object.coin_list.append(object.jupiter_sprite)
