# Sign your name: Gabe Van Haecke
 
# You will use the starting code below and build the program "BB8 Attack" as you go through Chapter 15.


import random
import arcade

# --- Constants ---
BB8_scale = 0.3
trooper_scale = 0.1
trooper_count = 5000
SW = 800
SH = 600


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/bb8.png", BB8_scale)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        if self.right > SW:
            self.right = SW
        if self.top > SH:
            self.top = SH
        if self.bottom < 0:
            self.bottom = 0


class Trooper(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/stormtrooper.png", trooper_scale)
        self.w = int(self.width)
        self.h = int(self.height)

    def update(self):
        pass


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.set_mouse_visible(False)

    def reset(self):
        self.player_list = arcade.SpriteList()
        self.trooper_list = arcade.SpriteList()
        self.score = 0
        self.BB8 = Player()
        self.BB8.center_x = SW/2
        self.BB8.center_y = SH/2
        self.player_list.append(self.BB8)

        for i in range(trooper_count):
            trooper = Trooper()
            trooper.center_x = random.randrange(trooper.w, SW - trooper.w)
            trooper.center_y = random.randrange(trooper.h, SH - trooper.h)
            self.trooper_list.append(trooper)

    def on_draw(self):
        arcade.start_render()
        self.trooper_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK)

    def on_update(self, dt):
        self.player_list.update()
        self.trooper_list.update()

        trooper_hit_list = arcade.check_for_collision_with_list(self.BB8, self.trooper_list)
        for trooper in trooper_hit_list:
            trooper.kill()
            self.score += 1

        if self.score == trooper_count:
            self.reset()

    def on_mouse_motion(self, x, y, dx, dy):
        self.BB8.center_x = x
        self.BB8.center_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.BB8.change_x = -4
        elif key == arcade.key.D:
            self.BB8.change_x = 4
        elif key == arcade.key.W:
            self.BB8.change_y = 4
        elif key == arcade.key.S:
            self.BB8.change_y = -4
        if key == arcade.key.LEFT:
            self.BB8.change_x = -4
        elif key == arcade.key.RIGHT:
            self.BB8.change_x = 4
        elif key == arcade.key.UP:
            self.BB8.change_y = 4
        elif key == arcade.key.DOWN:
            self.BB8.change_y = -4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.BB8.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.BB8.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.BB8.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.BB8.change_y = 0


# -----Main Function--------
def main():
    window = MyGame(SW, SH, "BB8 Attack")
    window.reset()
    arcade.run()


# ------Run Main Function-----
if __name__ == "__main__":
    main()
