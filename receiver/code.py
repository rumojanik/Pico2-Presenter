import usb_hid
import json
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.keycode import Keycode
from adafruit_httpserver import Server, Request, Response, POST, GET


