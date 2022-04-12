# Sign your name: Gabe Van Haecke
 
# You will use the starting code below and build the program "BB8 Attack" as you go through Chapter 15.


import random
import arcade

# --- Constants ---
BB8_scale = 0.03
trooper_scale = 0.1
b_scale = 1
trooper_count = 40
SW = 800
SH = 600
t_speed = 2
t_score = 5
b_score = 1
b_speed = 10


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/gabe.jpg", BB8_scale)
        self.laser_sound = arcade.load_sound("sounds/laser.mp3")

    def update(self):
        self.center_x += self.change_x
        # self.center_y += self.change_y
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
        self.explosion = arcade.load_sound("sounds/explosion.mp3")

    def update(self):
        self.center_y -= t_speed
        if self.top < 0:
            self.center_x = random.randint(self.w, SW - self.w)
            self.center_y = random.randint(SH + self.h, SH * 2)


class Bullet(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/bullet.png", b_scale)
        self.laser_sound = arcade.load_sound("sounds/laser.mp3")

    def update(self):
        self.center_y += b_speed
        if self.bottom > SH:
            self.kill()


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(True)
        self.BB8 = Player()
        self.BB8.bottom = 20
        self.score = 0
        self.BB8.center_x = SW/2

    def reset(self):
        self.player_list = arcade.SpriteList()
        self.trooper_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.gameover = False
        self.player_list.append(self.BB8)

        for i in range(trooper_count):
            trooper = Trooper()
            trooper.center_x = random.randrange(trooper.w, SW - trooper.w)
            trooper.center_y = random.randrange(int(SW/2), SH * 2)
            self.trooper_list.append(trooper)

    def on_draw(self):
        arcade.start_render()
        self.trooper_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.YELLOW)

    def on_update(self, dt):
        self.player_list.update()
        self.trooper_list.update()
        self.bullet_list.update()
        BB8_hit = arcade.check_for_collision_with_list(self.BB8, self.trooper_list)
        if len(BB8_hit) > 0:
            self.BB8.kill()
            arcade.play_sound(self.trooper.explosion_sound)
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.trooper_list)
            if len(hit_list) > 0:
                # arcade.play_sound(self.trooper.explosion)
                bullet.kill()
            for trooper in hit_list:
                trooper.kill()
                self.score += t_score
            if len(self.trooper_list) == 0:
                self.reset()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.BB8.change_x = -4
        elif key == arcade.key.D:
            self.BB8.change_x = 4
        if key == arcade.key.LEFT:
            self.BB8.change_x = -4
        elif key == arcade.key.RIGHT:
            self.BB8.change_x = 4
        if key == arcade.key.SPACE:
            self.bullet = Bullet()
            self.bullet.center_x = self.BB8.center_x
            self.bullet.bottom = self.BB8.top
            self.bullet.angle = 90
            self.bullet_list.append(self.bullet)
            self.score -= b_score
            arcade.play_sound(self.bullet.laser_sound)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.BB8.change_x = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.BB8.change_x = 0



# -----Main Function--------
def main():
    window = MyGame(SW, SH, "BB8 Attack")
    window.reset()
    arcade.run()


# ------Run Main Function-----
if __name__ == "__main__":
    main()
