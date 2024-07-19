from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file('gui/kv/home/homescreen.kv')

class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def card_clicked(self, instance):
        pass