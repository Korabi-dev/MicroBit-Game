gameOver = True
y = 0
x = 0
rowFull = False
canFall = False
canreset = True
started = False
stringShown = False
delay = 0
basic.show_icon(IconNames.SAD)

def on_button_pressed_a():
    global x
    if gameOver == True:
        return
    led.unplot(x, y)
    if x > 0 and not (led.point(x - 1, y)):
        x = x - 1
    led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x
    if gameOver == True:
        return
    led.unplot(x, y)
    if x < 4 and not (led.point(x + 1, y)):
        x = x + 1
    led.plot(x, y)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global canreset, stringShown, gameOver, started
    if canreset == False:
        return
    canreset = False
    basic.show_icon(IconNames.HAPPY)
    basic.clear_screen()
    basic.show_icon(IconNames.SMALL_HEART)
    basic.clear_screen()
    basic.show_icon(IconNames.HEART)
    pause(500)
    stringShown = False
    basic.clear_screen()
    gameOver = False
    started = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def tryFall():
    global canFall, y, gameOver
    canFall = y < 4 and not (led.point(x, y + 1))
    if gameOver == True:
        canFall = False
    if canFall:
        led.unplot(x, y)
        y = y + 1
        led.plot(x, y)
    else:
        gameOver = y == 0
    checkFullRow()
def checkFullRow():
    global rowFull, delay
    rowFull = False
    xx = 0
    while xx <= 5 - 1:
        if led.point(xx, 5):
            rowFull = True
        xx += 1
    if rowFull:
        delay = delay * 4 / 5
        yy = 5
        while yy > 0:
            for xx3 in range(5):
                if led.point(xx3, yy):
                    led.unplot(xx3, yy)
                    led.plot(xx3, yy + 1)
            yy -= 1
delay = 500
canFall = True

def on_forever():
    global y, x, canFall, stringShown, canreset
    if gameOver == False:
        y = 0
        x = Math.random_range(0, 4)
        canFall = True
        led.plot(x, y)
        while canFall:
            basic.pause(delay)
            tryFall()
    else:
        if stringShown == False and started == True:
            stringShown = True
            basic.clear_screen()
            basic.show_animation("""
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0
                    1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 0 1 1 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                    1 1 0 1 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                    1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0
                """,
                100)
            pause(600)
            basic.show_icon(IconNames.SAD)
            canreset = True
basic.forever(on_forever)
