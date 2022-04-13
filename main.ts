input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 9; index++) {
        number += -1
        basic.showNumber(number)
    }
    game.gameOver()
})
let number = 0
basic.showString("Starting Countdown  ")
number = 9
basic.showNumber(number)
