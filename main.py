'''
********************************************
* @Author: youmetme
* @Date: 2024 07 19
* @Description: 主程序入口
********************************************
'''

from gui.app import MyApp
from core.init import Init

if __name__ == "__main__":
    Init()          #初始化必要环境
    MyApp().run()   #运行主程序