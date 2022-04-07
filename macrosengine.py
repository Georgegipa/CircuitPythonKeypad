import usb_hid
from adafruit_hid import consumer_control
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import macros as Bindings

class macroengine(object):

    def __init__(self) -> None:
        self.cc =  consumer_control.ConsumerControl(usb_hid.devices)
        self.mouse = Mouse(usb_hid.devices)
        self.keyboard = Keyboard(usb_hid.devices)
        self.keyboardLayout = KeyboardLayoutUS(self.keyboard)

    def __executeMacro(self, macro: str)-> None:
        macro = macro.split("+")
        for i in macro:
            i = i.lower().upper()
            if i.isalpha() and len(i) == 1:
                self.keyboardLayout.write(i)
            else:
                keycode = Bindings.bindings.get(i)
                if( keycode != None):
                    self.keyboard.press(keycode)
        self.keyboard.release_all()


    def parseMacro(self, macro: str, Verbose: bool = False) -> None:
        if Verbose:
            print("Parsing macro:", macro)
        if macro[1] == ",":
            char = macro[0]
            char.lower().upper()
            print("Macro Commands not supported yet!")
            # if char == 'W':
            # elif char == 'R':
            # elif char == 'P':
            # elif char == 'H':
            # elif char == 'O':
        else:
            self.__executeMacro(macro)
