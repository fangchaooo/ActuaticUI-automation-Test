import time
from pywinauto.application import Application


class Stop:
    """
    This is ActuaticUI main window that make it closed.
    The step show 点击主界面的关闭按钮 -> 然后点击取消 ->再关闭 -> 点击确定
    """
    def __init__(self, app):
        self.app = app
    try:
        def anon_exit(self):            # 延迟关闭
            self.app.关闭.click()
            time.sleep(2)
            self.app.关闭.Button2.click()
            time.sleep(2)
            self.app.close()
            time.sleep(2)
            self.app.关闭.Button.click()
    except BaseException:
        pass
    try:
        def immediate_exit(self):        # 直接关闭
            self.app.关闭.click()
            time.sleep(2)
            self.app.关闭.Button.click()

    except BaseException:
        pass