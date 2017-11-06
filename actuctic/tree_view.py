import re
import time
from pywinauto.application import Application


class TreeView:
    """
    获取主界面中的TreeView中的各个参数
    """
    def __init__(self, app):
        self.app = app
        self.tree_view = self.app.child_window(auto_id="TreeViewActuatic", control_type="Tree")

    def get_tree_view_text(self):
        # 获取主界面上的treeview的所有文本
        s = self.tree_view.get_item('\电机列表').sub_elements()
        if s == '':
            assert "This TreeView is none!"
        else:
            baud_text = s[0].element_info.rich_text
            address_text = s[1].element_info.rich_text
            return baud_text, address_text

    def get_tree_view_value(self):
        baud_text, address_text = self.get_tree_view_text()
        res = re.compile(r'[0-9\.0-9]+')
        address_value = res.findall(address_text)[0]
        firmware_version = res.findall(address_text)[2]
        return address_value, firmware_version

    def select_actuator(self):
        baud_text, address_text = self.get_tree_view_text()
        cc = '\\电机列表\\' + baud_text + '\\' + address_text
        self.tree_view.get_item(cc).click_input(button='left')
        time.sleep(2)