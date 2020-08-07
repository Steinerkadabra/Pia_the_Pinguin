import arcade
from  constants import *
import utils

def home(object):
    # Load the background image. Do this in the setup so we don't keep reloading it
    object.background = arcade.load_texture("pictures/back.jpg")

    # Used to keep track of our scrolling
    object.view_bottom = object.view_bottom
    object.view_left = object.view_left

    # Create the Sprite lists
    object.player_list = arcade.SpriteList()
    object.wall_list = arcade.SpriteList()
    object.coin_list = arcade.SpriteList()

    # Set up the player, specifically placing it at these coordinates.
    image_source = "pictures/player.png"
    object.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    object.player_sprite.center_x = 64
    object.player_sprite.center_y = 96
    object.player_list.append(object.player_sprite)


    image_source = "pictures/rocket.png"

    object.rocket_sprite = arcade.Sprite(image_source, 1.1, hit_box_algorithm='Detailed')

    object.rocket_sprite.center_x = 400
    object.rocket_sprite.center_y = 142
    object.rocket_sprite.collision_radius = 10
    object.wall_list.append(object.rocket_sprite)

    utils.home_sprites(object)
    # Create the 'physics engine'
    object.physics_engine = arcade.PhysicsEnginePlatformer(object.player_sprite,
                                                         object.wall_list,
                                                         GRAVITY)
    
def start_from_home(object):
    # Load the background image. Do this in the setup so we don't keep reloading it
    object.background = arcade.load_texture("pictures/back.jpg")

    # Used to keep track of our scrolling
    object.view_bottom = object.view_bottom
    object.view_left = object.view_left

    # Create the Sprite lists
    object.player_list = arcade.SpriteList()
    object.wall_list = arcade.SpriteList()
    object.coin_list = arcade.SpriteList()


    image_source = "pictures/rocket_flying.png"

    object.rocket_sprite = arcade.Sprite(image_source, 1.1, hit_box_algorithm='Detailed')

    object.rocket_sprite.center_x = 400
    object.rocket_sprite.center_y = 142
    object.rocket_sprite.change_y = ROCKET_SPEED
    object.rocket_sprite.collision_radius = 10
    object.wall_list.append(object.rocket_sprite)


    utils.home_sprites(object)

    # Create the 'physics engine'
    object.physics_engine = arcade.PhysicsEnginePlatformer(object.player_sprite,
                                                     object.wall_list,
                                                         GRAVITY)
def planet(object):
    # Load the background image. Do this in the setup so we don't keep reloading it
    try:
        object.background = arcade.load_texture(f"pictures/{object.planet}_bkg.png")
    except FileNotFoundError:
        object.background = arcade.load_texture(f"pictures/{object.planet}_bkg.jpg")

    # Used to keep track of our scrolling
    object.view_bottom = object.view_bottom
    object.view_left = object.view_left

    # Create the Sprite lists
    object.player_list = arcade.SpriteList()
    object.wall_list = arcade.SpriteList()
    object.coin_list = arcade.SpriteList()

    # Set up the player, specifically placing it at these coordinates.
    image_source = "pictures/player.png"
    object.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    object.player_sprite.center_x = 64
    object.player_sprite.center_y = 96
    object.player_list.append(object.player_sprite)

    utils.planet_sprites(object)
    # Create the 'physics engine'
    object.physics_engine = arcade.PhysicsEnginePlatformer(object.player_sprite,
                                                         object.wall_list,
                                                         GRAVITY *object.planet_gravity)