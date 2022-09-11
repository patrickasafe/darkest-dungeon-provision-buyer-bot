import keyboard

from utils.buy_provisions import buy_provisions

# Here is the master function:
while keyboard.is_pressed('q') == False:
    print('running buy_provisions')
    buy_provisions()
