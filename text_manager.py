import arcade

import utils
from  constants import *

def draw_text(object):
    # utils.text_sprites(object)
    if object.place == 'starting_sequence':
        TEXT_SIZE1 = 34
        TEXT_SIZE2 = 14
    else:
        TEXT_SIZE1 = 24
        TEXT_SIZE2 = 8
    # print(object.text_val, object.text_strings, len(object.text_list) )
    if len(object.text_strings) > 0 and object.text_val <  len(object.text_strings):
        center_x = object.text_list[-1].center_x - int(object.text_list[-1].width * 0.05)
        center_y = object.text_list[-1].center_y +  2*int(object.text_list[-1].height * 0.05)
        arcade.draw_text(object.text_strings[object.text_val], center_x, center_y,
                         arcade.color.BLACK, TEXT_SIZE1 , align = 'center', anchor_x = 'center', anchor_y = 'center')

        center_x = object.text_list[-1].center_x - int(object.text_list[-1].width * 0.05)
        center_y = object.text_list[-1].center_y - int(object.text_list[-1].height * 0.25)

        arcade.draw_text('Drücke Leerzeichen um fortzufahren!', center_x, center_y,
                         arcade.color.BLACK, TEXT_SIZE2 , align = 'center', anchor_x = 'center', anchor_y = 'center')
    else:
        object.in_conversation = False
        object.text_val = 0
        object.text_strings = []
        object.text_list = arcade.SpriteList()
        if object.place == 'starting_sequence':
            object.place = 'home'
            object.setup()


