'''
SPRITE GAME
-----------
Here you will start the beginning of a game that you will be able to update as we
learn more in upcoming chapters. Below are some ideas that you could include:

1.) Find some new sprite images.
2.) Move the player sprite with arrow keys rather than the mouse. Don't let it move off the screen.
3.) Move the other sprites in some way like moving down the screen and then re-spawning above the window.
4.) Use sounds when a sprite is killed or the player hits the sidewall.
5.) See if you can reset the game after 30 seconds. Remember the on_update() method runs every 1/60th of a second.
6.) Try some other creative ideas to make your game awesome. Perhaps collecting good sprites while avoiding bad sprites.
7.) Keep score and use multiple levels. How do you keep track of an all time high score?
8.) Make a two player game.

'''

import random
import arcade
import math

# --- Constants ---
SW = 800
SH = 600

lanes = [[100 * math.cos(math.radians(0)) + SW/2], [100 * math.sin(math.radians(0)) + SH/2],
         [100 * math.cos(math.radians(360 * 1/16)) + SW/2], [100 * math.sin(math.radians(360 * 1/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 2/16)) + SW/2], [100 * math.sin(math.radians(360 * 2/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 3/16)) + SW/2], [100 * math.sin(math.radians(360 * 3/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 4/16)) + SW/2], [100 * math.sin(math.radians(360 * 4/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 5/16)) + SW/2], [100 * math.sin(math.radians(360 * 5/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 6/16)) + SW/2], [100 * math.sin(math.radians(360 * 6/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 7/16)) + SW/2], [100 * math.sin(math.radians(360 * 7/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 8/16)) + SW/2], [100 * math.sin(math.radians(360 * 8/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 9/16)) + SW/2], [100 * math.sin(math.radians(360 * 9/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 10/16)) + SW/2], [100 * math.sin(math.radians(360 * 10/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 11/16)) + SW/2], [100 * math.sin(math.radians(360 * 11/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 12/16)) + SW/2], [100 * math.sin(math.radians(360 * 12/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 13/16)) + SW/2], [100 * math.sin(math.radians(360 * 13/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 14/16)) + SW/2], [100 * math.sin(math.radians(360 * 14/16)) + SH/2],
         [100 * math.cos(math.radians(360 * 15/16)) + SW/2], [100 * math.sin(math.radians(360 * 15/16)) + SH/2]]


# ------MyGame Class--------------
class MyGame(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        for i in range(0, len(lanes), 4):
            sx += lanes[i]
            sy += lanes[i + 1]
            ex += lanes[i + 2]
            ey += lanes[i + 3]
            arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK)

    def on_update(self, dt):
        pass


# -----Main Function--------
def main():
    window = MyGame(SW, SH, "My Game")
    arcade.run()


# ------Run Main Function-----
if __name__ == "__main__":
    main()
