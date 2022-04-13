def on_button_pressed_a():
    global number
    for index in range(9):
        number += -1
        basic.show_number(number)
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

number = 0
basic.show_string("Starting Countdown  ")
number = 9
basic.show_number(number)