import time
import logging
import logging.config
from pywinauto.application import Application

logging.config.fileConfig('log_config.ini')


class MenuItem:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def get_menu_item(self):
        return {
            '模式MenuItem': ['普通模式', '专家模式'],
            '窗口MenuItem': ['实时图表', '命令广播'],
            '帮助MenuItem': ['关于'],
        }

    def click_menu_item(self):
        s = self.get_menu_item()
        for i in range(0, 3):
            self.app[s[i]].click_input()
            time.sleep(1)

    def click_fun(self, para):
        s = s