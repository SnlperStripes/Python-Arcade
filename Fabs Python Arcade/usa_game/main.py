import  turtle
import pandas
from usa_game.written import Written, Scoreboard

def usa_game_main():

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.setup(width=725, height=491)
    

    image = "usa_game/data/blank_states_img.gif"

    data = pandas.read_csv("usa_game/data/50_states.csv")

    game_is_on = True

    screen.addshape(image)
    turtle.shape(image)
    counter = 0

    #make list to check if in list
    all_states = data.state.to_list()

    correct_guesses = []

    def save_progress():
        
        saved_states = [state for state in all_states if state not in correct_guesses]

        print(saved_states)
        progress_data = pandas.DataFrame(saved_states)
        progress_data.to_csv("usa_game/data/save_file.csv")

    while game_is_on and counter < 50:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct", prompt="What's a State's name?")
        answer_state = answer_state.title()
        print(answer_state)

        if answer_state == "Exit":
            save_progress()
            break
        elif answer_state in all_states:
            guessed_state = data[data.state == answer_state]
            print(guessed_state)
            x_guessed = int(guessed_state.x)
            y_guessed = int(guessed_state.y)


            written_name = Written()
            written_name.destination(x_guessed, y_guessed)
            written_name.text(answer_state)
            counter += 1
            correct_guesses.append(answer_state)
            if counter >= 2:
                score.clear()
            score = Scoreboard()
            score.show_score(counter)
            print(correct_guesses)
            screen.title(f"U.S. States Game {counter}/50")