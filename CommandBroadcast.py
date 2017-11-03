import logging.config
from pywinauto.application import Application
from pywinauto import Desktop, Application


# 日志配置
logging.config.fileConfig('log_config.ini')


class CBroadCast:
    """
    命令广播界面的所有基础功能
    默认全选所有舵机进行后续自动化操作
    """
    def __init__(self):
        self.app = Desktop(backend='uia').window(title_re=".*命令广播*")
        self.pane = self.app['Pane']
        self.custom = self.pane[0]

    def click_button(self, para=None):
        if para == '':
            pass
        else:
            button = self.app[para]
            button.click()

    def calculate_speed(self):
        self.click_button('计算速度')

    def initialization(self):
        self.click_button('初始化')

    def send_command(self):
        self.click_button('下发命令')

    def stop_send(self):
        self.click_button('停止发送')

    def save_all(self):
        self.click_button('保存记录')

    def get_position(self):
        self.click_button('获取位置')

    def insert_value(self):






