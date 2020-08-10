"""
Platformer Game
"""
import arcade
import utils
import setups
import text_manager
from  constants import *


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
        self.wall_list = None
        self.player_list = None
        self.text_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.professor_sprite = None
        self.stair_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.place = "starting_sequence"
        self.planet = None
        self.rocket_flying = False
        self.choose_planet = False
        self.planet_gravity = None
        self.enable_physics = None
        self.home_count = 0
        self.home_conversation = False
        self.planet_conversation = False

        self.text_strings = []
        self.top_string = ''
        self.text_val = 0
        self.in_conversation = []
        arcade.set_background_color(arcade.csscolor.BLACK)


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

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        try:
            if self.place == 'on_planet' and self.planet == 'mars':
                arcade.draw_lrwh_rectangle_textured(-500, 0,
                                                1.6*self.background.width/self.background.height*SCREEN_WIDTH, 1.6*SCREEN_HEIGHT,
                                                self.background)
            else:
                arcade.draw_lrwh_rectangle_textured(-500, 0,
                                                1.1*self.background.width/self.background.height*SCREEN_WIDTH, 1.1*SCREEN_HEIGHT,
                                                self.background)
        except AttributeError:
            pass

        # Draw our sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()
        self.text_list.draw()
        text_manager.draw_text(self)
        arcade.draw_text(self.top_string, self.view_left + int(0.5 * SCREEN_WIDTH), self.view_bottom + int(0.9 * SCREEN_HEIGHT),
                         arcade.color.WHITE, 20 , align = 'center', anchor_x = 'center', anchor_y = 'center')


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if self.in_conversation:
            if key == arcade.key.SPACE:
                self.text_val += 1
            return

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            if self.stair_sprite.collides_with_point((self.player_sprite.center_x, self.player_sprite.center_y)):
                self.choose_planet = True
                utils.add_planets(self)
        elif key == arcade.key.ESCAPE:
            self.place = 'home'
            self.setup()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0


    def on_mouse_press(self, x, y, button, modifiers):
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



    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        if self.enable_physics:
            self.physics_engine.update()

        self.top_string = ''

        if self.place == 'home':
            if self.stair_sprite.collides_with_point((self.player_sprite.center_x, self.player_sprite.center_y)):
                if not self.planet_conversation:
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


        # Track if we need to change the viewport
        if self.rocket_flying:
            self.rocket_sprite.change_y = self.rocket_sprite.change_y *1.01
            if self.rocket_sprite.center_y-self.rocket_sprite.height/2 > SCREEN_HEIGHT:
                self.place = 'on_planet'
                self.rocket_flying = False
                self.setup()
        elif self.enable_physics:
            changed = False

            # Scroll left
            left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
            if self.player_sprite.left < left_boundary:
                self.view_left -= left_boundary - self.player_sprite.left
                changed = True

            # Scroll right
            right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
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
