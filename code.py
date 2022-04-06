import board
import time
import digitalio
import storage
import keypad
from macrosengine import macroengine

km = keypad.KeyMatrix(
    row_pins=(board.GP15, board.GP14, board.GP13, board.GP12),
    column_pins=(board.GP11, board.GP10, board.GP9, board.GP8),
    columns_to_anodes=False,
)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def running_led(speed):
    led.value = True
    time.sleep(speed)
    led.value = False
    time.sleep(speed)

file = "macros.txt"
# read a file from the filesystem
def read_file(filename,verbose = False):
    with open("/"+filename, "r") as f:
        fileLines = f.readlines()
        for i,line in enumerate(fileLines):
            fileLines[i] = line.replace("\r\n", "")
            if verbose == True:
                print(i,fileLines[i])
        f.close()
    return fileLines

macros = read_file(file,True)

macros = macroengine(km.key_count)

while True:
    event = km.events.get()
    if event and event.pressed:
        macros.key_actions(event.key_number)
    if km.events.overflowed:
        km.events.clear()    # Empty the event queue.
        km.reset()           # Forget any existing presses. Start over.
    running_led(0.05)
    

