from tkinter import *
from snake_game.main import snake_main
from quiz_game.main import quiz_main
from road_cross.main import road_cross_main
from pong_game.main import pong_main
from password_save.main import password_saver_main
from usa_game.main import usa_game_main

BACKGROUND_COLOR = "#2596be"

#old: BACKGROUND_COLOR = "#B1DDC6"

""" def play_snake():
    window.destroy()
    snake_main() 

def play_quiz():
    window.destroy()
    quiz_main()

def play_road_game():
    window.destroy()
    road_cross_main()

def play_pong_game():
    window.destroy()
    pong_main()

def start_password_saver():
    window.destroy()
    password_saver_main()

def usa_map_game():
    window.destroy()
    usa_game_main()
"""

def start_game(game):
    window.destroy()
    game()

window = Tk()

window.title("Fabs Game Arcade")
window.config(background=BACKGROUND_COLOR) 
""" padx=1000, pady=500,  """
""" window.attributes("-fullscreen", True) """



new_canvas = Canvas(width=1000, height=1000, bg=BACKGROUND_COLOR)
new_canvas.grid(row=0, column=0, columnspan=2)

canvas_top_text = new_canvas.create_text(500 , 190, text="Fabs Arcade", anchor="center", font=("Comic Sans MS", 90, "italic"))

""" canvas_snake_img = new_canvas.create_image(300, 500, image=img_snake)
canvas_quiz_img = new_canvas.create_image(900, 500, image=img_quiz) """

#images games
img_snake = PhotoImage(file="images/snake_pic.png")
img_quiz = PhotoImage(file="images/quiz_pic.png")
img_road = PhotoImage(file="images/road_cross.png")
img_pong = PhotoImage(file="images/pong.png")
img_password = PhotoImage(file="images/password.png")
img_usa_map = PhotoImage(file="images/usa_map.png")

#Creating Buttons for games
snake_button = Button(image=img_snake, background=BACKGROUND_COLOR, padx= 100, pady=100, command=lambda: start_game(snake_main))
snake_window = new_canvas.create_window(200, 400, window=snake_button)
""" unknown_button.grid(row=1, column=0) """

quiz_button = Button(image=img_quiz, background=BACKGROUND_COLOR, padx= 100, pady=100, command=lambda: start_game(quiz_main))
quiz_window = new_canvas.create_window(500, 400, window=quiz_button)
""" known_button.grid(row=1, column=1) """

road_button = Button(image=img_road, background=BACKGROUND_COLOR, padx= 100, pady=100, command=lambda: start_game(road_cross_main))
road_window = new_canvas.create_window(800, 400, window=road_button)

pong_button = Button(image=img_pong, background=BACKGROUND_COLOR, padx= 100, pady=100, command=lambda: start_game(pong_main))
png_window = new_canvas.create_window(200, 800, window=pong_button)

password_button = Button(image=img_password, background=BACKGROUND_COLOR, padx= 100, pady=100, command=lambda: start_game(password_saver_main))
password_window = new_canvas.create_window(500, 800, window=password_button)

usa_button = Button(image=img_usa_map, background=BACKGROUND_COLOR, padx= 100, pady=100, command=lambda: start_game(usa_game_main))
usa_window = new_canvas.create_window(800, 800, window=usa_button)

window.mainloop()

