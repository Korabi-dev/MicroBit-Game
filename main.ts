let gameOver = true;
let y = 0
let x = 0
let rowFull = false
let canFall = false
let canreset = true;
let started = false;
let stringShown = false;
let delay = 0
basic.showIcon(IconNames.Sad);
input.onButtonPressed(Button.A, () => {
    if(gameOver === true) return;
    led.unplot(x, y)
    if (x > 0 && !(led.point(x - 1, y))) {
        x = x - 1
    }
    led.plot(x, y)
})
input.onButtonPressed(Button.B, () => {
    if (gameOver === true) return;
    led.unplot(x, y)
    if (x < 4 && !(led.point(x + 1, y))) {
        x = x + 1
    }
    led.plot(x, y)
})
input.onButtonPressed(Button.AB, function() {
    if (canreset === false) return;
    canreset = false;
    basic.showIcon(IconNames.Happy)
    basic.clearScreen()
    basic.showIcon(IconNames.SmallHeart);
    basic.clearScreen()
    basic.showIcon(IconNames.Heart)
    pause(500)
    stringShown = false;
    basic.clearScreen();
    gameOver = false;
    started = true
})
function tryFall() {
    canFall = y < 4 && !(led.point(x, y + 1))
    if(gameOver === true) canFall = false;
    if (canFall) {
        led.unplot(x, y)
        y = y + 1
        led.plot(x, y)
    } else {
        gameOver = y == 0
    }
    checkFullRow()
}
function checkFullRow() {
    rowFull = false
    for (let xx = 0; xx <= 5 - 1; xx++) {
        if (led.point(xx, 5)) {
            rowFull = true
        }
    }
    if (rowFull) {
        delay = delay * 4 / 5
        for (let yy = 5; yy > 0; yy--) {
            for (let xx3 = 0; xx3 < 5; xx3++) {
                if (led.point(xx3, yy)) {
                    led.unplot(xx3, yy)
                    led.plot(xx3, yy + 1)
                }
            }
        }
    }
}
delay = 500
canFall = true
basic.forever(function(){
    if(gameOver === false){
        y = 0
        x = Math.randomRange(0, 4)
        canFall = true
        led.plot(x, y)
        while (canFall) {
            basic.pause(delay)
            tryFall()
        }
    } else {
        if(stringShown === false && started === true){
            stringShown = true;
            basic.clearScreen();
            basic.showAnimation(`1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 0 1 1 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 0 1 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0`, 100);
        pause(600)
        basic.showIcon(IconNames.Sad);
        canreset = true;
        }
    }
})