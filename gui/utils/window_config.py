from kivy.core.window import Window
from gui.utils.config import readConfig
from kivy.metrics import dp

Window.size = (dp(readConfig()['window']['window_width']), dp(readConfig()['window']['window_height']))
Window.minimum_width = dp(readConfig()['window']['window_min_width'])
Window.minimum_height = dp(readConfig()['window']['window_min_height'])
Window.set_icon(r'assets/image/icon.jpg')