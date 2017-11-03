import time
import logging
import logging.config
from pywinauto.application import Application

logging.config.fileConfig('log_config.ini')

class stop:
    """
    This is ActuaticUI main window that make it closed.
    The step show 点击主界面的关闭按钮 -> 然后点击取消 ->再关闭 -> 点击确定
    """
    def __init__(self, app):
        self.app = app
    try:
        def anon_exit(self):
            self.app.关闭.click()
            time.sleep(2)
            self.app.关闭.Button2.click()
            time.sleep(2)
            self.app.close()
            time.sleep(2)
            self.app.关闭.Button.click()
    except BaseException:
        logging.error("Stop---------------------anno_exit was wrong")
    try:
        def immediate_exit(self):
            self.app.关闭.click()
            time.sleep(2)
            self.app.关闭.Button.click()
    except BaseException:
        logging.error("Stop---------------------immediate_exit was wrong")