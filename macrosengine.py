import usb_hid
from adafruit_hid import consumer_control
import adafruit_hid.keyboard as keyboard
import adafruit_hid.mouse as mouse
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode

class macroengine(object):

    def __init__(self, key_count: int) -> None:
        self.cc =  consumer_control.ConsumerControl(usb_hid.devices)
        self.key_count = key_count

    def HIDsend(keycode , type):
        print(type)

    def key_actions(self,key: int):
        if key >= self.key_count or key < 0:
            print("Undefined key")
        else :
            print("Just pressed key:", key)
            if key == 5:
                self.cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            elif key == 4:
                self.cc.send(ConsumerControlCode.VOLUME_DECREMENT)