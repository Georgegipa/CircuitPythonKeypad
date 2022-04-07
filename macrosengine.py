import usb_hid
from adafruit_hid import consumer_control
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control_code import ConsumerControlCode as ConsumerKeycode
import time

bindings = {
    "CTRL": Keycode.CONTROL,
    "SHIFT": Keycode.SHIFT,
    "ALT": Keycode.ALT,
    "WIN": Keycode.GUI,
    "UP": Keycode.UP_ARROW,
    "DOWN": Keycode.DOWN_ARROW,
    "LEFT": Keycode.LEFT_ARROW,
    "RIGHT": Keycode.RIGHT_ARROW,
    "BKSP": Keycode.BACKSPACE,
    "TAB": Keycode.TAB,
    "ENTER": Keycode.ENTER,
    "ESC": Keycode.ESCAPE,
    "INS": Keycode.INSERT,
    "DEL": Keycode.DELETE,
    "PU": Keycode.PAGE_UP,
    "PD": Keycode.PAGE_DOWN,
    "HOME": Keycode.HOME,
    "END": Keycode.END,
    "CL": Keycode.CAPS_LOCK,
    "M_PLAY": ConsumerKeycode.PLAY_PAUSE,
}

special_chars_bindings = {
    "`": Keycode.GRAVE_ACCENT,
    "~": Keycode.GRAVE_ACCENT,
    "!": Keycode.ONE,
    "@": Keycode.TWO,
    "#": Keycode.THREE,
    "$": Keycode.FOUR,
    "%": Keycode.FIVE,
    "^": Keycode.SIX,
    "&": Keycode.SEVEN,
    "*": Keycode.EIGHT,
    "(": Keycode.NINE,
    ")": Keycode.ZERO,
    "_": Keycode.MINUS,
    "+": Keycode.EQUALS,
    "-": Keycode.MINUS,
    "=": Keycode.EQUALS,
    "{": Keycode.LEFT_BRACKET,
    "}": Keycode.RIGHT_BRACKET,
    "[": Keycode.LEFT_BRACKET,
    "]": Keycode.RIGHT_BRACKET,
    "|": Keycode.BACKSLASH,
    ":": Keycode.SEMICOLON,
    ";": Keycode.SEMICOLON,
    '"': Keycode.QUOTE,
    "'": Keycode.QUOTE,
    ",": Keycode.COMMA,
    "<": Keycode.COMMA,
    ".": Keycode.PERIOD,
    ">": Keycode.PERIOD,
    "/": Keycode.FORWARD_SLASH,
    "?": Keycode.FORWARD_SLASH,
    "\\": Keycode.BACKSLASH,
    " ": Keycode.SPACE
}

consumer_bindings = {
    "M_PLAY": ConsumerKeycode.PLAY_PAUSE,
    "M_NEXT": ConsumerKeycode.SCAN_NEXT_TRACK,
    "M_PREV": ConsumerKeycode.SCAN_PREVIOUS_TRACK,
    "M_STOP": ConsumerKeycode.STOP,
    "VOL_M": ConsumerKeycode.MUTE,
    "VOL_U": ConsumerKeycode.VOLUME_INCREMENT,
    "VOL_D": ConsumerKeycode.VOLUME_DECREMENT,
    "BRT_U": ConsumerKeycode.BRIGHTNESS_INCREMENT,
    "BRT_D": ConsumerKeycode.BRIGHTNESS_DECREMENT,
}

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
            keycode =None
            if len(i) == 1:
                ascii_i = ord(i)
                if i.isalpha():
                    keycode = int(Keycode.Z) - (ord('Z') - ascii_i ) 
                    
                elif i.isdigit:
                    keycode = int(Keycode.NINE) - (ord('1')- ascii_i) 
                else:
                    keycode = special_chars_bindings.get(i)
                self.keyboard.press(keycode)       
            elif len(i) == 2 or len(i)==3:
                if(i[0] == 'F'):
                    temp = i[1:]
                    if(temp.isdigit() and int(temp) >= 1 and int(temp) <= 24):
                        if(int(temp) >= 1 and int(temp) <= 12):
                            keycode = Keycode.F1 + int(temp) - 1
                        elif(int(temp) >= 13 and int(temp) <= 24):
                            keycode = Keycode.F13 + int(temp) - 13
            else:
                keycode = bindings.get(i)
                if(len(i) >= 4 and keycode == None):
                    keycode = consumer_bindings.get(i)
                    if(keycode != None):
                        self.cc.send(keycode)
                        continue
            self.keyboard.press(keycode)
        self.keyboard.release_all()


    def parseMacro(self, macro: str, Verbose: bool = False) -> None:
        if Verbose:
            print("Parsing macro:", macro)
        if macro[1] == ",":
            char = macro[0]
            char.lower().upper()
            if char == 'W':
                self.keyboardLayout.write(macro[2:])
            elif char == 'R':
                self.keyboard.press(Keycode.WINDOWS)
                self.keyboard.press(Keycode.R)
                self.keyboard.release_all()
                time.sleep(0.05)
                self.keyboardLayout.write(macro[2:])
                self.keyboard.press(Keycode.ENTER)
                self.keyboard.release_all()
            elif char == 'P' or  char == 'H' or char == 'O':
                print("Macro Command not supported yet!")
        else:
            self.__executeMacro(macro)
