import board
import time
import digitalio
import storage
import keypad
from macrosengine import macroengine

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

km = keypad.KeyMatrix(
    row_pins=(board.GP15, board.GP14, board.GP13, board.GP12),
    column_pins=(board.GP11, board.GP10, board.GP9, board.GP8),
    columns_to_anodes=False,
)

def running_led(speed):
    led.value = True
    time.sleep(speed)
    led.value = False
    time.sleep(speed)

file = "macros.txt"
macros_sum = 0 

with open("/"+file, "r") as f:
    fileLines = f.readlines()
    macros_sum = len(fileLines)

def parse_line(line_number,filename=file):
    with open("/"+filename, "r") as f:
        fileLines = f.readlines()
        for i,line in enumerate(fileLines):
            line =  line.replace("\r\n", "")
            if i == line_number:
                f.close()
                return line
        f.close()

macros = macroengine()

current_profile = 0
profiles = int(macros_sum / km.key_count)
remaining_macros = int(macros_sum % km.key_count )
if remaining_macros > 0:
    profiles += 1

print("Number of lines:"+str(macros_sum))
print("Profiles:"+str(profiles))

def keyToMacro(key_pressed: int):
    x = (current_profile * km.key_count) + key_pressed
    if(key_pressed <= macros_sum - 1):
        macros.parseMacro(parse_line(x))

while True:
    event = km.events.get()
    if event and event.pressed:
        keyToMacro(event.key_number)
    if km.events.overflowed:
        km.events.clear()    # Empty the event queue.
        km.reset()           # Forget any existing presses. Start over.
    running_led(0.05)
