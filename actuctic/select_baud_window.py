import time
from pywinauto.application import Application
from pywinauto import Desktop, Application


class SelectBaud:
    """
    操作命令广播 -> 选择波特率
    select_baud_rate(parameter) ---------- 选择通讯波特率
        parameter在没有对设备选择的情况下，默认为115200
                在TreeView里面选中哪个，哪个设备的波特率就是默认波特率
    """

    def __init__(self):
        self.app = Desktop(backend='uia').window(title_re=".*选择波特率*")
        self.close = self.app.child_window(title="关闭", control_type="Button")
        self.selectBaudRateComboBox = self.app.child_window(auto_id="ComboBox_Bitrate", control_type="ComboBox")
        self.selectListBox = self.app.child_window(auto_id="ListView_Address", control_type="List")
        self.select_history = self.app.child_window(title="选择记录", control_type="Button")
        self.enter = self.app.child_window(title="确认", control_type="Button")

    def get_baud(self):
        return self.selectBaudRateComboBox.selected_text()

    def check_baud(self):
        baud_list = ['115200', '128000', '200000', '230400', '256000', '460800', '500000', '921600', '1000000', '1382400', '1500000', '2000000']
        if self.selectBaudRateComboBox.texts() != baud_list:
            raise "波特率列表出错了"
        for i in range(0, 12):
            self.selectBaudRateComboBox.select(baud_list[i])
            time.sleep(2)

    def set_baud(self, baud_rate):
        self.check_baud()
        self.selectBaudRateComboBox.select(baud_rate)

    def check_listbox(self):
        # ToDo:在listBox中的内容与TreeView相对比
         pass

    def get_listbox(self):
        return self.selectListBox.texts()

    def set_listbox(self, checkbox_list):
        for i in checkbox_list:
            self.selectListBox.get_item(i).click_input(button='left')

    def verify_button(self):
        self.enter.click()

    def select_history_button(self):
        pass

    def close_window(self):
        self.close.click()



