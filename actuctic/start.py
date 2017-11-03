import time
import logging
import logging.config
from actuctic.select_com_port import Port
from pywinauto.application import Application

# 日志配置
logging.config.fileConfig('log_config.ini')


class Start:
    """
    软件启动，传入端口号和软件地址链接，软件启动分为无连接启动和链接启动
    """
    def __init__(self, com=Port.find_com_port()[0], url='C:\Program Files (x86)\EwayBot\ActuaticUI\ActuaticUI.exe'):
        self.com = com
        self.url = url
        self.app = Application(backend='uia').start(url)
        self.dlg = self.app.window(title_re=".*输入端口*")

    def start_ui(self):
        com = self.com
        dlg = self.dlg
        try:
            if (com):
                dlg.ComboBox.select(com)
                time.sleep(1)
                dlg.child_window(title="确定", auto_id="Button_ConfirmPort", control_type="Button").click()
            else:
                dlg['TitleBar'].关闭.click()
                time.sleep(1)
                dlg['关闭'].Button2.click()
                time.sleep(1)
                dlg['TitleBar'].关闭.click()
                time.sleep(1)
                dlg['关闭'].Button.click()
        except BaseException:
            logging.critical('start error')
        time.sleep(3)