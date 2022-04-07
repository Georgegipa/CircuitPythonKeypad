from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode as ConsumerKeycode

#f_bindings = ["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19","F20","F21","F22","F23","F24"]
#extra_bindings = ["MEDIA","EMAIL","CALC","FILES","B_HOME","B_PREV","B_NEXT","B_REF","B_FAV"]

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

consumer_bindings = {
    "M_PLAY": ConsumerKeycode.PLAY_PAUSE,
    "M_NEXT": ConsumerKeycode.SCAN_NEXT_TRACK,
    "M_PREV": ConsumerKeycode.SCAN_PREVIOUS_TRACK,
    "M_STOP": ConsumerKeycode.STOP,
    "VOL_M": ConsumerKeycode.VOLUME_DECREMENT,
    "VOL_U": ConsumerKeycode.VOLUME_INCREMENT,
    "BRT_U": ConsumerKeycode.BRIGHTNESS_INCREMENT,
    "BRT_D": ConsumerKeycode.BRIGHTNESS_DECREMENT,
}