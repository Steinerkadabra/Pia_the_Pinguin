"""
Platformer Game
"""
import arcade
import utils
import setups
import text_manager
from  constants import *
from numpy import loadtxt, where


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


        # Background image will be stored in this variable
        self.background = None

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.collect_coin_list = None
        self.money_coin_list =  arcade.SpriteList()

        image_source = "pictures/coinGold.png"
        self.money_sprite = arcade.Sprite(image_source, 0.5,)
        self.money_coin_list.append(self.money_sprite)

        self.wall_list = None
        self.player_list = None
        self.text_list = None
        self.telescope_stars_list = loadtxt('stars_list.txt')
        for star in self.telescope_stars_list:
            star[-1] = 0 # set all stars to not peer reviewed
        self.telescope_list = arcade.SpriteList()
        self.lightcurve_list = arcade.SpriteList()
        for i in range(len((self.telescope_stars_list.T)[0])):
            image_source = f"pictures/stars/{int(self.telescope_stars_list[i][1])}png.png"
            star_sprite= arcade.Sprite(image_source,  self.telescope_stars_list[i][4]/50)

            star_sprite.center_x = self.telescope_stars_list[i][2]*5
            star_sprite.center_y = self.telescope_stars_list[i][3]*5
            self.telescope_list.append(star_sprite)
        self.active_pic = None

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.professor_sprite = None
        self.stair_sprite = None
        self.whiteboard_sprite = None
        self.lightcurve_sprite = None
        self.lightcurve_active = False
        self.full_button_sprite = None
        self.days_button_sprite = None
        self.hours_button_sprite = None
        self.classification_sprites = [None, None, None, None]
        self.classification_values = [False, False, False, False]
        self.lightcurve_active_kind = 'full'
        self.send_results_sprite = None
        self.close_button = None
        self.do_peer_review = False
        self.peer_review_text = ''

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # self.place = "starting_sequence"
        self.place = "telescope_view"
        # self.place = 'home'
        self.planet = None
        self.rocket_flying = False
        self.choose_planet = False
        self.planet_gravity = None
        self.enable_physics = None
        self.home_count = 0
        self.home_conversation = False
        self.planet_conversation = False
        self.whiteboard_conversation = False

        self.current_money = 0

        self.text_strings = []
        self.top_string = ''
        self.text_val = 0
        self.in_conversation = False




        arcade.set_background_color(arcade.csscolor.BLACK)

        self.planet_score = {'moon': 0, 'sun': 0, 'jupiter':0, 'mars':0}

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        if self.place == "home":
            setups.home(self)

        elif self.place == 'starting_sequence':
            setups.starting_sequence(self)

        elif self.place == "start_from_home":
            setups.start_from_home(self)

        elif self.place == "on_planet":
            setups.planet(self)

        elif self.place == "whiteboard":
            setups.whiteboard(self)

        elif self.place == "telescope_view":
            setups.telescope_view(self)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        try:
            if self.place == 'on_planet' and self.planet == 'mars':
                arcade.draw_lrwh_rectangle_textured(-500, 0,
                                                2.2*self.background.width/self.background.height*SCREEN_WIDTH, 2.2*SCREEN_HEIGHT,
                                                self.background)
            elif self.place == 'whiteboard':
                arcade.draw_lrwh_rectangle_textured(0, 0,
                                                1200, 800,
                                                self.background)
            else:
                arcade.draw_lrwh_rectangle_textured(-500, 0,
                                                1.1*self.background.width/self.background.height*SCREEN_WIDTH, 1.1*SCREEN_HEIGHT,
                                                self.background)
        except AttributeError:
            pass



        # Draw our sprites
        # image_source = "pictures/coin.png"
        # real_size = 0.4
        #
        # sprite = arcade.Sprite(image_source, 1)
        # sprite.center_x = 1150
        # sprite.center_y = 50
        # self.coin_list.append(sprite)

        self.money_sprite.center_x =  self.view_left + 1180
        self.money_sprite.center_y =  self.view_bottom + 780
        self.coin_list.draw()
        if self.place == 'telescope_view':
            self.telescope_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()
        self.collect_coin_list.draw()
        self.player_list.draw()
        self.text_list.draw()
        self.lightcurve_list.draw()
        if self.place != 'whiteboard':
            self.money_coin_list.draw()
        text_manager.draw_text(self)
        arcade.draw_text(self.top_string, self.view_left + int(0.5 * SCREEN_WIDTH), self.view_bottom + int(0.9 * SCREEN_HEIGHT),
                         arcade.color.WHITE, 20 , align = 'center', anchor_x = 'center', anchor_y = 'center')

        if self.peer_review_text != '':
            arcade.draw_text(self.peer_review_text, self.view_left + int(SCREEN_WIDTH / 2) - 400,
            self.view_bottom + int(SCREEN_HEIGHT / 2) + 200,
            arcade.color.BLACK, 22, align = 'left', anchor_x = 'left', anchor_y = 'top')

        if self.current_money < 0:
            color = arcade.color.RED
        else:
            color = arcade.color.WHITE

        if self.place != 'whiteboard':
            arcade.draw_text(str(self.current_money), self.view_left +1150, self.view_bottom +780,color , 20, align='right', anchor_x='right', anchor_y='center')

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # if key == arcade.key.SPACE:
        #     print(self.player_sprite.center_x, self.player_sprite.center_y)


        if self.in_conversation:
            if key == arcade.key.SPACE:
                self.text_val += 1
            return
        else:
            if key == arcade.key.UP or key == arcade.key.W:
                if self.place ==  'telescope_view':
                    self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
                elif self.physics_engine.can_jump():
                    self.player_sprite.change_y = PLAYER_JUMP_SPEED
            elif key == arcade.key.DOWN or key == arcade.key.S:
                if self.place =='telescope_view':
                    self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.SPACE and not self.do_peer_review:
                if self.place == 'telescope_view' and not self.do_peer_review:
                    if self.lightcurve_active:
                        self.lightcurve_active = False
                        self.lightcurve_list = arcade.SpriteList()
                        self.classification_values = [False, False, False, False]
                        self.lightcurve_active_kind = 'full'
                    elif self.active_pic != None:
                        PIC = self.telescope_stars_list[self.active_pic][0]
                        setups.active_lightcurve(self, PIC)
                        # print(self.telescope_stars_list[self.active_pic][0],self.telescope_stars_list[self.active_pic][1],self.telescope_stars_list[self.active_pic][4], )
                elif self.stair_sprite.collides_with_point((self.player_sprite.center_x, self.player_sprite.center_y)):
                    self.choose_planet = True
                    utils.add_planets(self)
                elif self.whiteboard_sprite.collides_with_point((self.player_sprite.center_x, self.player_sprite.center_y)):
                    self.place = 'whiteboard'
                    arcade.set_viewport(0,
                                        SCREEN_WIDTH ,
                                        0,
                                        SCREEN_HEIGHT)
                    self.setup()
            elif key == arcade.key.ESCAPE and self.place != 'start_from_home':
                self.place = 'home'
                self.setup()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

        if self.place == 'telescope_view':
            if key == arcade.key.UP or key == arcade.key.W:
                self.player_sprite.change_y = 0
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.player_sprite.change_y = 0


    def on_mouse_press(self, x, y, button, modifiers):

        x = x + self.view_left
        y = y + self.view_bottom
        print(x,y)



        if self.choose_planet:
            hit_planet = False
            x = x + self.view_left
            y = y + self.view_bottom
            if self.mars_sprite.collides_with_point((x,y)):
                self.planet = 'mars'
                self.planet_gravity = 3.711/9.81
                hit_planet = True
            elif self.sun_sprite.collides_with_point((x,y)):
                self.planet = 'sun'
                self.planet_gravity = 274/9.81
                hit_planet = True
            elif self.moon_sprite.collides_with_point((x,y)):
                self.planet = 'moon'
                self.planet_gravity = 1.62/9.81
                hit_planet = True
            elif self.jupiter_sprite.collides_with_point((x,y)):
                self.planet = 'jupiter'
                self.planet_gravity = 24.8/9.81
                hit_planet = True
            if hit_planet:
                self.place = 'start_from_home'
                self.rocket_flying = True
                self.choose_planet = False
                self.setup()
        elif self.lightcurve_active:
            PIC = self.telescope_stars_list[self.active_pic][0]
            if self.full_button_sprite.collides_with_point((x,y)) and not self.do_peer_review:
                setups.active_lightcurve(self, PIC)
                self.lightcurve_active_kind = 'full'
            elif self.days_button_sprite.collides_with_point((x,y)) and not self.do_peer_review:
                setups.active_lightcurve(self, PIC, kind = 'days')
                self.lightcurve_active_kind = 'days'
            elif self.hours_button_sprite.collides_with_point((x,y)) and not self.do_peer_review:
                setups.active_lightcurve(self, PIC, kind = 'hours')
                self.lightcurve_active_kind = 'hours'
            elif self.send_results_sprite.collides_with_point((x,y)) and self.telescope_stars_list[self.active_pic][-1] == 0:
                print(self.telescope_stars_list[self.active_pic][5:9])
                print(self.classification_values)
                setups.peer_review_feedback(self, self.classification_values, self.telescope_stars_list[self.active_pic][5:9])
                self.do_peer_review = True
            elif self.do_peer_review:
                if self.close_button.collides_with_point((x,y)):
                    self.do_peer_review = False
                    self.peer_review_text = ''
                    self.telescope_stars_list[self.active_pic][-1] = 1
                    setups.active_lightcurve(self, PIC, kind=self.lightcurve_active_kind)
            else:
                for i in range(4):
                    if self.classification_sprites[i].collides_with_point((x,y)):
                        self.classification_values[i] = not self.classification_values[i]
                        setups.active_lightcurve(self, PIC, kind = self.lightcurve_active_kind)
                        break

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Move the player with the physics engine
        if self.enable_physics:
            self.physics_engine.update()

        self.top_string = ''

        if self.place == 'telescope_view':
            collides = arcade.check_for_collision_with_list(self.player_sprite, self.telescope_list)
            if collides:
                spr = collides[0]
                x = set(list(where(self.telescope_stars_list == spr.center_x/5)[0]))
                y = list(where(self.telescope_stars_list == spr.center_y/5)[0])
                intersection = x.intersection(y)
                intersection_as_list = list(intersection)
                try:
                    self.active_pic = intersection_as_list[0]
                except IndexError:
                    pass
                if self.lightcurve_active:
                    self.top_string = f'Das ist PIC {int(self.telescope_stars_list[self.active_pic][0])}. Drücke Leertaste um Beobachtungen zu schließen. '
                else:
                    self.top_string = f'Das ist PIC {int(self.telescope_stars_list[self.active_pic][0])}. Drücke Leertaste für Beobachtungen. '
            else:
                self.active_pic = None

        if self.place == 'home':
            if self.stair_sprite.collides_with_point((self.player_sprite.center_x, self.player_sprite.center_y)):
                if not self.planet_conversation:
                    self.player_sprite.change_x = 0
                    self.player_sprite.change_y = 0
                    utils.text_sprites(self)
                    self.text_strings = [
                        'Super! \n Das ist  \n unsere Rakete!',
                        'Damit können \n wir fast überall \n hinfliegen!',
                        'Woanders sind \n die Bedingungen aber \n ganz anders!',
                        'Die Schwerkraft \n ist z.B. auf dem \n Jupiter viel stärker!',
                        'Wenn du auf\n der Leiter stehst \n und das Leerzeichen \n drückst ...',
                        '... kannst du \n dir aussuchen, wohin \n dich die ...',
                        'Rakete bringen soll! \n Versuche es!'
                    ]
                    if self.text_val == len(self.text_strings) :
                        self.planet_conversation = True
                elif self.choose_planet:
                    self.top_string = 'Wähle mit der Maus ein Ziel aus!'
                else:
                    self.top_string =  'Drücke Leertaste um ein Ziel auszuwählen!'


            if self.whiteboard_sprite.collides_with_point((self.player_sprite.center_x, self.player_sprite.center_y)):
                if not self.whiteboard_conversation:
                    self.player_sprite.change_x = 0
                    self.player_sprite.change_y = 0
                    utils.text_sprites(self)
                    self.text_strings = [
                        'Das ist \n unser Whiteboard!',
                        'Es bildet \n das Zentrum \n unserer Basis',
                        'Hier \n siehst du welche \n Aufgbaen du erfüllen\n musst',
                        'Du kannst \n jederzeit hierher kommen\n um deinen Fortschritt \n zu sehen',
                        'Sieh ihn \n dir doch gleich\n einmal an!'
                    ]
                    if self.text_val == len(self.text_strings) :
                        self.whiteboard_conversation = True
                else:
                    self.top_string =  'Drücke Leertaste um ein deinen Fortschritt zu sehen!'






        if self.place == 'on_planet':
            for sprite in self.collect_coin_list:
                if sprite.collides_with_point((self.player_sprite.center_x, self.player_sprite.center_y)):
                    self.planet_score[self.planet] += 1
                    self.current_money += 1
                    print(self.planet_score)
                    self.collect_coin_list.remove(sprite)


        # Track if we need to change the viewport
        if self.rocket_flying:
            self.rocket_sprite.change_y = self.rocket_sprite.change_y *1.01
            if self.rocket_sprite.center_y-self.rocket_sprite.height/2 > SCREEN_HEIGHT:
                self.place = 'on_planet'
                self.rocket_flying = False
                self.setup()
        elif self.enable_physics or self.place == 'telescope_view':
            changed = False

            # Scroll left
            left_boundary = self.view_left + LEFT_MOVEMENT_MARGIN
            if self.player_sprite.left < left_boundary:
                self.view_left -= left_boundary - self.player_sprite.left
                changed = True

            # Scroll right
            right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MOVEMENT_MARGIN
            if self.player_sprite.right > right_boundary:
                self.view_left += self.player_sprite.right - right_boundary
                changed = True

            # Scroll up
            top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
            if self.player_sprite.top > top_boundary:
                self.view_bottom += self.player_sprite.top - top_boundary
                changed = True

            # Scroll down
            bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
            if self.player_sprite.bottom < bottom_boundary:
                self.view_bottom -= bottom_boundary - self.player_sprite.bottom
                changed = True

            if changed:
                # Only scroll to integers. Otherwise we end up with pixels that
                # don't line up on the screen
                self.view_bottom = int(self.view_bottom)
                self.view_left = int(self.view_left)

                # Do the scrolling
                arcade.set_viewport(self.view_left,
                                    SCREEN_WIDTH + self.view_left,
                                    self.view_bottom,
                                    SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
