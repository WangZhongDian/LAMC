'''
********************************************
* @Author: youmetme
* @Date: 2024 07 18
* @Description: 配置相关工具
********************************************
'''

import configparser

def readConfig()->configparser.ConfigParser:
    '''
    :description : 读取配置文件
    '''
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config