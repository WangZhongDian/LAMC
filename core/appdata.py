'''
********************************************
* @Author: youmetme
* @Date: 2024 07 19
* @Description: 应用数据格式定义
********************************************
'''
from enum import Enum

__all__ = ["AppData", "AppType","AppCategory"]

class AppType(Enum):
    '''
    :description : 应用类型
    '''
    APPLICATION = "application"
    LIBRARY = "library"
    # TODO: Add more types

class AppCategory(Enum):
    '''
    :description : 应用分类
    '''
    GAME = "game"
    DEVELOPMENT = "development"
    AUDIO = "audio"
    VIDEO = "video"
    GRAPHICS = "graphics"
    TOOLS = "tools"
    # TODO: Add more categories

class AppData:
    '''
    :description 应用数据格式
    '''
    downloadurl:str
    icon:str
    appname:str
    version:str
    apptype:AppType
    description:str
    categories:list[AppCategory]
