import time
from pywinauto.application import Application


class MenuItem:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def get_menu_item():
        return {
            '模式MenuItem': ['普通模式', '专家模式'],
            '窗口MenuItem': ['实时图表', '命令广播'],
            '帮助MenuItem': ['关于'],
        }

    def get_all(self):
        return self.app.menu()

    def click_menu_item(self):
        s = {}
        s = self.get_menu_item()
        for i in s:
            self.app[i].click_input()
            time.sleep(1)

    def select_fun(self, para={}):
        if para != '':
            s = self.get_menu_item()
            for k,v in para.items():
                s = "" + k+"->"+v
                self.app.menu_select(s)




