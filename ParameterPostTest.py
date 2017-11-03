from time import sleep
import logging.config
from Start import start

# 连接舵机后启动
url = 'C:\Program Files (x86)\EwayBot\ActuaticUI\ActuaticUI.exe'
com = 'COM5'
app_start = start(com, url)
app_start.start_ui()
app_main = app_start.app['一维弦电机界面']


# 配置日志文件和级别
logging.config.fileConfig('log_config.ini')

try:
    # 选中舵机参数
    app_main.TabControl.select("舵机参数")
    duoji_para = app_main.child_window(title="舵机参数", control_type="TabItem")
except BaseException:
    logging.error("ParameterPostTest-----select douji parameter was wrong")

# 获取TreeView中的波特率、地址、固件版本
app_main_treeView = app_main.child_window(auto_id="TreeViewActuatic", control_type="Tree")
s = app_main_treeView.get_item('\电机列表').sub_elements()
baud_text = s[0].element_info.rich_text
address_text = s[1].element_info.rich_text
baud_value = baud_text[4:]


# 选中当前设备
def click_this(baud_text1, address_text1, control_obj):
    # 选中当前连接舵机
    str1 = '\\电机列表\\'+baud_text+'\\'+address_text
    control_obj.get_item(str1).click_input(button='left')
    sleep(2)

click_this(baud_text, address_text, app_main_treeView)

try:
    # 电机参数输入测试
    dianji_para = duoji_para.child_window(title="电机参数", control_type="Group")
    xiafa = duoji_para.child_window(title="下发", control_type="Button")
    TestList = [
        ['', '', ''],
        ['-1', '1', '1'],
        ['266', '1', '1'],
        ['-32', '1', '1'],
        ['435', '1', '1'],
        ['sdsa', '1', '1'],
        ['@123', '1', '1'],
        ['22!', '1', '1'],
        ['6.6', '1', '1'],
        ['12', '', '1'],
        ['66', 'sqd1', '1'],
        ['111', '@#dsf', '1'],
        ['222', '2313213', '1'],
        ['232', '-23234', '1'],
        ['143', '-1', '1'],
        ['155', '655.4', '1'],
        ['66', 'asqw2', '1'],
        ['66', '232.1', '1'],
    ]
    for i in TestList:
        sleep(1)
        dianji_para.Edit.set_text(i[0])
        sleep(1)
        dianji_para.Edit2.set_text(i[1])
        sleep(1)
        dianji_para.Edit3.set_text(i[2])
        sleep(1)
        xiafa.click()
        sleep(1)
        app_main['Dialog2'].确定.click()

except BaseException:
    logging.error("ParameterPostTest------the para of dianji input error")

try:
    # 保护参数输入测试
    protect_para = duoji_para.child_window(title="保护参数", control_type="Group")
    angle_value = [
        ['-4324', '-3423'],
        ['', ''],
        ['dsfhsdf', 'sdfs'],
        ['358', '35'],
        ['33', '256'],
    ]

    voltage_value = [
        ['32', '61'],
        ['-4', '-3423'],
        ['', ''],
        ['ds', 'sdfs'],
        ['58', '35'],
        ['52', '344'],
        ['33', '60'],
        ['60', '22'],
    ]

    for j in angle_value:
        sleep(1)
        protect_para.Edit.set_text(j[0])
        sleep(1)
        protect_para.Edit2.set_text(j[1])
        sleep(1)
        xiafa.click()
        sleep(1)
        app_main['Dialog2'].确定.click()

    for k in voltage_value:
        sleep(1)
        protect_para.Edit3.set_text(k[0])
        sleep(1)
        protect_para.Edit4.set_text(k[1])
        sleep(1)
        xiafa.click()
        sleep(1)
        if k != voltage_value[-1]:
            app_main['Dialog2'].确定.click()
except BaseException:
    logging.error("ParameterPostTest-----project para was wrong!")

sleep(5)
# 关闭
app_main.关闭.click()
sleep(2)
app_main.关闭.Button.click()