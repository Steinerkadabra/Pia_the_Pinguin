import arcade
from  constants import *
import utils


def peer_review_feedback(object, input, true):
    object.coin_list = arcade.SpriteList()


    image_source = f'pictures/airmail.png'

    sprite = arcade.Sprite(image_source, 0.8)
    sprite.center_x = object.view_left + int(SCREEN_WIDTH / 2)
    sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT / 2)
    object.lightcurve_list.append(sprite)

    image_source = f'pictures/close.png'

    object.close_button = arcade.Sprite(image_source, 0.05)
    object.close_button.center_x = object.view_left + int(SCREEN_WIDTH / 2) -450
    object.close_button.center_y = object.view_bottom + int(SCREEN_HEIGHT / 2) + 240
    object.lightcurve_list.append(object.close_button)

    num_correct = 0

    pulsation_True = 'Uns wurde bestätigt, dass deine Klasifizierung als\n' + 'pulsierender Stern korrekt war! Du hast 50 Gold verdient!\n'
    pulsation_False = 'Uns wurde leider mitgeteilt dass deine Klasifizierung als\n' + 'pulsierender Stern nicht korrekt war! \n' + \
                       'Wir müssen deshalb leider 25 Gold abziehen!\n'

    spot_True = 'Super! Es handelt sich tatsächlich um einen Sternfleck!\n' + 'Du hast 10 Gold verdient!\n'
    spot_False = 'Der Sternfleck, den du in dieser Lichtkurve entdeckt hast\n' + 'konnte uns leider nicht bestätigt werden! \n' + \
                       'Wir müssen deshalb leider 5 Gold abziehen!\n'

    planet_True = 'Nach einreichender Kontrolle weltweiter Wissenschaftler hat sich\n' + 'herausgestellt das es sich tatsächlich um einen Planeten handelt!\n' +'Du hast 50 Gold verdient!\n'
    planet_False = 'Selbst nach intensiver Suche von mehreren Teams weltweit\n' + 'konnte der Planet leider nicht gefunden werden! \n' + \
                    'Wir müssen deshalb leider 25 Gold abziehen!\n'

    binary_True = 'Wow! Viele Teams beschäftigen sich bereits mit einer genaueren\n' + 'Analyse des von dir entdeckten Doppelsterns!\n' +'Du hast 30 Gold verdient!\n'
    binary_False = 'Wir müssen dir leider mitteilen, dass sich in dieser\n' + 'Lichtkurve kein Doppelstern versteckt! \n' + \
                    'Wir müssen deshalb leider 15 Gold abziehen!\n'

    none_correct = 'Auch kein Experte konnte ein Signal von Variabilität in der\n' + 'Lichtkurve erkennen! Du hast 10 Gold verdient!\n'
    none_False = 'Experten haben festgestellt, dass sich doch Variabilität in der\n' + 'Lichtkurve versteckt! Du hast deshalb leider kein Gold verdient!\n'

    object.peer_review_text = 'Liebe Pia,\n \n' + f'Danke für das einreichen deiner Analyse für PIC {int(object.telescope_stars_list[object.active_pic][0])}.\n'
    earned_money = 0
    moneys = [50, 10, 50, 30]
    for num, correct, not_correct in zip([0,1,2,3], [pulsation_True, spot_True,planet_True,binary_True], [pulsation_False, spot_False,planet_False,binary_False]):
        if input[num] == True and true[num] == 1:
            object.peer_review_text += correct
            num_correct += 1
            earned_money += moneys[num]
        elif input[num] == True and true[num] == 0:
            object.peer_review_text += not_correct
            earned_money -= moneys[num]/2

    if input == [False, False, False, False]:
        if max(true) == 0:
            object.peer_review_text += none_correct
            earned_money += 10
        else:
            object.peer_review_text += none_False
            earned_money -= 5



    if num_correct >0:
        additional_string = 'Übrigens: Die Lichtkurve zeigt auch das Signal '
    else:
        additional_string = 'Die Lichtkurve zeigt das Signal '

    names = ['von Pulsation', 'eines Sternflecks', 'eines Planeten', 'eines Doppelsterns']
    add = []
    for num in range(4):
        if input[num] == False and true[num] == 1:
            add.append(num)

    if add != []:
        if len(add) == 1:
            additional_string += names[add[0]]
        elif len(add) == 2:
            additional_string += names[add[0]]
            additional_string += ' und '
            additional_string += names[add[1]]
        elif len(add) == 3:
            additional_string += names[add[0]]
            additional_string += ', '
            additional_string += names[add[1]]
            additional_string += ' und '
            additional_string += names[add[2]]
        elif len(add) == 3:
            additional_string += names[add[0]]
            additional_string += ', '
            additional_string += names[add[1]]
            additional_string += ', '
            additional_string += names[add[2]]
            additional_string += ' und '
            additional_string += names[add[3]]
        additional_string += '.'
        object.peer_review_text += additional_string

    object.current_money += int(earned_money)





def active_lightcurve(object, PIC, kind = 'full'): # kind either 'full', 'hours', or 'days'
    object.lightcurve_list = arcade.SpriteList()




    image_source = f'pictures/stars/PIC_{int(PIC)}_{kind}.png'

    object.lightcurve_sprite = arcade.Sprite(image_source, 0.8)
    object.lightcurve_sprite.center_x = object.view_left + int(SCREEN_WIDTH / 2)
    object.lightcurve_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT / 2)
    object.lightcurve_list.append(object.lightcurve_sprite)
    object.lightcurve_active = True

    image_source = f'pictures/button_violett.png'
    object.full_button_sprite = arcade.Sprite(image_source, 0.2)
    object.full_button_sprite.center_x = object.view_left + int(SCREEN_WIDTH / 4)
    object.full_button_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT / 10)
    object.lightcurve_list.append(object.full_button_sprite)

    image_source = f'pictures/button_orange.png'
    object.days_button_sprite = arcade.Sprite(image_source, 0.2)
    object.days_button_sprite.center_x = object.view_left + int(SCREEN_WIDTH / 2)
    object.days_button_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT / 10)
    object.lightcurve_list.append(object.days_button_sprite)

    image_source = f'pictures/button_red.png'
    object.hours_button_sprite = arcade.Sprite(image_source, 0.2)
    object.hours_button_sprite.center_x = object.view_left + int(SCREEN_WIDTH *3/ 4)
    object.hours_button_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT / 10)
    object.lightcurve_list.append(object.hours_button_sprite)



    image_source = f'pictures/button_red.png'
    object.hours_button_sprite = arcade.Sprite(image_source, 0.2)
    object.hours_button_sprite.center_x = object.view_left + int(SCREEN_WIDTH *3/ 4)
    object.hours_button_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT / 10)
    object.lightcurve_list.append(object.hours_button_sprite)

    classification_names = ['pulsation', 'spot', 'planet', 'binary']
    for i in range(4):
        if object.classification_values[i]:
            image_source = f'pictures/button_green_{classification_names[i]}.png'
        else:
            image_source = f'pictures/button_black_{classification_names[i]}.png'
        object.classification_sprites[i] = arcade.Sprite(image_source, 0.25)
        object.classification_sprites[i].center_x = object.view_left + int(SCREEN_WIDTH * 11/ 12)
        object.classification_sprites[i].center_y = object.view_bottom + int(SCREEN_HEIGHT*(9-i)/10)
        object.lightcurve_list.append(object.classification_sprites[i])

    if object.telescope_stars_list[object.active_pic][-1] == 0:
        image_source = f'pictures/pigeon_letter.png'
    else:
        image_source = f'pictures/pigeon_letter_grey.png'

    object.send_results_sprite = arcade.Sprite(image_source, 0.2)
    object.send_results_sprite.center_x = object.view_left + int(SCREEN_WIDTH * 11/ 12)
    object.send_results_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT *2/5)
    object.lightcurve_list.append(object.send_results_sprite)



def telescope_view(object):

    object.background = arcade.load_texture("pictures/black_background.png")
    # object.in_conversation = True

    object.player_list = arcade.SpriteList()
    object.wall_list = arcade.SpriteList()
    object.coin_list = arcade.SpriteList()
    object.collect_coin_list = arcade.SpriteList()
    object.text_list = arcade.SpriteList()

    for x in range(-5200, 5200, 64):
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = x
        wall.center_y = 5200
        object.wall_list.append(wall)
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = x
        wall.center_y = -5200
        object.wall_list.append(wall)

    for y in range(-5200, 5200, 64):
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = 5200
        wall.center_y = y
        object.wall_list.append(wall)
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", TILE_SCALING)
        wall.alpha = 0
        wall.center_x = -5200
        wall.center_y = y
        object.wall_list.append(wall)


    image_source = "pictures/crosshair.png"
    object.player_sprite = arcade.Sprite(image_source, CROSSHAIR_SCALING)
    object.player_sprite.center_x = 64
    object.player_sprite.center_y = 96

    object.player_sprite.collision_radius = 0.0
    object.player_list.append(object.player_sprite)

    object.physics_engine = arcade.PhysicsEngineSimple(object.player_sprite,
                                                         object.wall_list)
    object.enable_physics = True

def starting_sequence(object):


    object.enable_physics = False

    object.in_conversation = True
    object.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    object.player_list = arcade.SpriteList()
    object.wall_list = arcade.SpriteList()
    object.coin_list = arcade.SpriteList()
    object.collect_coin_list = arcade.SpriteList()
    object.text_list = arcade.SpriteList()

    image_source = "pictures/professor.png"
    object.professor_sprite = arcade.Sprite(image_source, PROFESSOR_SCALING)

    object.professor_sprite.center_x = 950
    object.professor_sprite.center_y = 300
    object.text_list.append(object.professor_sprite)

    image_source = "pictures/bubble_rb.png"
    bubble_sprite = arcade.Sprite(image_source, 0.6*PROFESSOR_SCALING)
    bubble_sprite.center_x = object.professor_sprite.center_x - 0.7 * bubble_sprite.width
    bubble_sprite.center_y = object.professor_sprite.center_y + 0.35  * bubble_sprite.height
    object.text_list.append(bubble_sprite)

    object.text_strings = [
        'Hallo! \n Ich bin Petra \n die Professorin.', 'Ich möchte dir \n heute das Weltall und die \n Sterne etwas näher bringen. \n Bist du bereit?'
    ]


def home(object):
    # Load the background image. Do this in the setup so we don't keep reloading it
    object.background = arcade.load_texture("pictures/back.jpg")

    # Used to keep track of our scrolling
    object.view_bottom = 0
    object.view_left = -239

    # Create the Sprite lists
    object.player_list = arcade.SpriteList()
    object.wall_list = arcade.SpriteList()
    object.coin_list = arcade.SpriteList()
    object.collect_coin_list = arcade.SpriteList()
    object.text_list = arcade.SpriteList()


    # Set up the player, specifically placing it at these coordinates.
    image_source = "pictures/player.png"
    object.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    object.player_sprite.center_x = 64
    object.player_sprite.center_y = 96
    object.player_list.append(object.player_sprite)


    image_source = "pictures/rocket.png"

    object.rocket_sprite = arcade.Sprite(image_source, 1.1/4, hit_box_algorithm='None')

    object.rocket_sprite.center_x = 400 + 600
    object.rocket_sprite.center_y = 142
    object.rocket_sprite.collision_radius = 10
    object.wall_list.append(object.rocket_sprite)




    utils.home_sprites(object)
    if not object.home_conversation:
        object.home_conversation = True
        utils.text_sprites(object)
        object.text_strings = [
            'Das ist \n unsere Basis. \n Du bist Pia  \n der Pinguin!',
            'Du kannst dich mit\n mit den Pfeiltasten \n bewegen!',
            'Versuche, \n dich mittig auf \n die Leiter zu setzen!'
        ]

    # Create the 'physics engine'
    object.physics_engine = arcade.PhysicsEnginePlatformer(object.player_sprite,
                                                         object.wall_list,
                                                         GRAVITY)
    object.enable_physics = True


def whiteboard(object):
    # Load the background image. Do this in the setup so we don't keep reloading it
    object.background = arcade.load_texture("pictures/whiteboard_back.png")

    # Used to keep track of our scrolling


    # Create the Sprite lists
    object.player_list = arcade.SpriteList()
    object.wall_list = arcade.SpriteList()
    object.coin_list = arcade.SpriteList()
    object.collect_coin_list = arcade.SpriteList()
    object.text_list = arcade.SpriteList()


    planets_done = True
    for planet in ['mars', 'moon', 'jupiter', 'sun']:
        val = int(object.planet_score[planet])
        if val == 0:
            planets_done = False
        if val >=10:
            val1 = str(val)[0]
            val2 = str(val)[1]

            sprite1 = arcade.Sprite(f"pictures/digit_{val1}.png", 0.1)
            sprite1.center_x = PLANET_SCORE_POSITIONS[planet][0] - 20
            sprite1.center_y =  PLANET_SCORE_POSITIONS[planet][1]
            object.wall_list.append(sprite1)

            sprite2 = arcade.Sprite(f"pictures/digit_{val2}.png", 0.1)
            sprite2.center_x = PLANET_SCORE_POSITIONS[planet][0] + 20
            sprite2.center_y =  PLANET_SCORE_POSITIONS[planet][1]
            object.wall_list.append(sprite2)

        else:
            sprite1 = arcade.Sprite(f"pictures/digit_{val}.png", 0.1)
            sprite1.center_x = PLANET_SCORE_POSITIONS[planet][0]
            sprite1.center_y =  PLANET_SCORE_POSITIONS[planet][1]
            object.wall_list.append(sprite1)

    if planets_done:
        planets_done_sprite = arcade.Sprite(f"pictures/perfect.png", 0.1)
    else:
        planets_done_sprite = arcade.Sprite(f"pictures/cross.png", 0.1)

    planets_done_sprite.center_x = TASK1_POSITION[0]
    planets_done_sprite.center_y = TASK1_POSITION[1]
    object.wall_list.append(planets_done_sprite)



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
    object.collect_coin_list = arcade.SpriteList()
    object.text_list = arcade.SpriteList()


    image_source = "pictures/rocket_flying.png"

    object.rocket_sprite = arcade.Sprite(image_source, 1.1/5, hit_box_algorithm='None')

    object.rocket_sprite.center_x = 400 + 600
    object.rocket_sprite.center_y = 142
    object.rocket_sprite.change_y = ROCKET_SPEED
    object.rocket_sprite.collision_radius = 5
    object.wall_list.append(object.rocket_sprite)


    utils.home_sprites(object)

    # Create the 'physics engine'
    object.physics_engine = arcade.PhysicsEnginePlatformer(object.player_sprite,
                                                     object.wall_list,
                                                         GRAVITY)
    object.enable_physics = True


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
    object.collect_coin_list = arcade.SpriteList()
    object.text_list = arcade.SpriteList()

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
    object.enable_physics = True


def help(object):
    object.help_sprite_list = arcade.SpriteList()
    if object.place in ["home", "on_planet", "telescope_view"]:
        image_source = f"pictures/help_{object.place}.png"
    else:
        return


    object.help_sprit = arcade.Sprite(image_source, 0.5 )

    object.help_sprit.center_x = object.view_left + int(SCREEN_WIDTH / 2)
    object.help_sprit.center_y = object.view_bottom + int(SCREEN_HEIGHT / 2)
    object.help_sprite_list.append(object.help_sprit)
