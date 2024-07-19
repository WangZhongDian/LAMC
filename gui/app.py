'''
********************************************
* @Author: youmetme
* @Date: 2024 07 19
* @Description: 应用程序入口
********************************************
'''
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from gui.utils.font import theme_font_styles
from gui.utils.config import readConfig
import gui.utils.window_config

from kivy.lang.builder import Builder
from kivy.core.window import Window

from gui.pages import *

class MyApp(MDApp):
    def build(self):
        self.language = readConfig()['setting']['language']
        self.title = "Linux for App Management Center" if self.language == 'en' else "Linux应用管理中心"
        self.icon = r'assets/image/icon.jpg'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("gui/kv/app.kv")
    
    def getParentClass(self,startobj:object,mode:str='name',keyword:str=None):
        '''
        :description 获取出发点kivy widget的指定父类实例
        :param startobj:object 发起点kivy widget
        :param mode:str 指定获取模式,类名或id 可选 'name' or 'id'
        :param class_name:str 指定类名
        :param id:str 指定id
        :return 一个指定类名的父类实例
        '''
        temp = startobj.parent
        while True:
            match mode:
                case 'name':
                    print(temp)
                    if type(temp).__name__ == keyword:
                        return temp
                    temp = temp.parent
                    
                    if type(temp).__name__  == type(startobj.get_root_window()).__name__ or temp == None:
                        raise ValueError("Can't find parent class with class_name "+keyword)
                case 'id':
                    if temp.ids.get(keyword) != None:
                        return temp.ids[keyword]
                    temp = temp.parent
                    if type(temp).__name__  == type(startobj.get_root_window()).__name__ or temp == None:
                        raise ValueError("Can't find parent class with ID "+keyword)
                case _:
                    raise ValueError("mode must be 'name' or 'id'")