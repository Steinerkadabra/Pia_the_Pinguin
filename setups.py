import arcade
from  constants import *
import utils
from random import randrange


def james_webb_report(object):
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


    cold_True = 'Auf dem Planeten ist es so kalt, dass ein\n' + 'Kälteschutz unbedingt nötig ist!\n'

    gas_True = 'Es sieht so aus, als ob sich sehr viel Giftas\n' + 'auf dem Planeten befinden! Fahr bitte nur mit\n' + 'einer entsprechenden Gasmaske hin!\n'

    hot_True = 'Wir wissen nicht genau wie heiß es auf\n' + 'dem Planeten ist, aber flieg bitte nicht ohne\n' +'Wärmeschutz hin!\n'



    none_True = 'Für diesen Planeten ist keine besonderen\n' + 'Schutzausrüstung notwendig!\n'

    no_planet = 'In diesem Sternsystem befindet sich kein Planet.\n'

    object.peer_review_text = 'Liebe Pia,\n \n' + f'Das Kaiserpinguinen Teleskop hat sich PIC {int(object.telescope_stars_list[object.active_pic][0])} genau angesehen.\n'
    all_False = True
    if int(object.telescope_stars_list[object.active_pic][13]) == 1:
        object.peer_review_text += gas_True
        all_False = False
    if int(object.telescope_stars_list[object.active_pic][14]) == 1:
        object.peer_review_text += cold_True
        all_False = False
    if int(object.telescope_stars_list[object.active_pic][15]) == 1:
        object.peer_review_text += hot_True
        all_False = False


    if all_False and object.telescope_stars_list[object.active_pic][10] in [1, 2,3, 4, 5]:
        object.peer_review_text += none_True

    if object.telescope_stars_list[object.active_pic][10] ==0:
        object.peer_review_text += no_planet



    object.peer_review_text += '\n' + 'Diese Untersuchung hat 50 Gold gekostet!\n'
    object.current_money -= 50






def go_to_planet_menu(object):
    object.coin_list = arcade.SpriteList()

    image_source = f'pictures/exoplanet_visit_start.png'

    sprite = arcade.Sprite(image_source, 0.8)
    sprite.center_x = object.view_left + int(SCREEN_WIDTH / 2)
    sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT / 2)
    object.lightcurve_list.append(sprite)

    image_source = f'pictures/close.png'

    object.close_button = arcade.Sprite(image_source, 0.05)
    object.close_button.center_x = object.view_left + int(SCREEN_WIDTH / 2) -450
    object.close_button.center_y = object.view_bottom + int(SCREEN_HEIGHT / 2) + 240
    object.lightcurve_list.append(object.close_button)

    hazard_names = ['gas_mask', 'cold', 'hot']
    for i in range(3):
        if object.safety_hazard[i]:
            image_source = f'pictures/hazard_colour_{hazard_names[i]}.png'
        else:
            image_source = f'pictures/hazard_black_{hazard_names[i]}.png'
        object.safety_hazard_sprites[i] = arcade.Sprite(image_source, 0.085)
        object.safety_hazard_sprites[i].center_x = object.view_left + int(SCREEN_WIDTH *2.75/10)+ int(SCREEN_WIDTH*i/4.3)
        object.safety_hazard_sprites[i].center_y = object.view_bottom + int(SCREEN_HEIGHT*(11)/20)
        object.lightcurve_list.append(object.safety_hazard_sprites[i])

    image_source = f'pictures/rocket.png'

    object.visit_exoplanet_launch_sprite = arcade.Sprite(image_source, 0.075)
    object.visit_exoplanet_launch_sprite.center_x = object.view_left + int(SCREEN_WIDTH * 8/ 12)
    object.visit_exoplanet_launch_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT *0.8/3)
    object.lightcurve_list.append(object.visit_exoplanet_launch_sprite)


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

    pulsation_True = 'Uns wurde bestätigt, dass deine Klassifizierung als\n' + 'pulsierender Stern korrekt war! Du hast 50 Gold verdient!\n'
    pulsation_False = 'Uns wurde leider mitgeteilt dass deine Klassifizierung als\n' + 'pulsierender Stern nicht korrekt war! \n' + \
                       'Wir müssen deshalb leider 25 Gold abziehen!\n'

    spot_True = 'Super! Es handelt sich tatsächlich um einen Sternfleck!\n' + 'Du hast 10 Gold verdient!\n'
    spot_False = 'Der Sternfleck, den du in dieser Lichtkurve entdeckt hast\n' + 'konnte uns leider nicht bestätigt werden! \n' + \
                       'Wir müssen deshalb leider 5 Gold abziehen!\n'

    planet_True = 'Nach einreichender Kontrolle weltweiter Wissenschaftler hat sich\n' + 'herausgestellt das es sich tatsächlich um einen Exoplaneten handelt!\n' +'Du hast 50 Gold verdient!\n'
    planet_False = 'Selbst nach intensiver Suche von mehreren Teams weltweit\n' + 'konnte der Exoplanet leider nicht gefunden werden! \n' + \
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
        if input[num] == True and true[num] > 0:
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
        additional_string = 'Übrigens: Die Lichtkurve zeigt auch das Signal \n'
    else:
        additional_string = 'Die Lichtkurve zeigt das Signal \n'

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

    object.money_earned_from_classificiation += int(earned_money)

    object.last_peer_review_money =  int(earned_money)





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

    if object.telescope_stars_list[object.active_pic][9] == 0:
        image_source = f'pictures/pigeon_letter.png'
    else:
        image_source = f'pictures/pigeon_letter_grey.png'

    object.send_results_sprite = arcade.Sprite(image_source, 0.2)
    object.send_results_sprite.center_x = object.view_left + int(SCREEN_WIDTH * 11/ 12)
    object.send_results_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT *2/5)
    object.lightcurve_list.append(object.send_results_sprite)

    if object.telescope_stars_list[object.active_pic][12] == 0:
        image_source = f'pictures/rocket.png'
    else:
        image_source = f'pictures/rocket_grey.png'

    object.go_to_planet_visit_sprite = arcade.Sprite(image_source, 0.1)
    object.go_to_planet_visit_sprite.center_x = object.view_left + int(SCREEN_WIDTH * 1/ 12)
    object.go_to_planet_visit_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT *2/5)
    object.lightcurve_list.append(object.go_to_planet_visit_sprite)


    if object.telescope_stars_list[object.active_pic][9] == 1:
        image_source = f'pictures/james_webb.png'
    else:
        image_source = f'pictures/james_webb_grey.png'

    object.james_webb_sprite = arcade.Sprite(image_source, 0.1)
    object.james_webb_sprite.center_x = object.view_left + int(SCREEN_WIDTH * 1/ 12)
    object.james_webb_sprite.center_y = object.view_bottom + int(SCREEN_HEIGHT *3/4)
    object.lightcurve_list.append(object.james_webb_sprite)



def telescope_view(object):

    object.information_string = 'Spieldesign: Universität Innsbruck'


    # if object.last_telescope_view_bottom > -10000:
    #     object.view_bottom = self.last_telescope_view_bottom
    #     object.view_left = self.last_telescope_view_left

    print(int(object.last_telescope_view_left), int(object.last_telescope_view_bottom))
    arcade.set_viewport(0,
                        SCREEN_WIDTH,
                        0,
                        SCREEN_HEIGHT)

    object.choose_planet = False
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
    object.player_sprite.center_x = 64 + int(object.last_telescope_view_left)
    object.player_sprite.center_y = 96 + int(object.last_telescope_view_bottom)

    object.player_sprite.collision_radius = 0.0
    object.player_list.append(object.player_sprite)

    if not object.telescope_view_conversation:
        utils.text_sprites(object)
        object.text_strings = [
            'So sieht der \n Nachthimmel durch unser  \n Teleskop aus!',
            'Mit den Pfeiltasten \n kannst du dein Ziel \n bewegen!',
            'Wenn du auf einen \n Stern zielst, kannst du \n ihn genauer studieren!',
        ]
        object.telescope_view_conversation = True



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
    object.information_string = 'Spieldesign: Universität Innsbruck, Pinguin Design: Daniela Kurzböck'

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
    object.rocket_sprite.collision_radius = 0.1
    object.wall_list.append(object.rocket_sprite)




    utils.home_sprites(object)
    if not object.home_conversation:
        object.home_conversation = True
        utils.text_sprites(object)
        object.text_strings = [
            'Das ist \n unsere Basis. \n Du bist Pia  \n der Pinguin!',
            'Du kannst dich mit\n mit den Pfeiltasten \n bewegen!',
            'Mit der ESC\n  Taste kommst du jederzeit\n  hierher züruck!',
            'Versuche, \n dich mittig auf \n die Leiter zu setzen!'
        ]
    elif object.return_from_planet_visit:
        utils.text_sprites(object)
        if object.return_reason == 1:
            print("this happens")
            object.text_strings = [
                'OJEEE!',
                'Bei diesem \n Stern ware leider \n gar kein Planet!',
                'Du bist umsonst  \n dorthin geflogen!'
            ]
        elif object.return_reason == 2:
            print("this happens")
            object.text_strings = [
                'Hust Hust Hust!',
                'Der Planet, \n den du besuchen wolltest \n ist leider voller Giftgas!',
                'Du kannst nur  \n mit einer Gasmaske\n darauf landen!'
            ]
        elif object.return_reason == 3:
            print("this happens")
            object.text_strings = [
                'BRRRR!',
                'Der Planet \n den du besuchen wolltest \n ist leider viel zu kalt!',
                'Du kannst nur  \n mit Kälteschutz\n darauf landen!'
            ]
        elif object.return_reason == 4:
            print("this happens")
            object.text_strings = [
                'AUA!',
                'Der Planet \n den du besuchen wolltest \n ist leider viel zu heiss!',
                'Du kannst nur  \n mit Wärmeschutz\n darauf landen!'
            ]
    object.return_from_planet_visit = False
    object.return_reason = 0
    # Create the 'physics engine'
    object.physics_engine = arcade.PhysicsEnginePlatformer(object.player_sprite,
                                                         object.wall_list,
                                                         GRAVITY)
    object.enable_physics = True


def whiteboard(object):
    # Load the background image. Do this in the setup so we don't keep reloading it
    object.background = arcade.load_texture("pictures/whiteboard_back.png")

    object.information_string = 'Spieldesign: Universität Innsbruck'
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


    classification_done = False
    val = object.money_earned_from_classificiation
    if val > 0:
        classification_done = True
    vals = []

    got_nan = False
    i = 0
    while got_nan == False:
        try:
            vals.append(str(val)[i])
        except IndexError:
            got_nan = True
        i = i+1
    i = 0
    for digit in vals:
        sprite1 = arcade.Sprite(f"pictures/digit_{digit}.png", 0.1)
        sprite1.center_x = CLASSIFICATION_SCORE_POSITION[0] + i*40
        sprite1.center_y = CLASSIFICATION_SCORE_POSITION[1]
        object.wall_list.append(sprite1)
        i = i + 1

    if classification_done:
        classification_done_sprite = arcade.Sprite(f"pictures/perfect.png", 0.1)
    else:
        classification_done_sprite = arcade.Sprite(f"pictures/cross.png", 0.1)

    classification_done_sprite.center_x = TASK2_POSITION[0]
    classification_done_sprite.center_y = TASK2_POSITION[1]
    object.wall_list.append(classification_done_sprite)


    planet_visits_done = False
    val = object.money_earned_from_planet_visits
    if val > 0:
        planet_visits_done = True
    vals = []

    got_nan = False
    i = 0
    while got_nan == False:
        try:
            vals.append(str(val)[i])
        except IndexError:
            got_nan = True
        i = i+1
    i = 0
    for digit in vals:
        sprite1 = arcade.Sprite(f"pictures/digit_{digit}.png", 0.1)
        sprite1.center_x = PLANET_VISIT_SCORE_POSITION[0] + i*40
        sprite1.center_y = PLANET_VISIT_SCORE_POSITION[1]
        object.wall_list.append(sprite1)
        i = i + 1

    if planet_visits_done:
        planet_visits_done_sprite = arcade.Sprite(f"pictures/perfect.png", 0.1)
    else:
        planet_visits_done_sprite = arcade.Sprite(f"pictures/cross.png", 0.1)

    planet_visits_done_sprite.center_x = TASK3_POSITION[0]
    planet_visits_done_sprite.center_y = TASK3_POSITION[1]
    object.wall_list.append(planet_visits_done_sprite)

def start_from_home(object):
    # Load the background image. Do this in the setup so we don't keep reloading it
    object.background = arcade.load_texture("pictures/back.jpg")

    object.information_string = 'Spieldesign: Universität Innsbruck, Pinguin Design: Daniela Kurzböck'

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
    if object.planet == 'PIC':
        if object.telescope_stars_list[object.active_pic][10] ==0:
            object.place = 'home'
            object.return_from_planet_visit = True
            object.return_reason =1
            object.setup()
            return
        if object.telescope_stars_list[object.active_pic][13] ==1 and not object.safety_hazard[0]:
            object.place = 'home'
            object.return_from_planet_visit = True
            object.return_reason =2
            object.setup()
            return
        if object.telescope_stars_list[object.active_pic][14] ==1 and not object.safety_hazard[1]:
            object.place = 'home'
            object.return_from_planet_visit = True
            object.return_reason = 3
            object.setup()
            return
        print(object.safety_hazard, object.telescope_stars_list[object.active_pic][15])
        if object.telescope_stars_list[object.active_pic][15] ==1 and not object.safety_hazard[2]:
            object.place = 'home'
            object.return_from_planet_visit = True
            object.return_reason =4
            object.setup()
            return
        val = randrange(1, 6)
        type = int(object.telescope_stars_list[object.active_pic][10])
        object.background = arcade.load_texture(f"pictures/planets/planet-type{type}-val_{val}.png")
        if type == 1:
            arcade.set_background_color([92, 153, 160])
        elif type ==2 :
            arcade.set_background_color([0, 0, 0])
        elif type ==3 :
            arcade.set_background_color([174, 175, 175])
        else:
            arcade.set_background_color([79, 164, 173])

        object.telescope_stars_list[object.active_pic][12] = 1
        # object.background = arcade.load_texture(f"pictures/planets/planet-type1-val_1.png")
        object.safety_hazard = [False, False, False]
    else:
        try:
            object.background = arcade.load_texture(f"pictures/{object.planet}_bkg.png")
        except FileNotFoundError:
            object.background = arcade.load_texture(f"pictures/{object.planet}_bkg.jpg")
    if object.planet == 'moon' or object.planet == 'jupiter':
        object.information_string = 'Hintergrund: credit: NASA, Spieldesign: Universität Innsbruck, Pinguin Design: Daniela Kurzböck'
    elif object.planet == 'mars':
        object.information_string = 'Hintergrund: credit: NASA Jet Propulsion Laboratory, Spieldesign: Universität Innsbruck, Pinguin Design: Daniela Kurzböck'
    elif object.planet == 'sun' :
        object.information_string = 'Hintergrund: credit: JAXA/NASA Jet Propulsion Laboratory, Spieldesign: Universität Innsbruck, Pinguin Design: Daniela Kurzböck'
    else:
        object.information_string = 'Spieldesign: Universität Innsbruck, Pinguin Design: Daniela Kurzböck'




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

    if object.planet == "PIC":
        utils.PIC_planet_sprites(object)
    else:
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
