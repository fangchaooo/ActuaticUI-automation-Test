import time
from pywinauto.application import Application


class TitleBar:
    def __init__(self, app):
        self.app = app

    def max_main_window(self):
        self.app.maximize()

    def min_main_window(self):
        self.app.minimize()

    def reduction_main_window(self):
        # 还原必须在界面放大后才可以执行
        self.app.TitleBar.还原.click()

