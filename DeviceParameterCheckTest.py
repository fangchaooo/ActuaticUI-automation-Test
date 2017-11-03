import re
from random import randint
from time import sleep
from Start import start
import logging.config
# 配置日志文件和级别
logging.config.fileConfig('log_config.ini')

app_start = start()
app_start.start_ui()
app_main = app_start.app['一维弦电机界面']

try:
    # 获取TreeView中的波特率、地址、固件版本
    app_main_treeView = app_main.child_window(auto_id="TreeViewActuatic", control_type="Tree")
    s = app_main_treeView.get_item('\电机列表').sub_elements()
    baud_text = s[0].element_info.rich_text
    address_text = s[1].element_info.rich_text
    baud_value = baud_text[4:]
    res = re.compile(r'[0-9\.0-9]+')
    address_value = res.findall(address_text)[0]
    gujian_version = res.findall(address_text)[2]
except BaseException:
    logging.error("DeviceParameterCheckTest-----Can't get the information for treeview!")

try:
    # 选中当前连接舵机
    def click_this(baud_text, address_text, control_obj):
        s = '\\电机列表\\'+baud_text+'\\'+address_text
        control_obj.get_item(s).click_input(button='left')
        sleep(2)

    click_this(baud_text, address_text, app_main_treeView)
except BaseException:
    logging.error("DeviceParameterCheckTest-----can't click the treeview")


try:
    '''
                        查看通信参数中数据是否与显示相同
    '''
    system_para = app_main.child_window(title="系统参数", auto_id="adaaa", control_type="TabItem")
    communions_para = system_para.child_window(title="通信参数", control_type="Group")
    # 获取到ID的输入和ID输入框中的原始值
    communions_para_id_edit = communions_para.Edit
    communions_para_id_edit_para = communions_para_id_edit.text_block()
    # 获取波特率选择和波特率中的原始值
    communions_para_baud = communions_para.child_window(auto_id="ComboBox_Bitrate", control_type="ComboBox")
    communions_para_baud_value = communions_para_baud.selected_text()
    if baud_value == communions_para_baud_value and address_value == communions_para_id_edit_para:
        # Parameter Test successful
        pass
    else:
        raise print("Parameter is wrong")

    # 更改ID和baud rate
    i = randint(0, 11)
    baud_index = ['115200', '128000', '200000', '230400', '256000', '460800', '500000', '921600', '1000000', '1382400', '1500000', '2000000']
    communions_para_id_edit.set_text(str(i))
    sleep(2)
    communions_para_baud.select(baud_index[i])
    sleep(2)
    send_cmd = communions_para.child_window(title="下发", auto_id="button1", control_type="Button")
    send_cmd.click()

    # 再次判断
    if baud_value == communions_para_baud_value and address_value == communions_para_id_edit_para:
        # Parameter Test successful
        pass
    else:
        raise print("Parameter is wrong")

    # 进行ID输入边界测试
    ID_Enter_value = ['', '3242342342', 'sadsd', '#d', '12@', '8']
    for x in ID_Enter_value:
        communions_para_id_edit.set_text(x)
        sleep(2)
        send_cmd.click()
        sleep(2)
        app_main.Dialog2.Button.click()
except BaseException:
    logging.error("DeviceParameterCheckTest-----finding communtion paramenter was wrong!")

try:
    '''
        固件管理
    '''
    # ToDo:选中.bin后缀文件进行固件刷新操作
    gujian_management = system_para.child_window(title="固件管理", control_type="Group")
    gujian_management.child_window(title="...", control_type="Button").click()
    sleep(2)
    open = app_main.child_window(title="打开", control_type="Window")
    open.取消.click()
except BaseException:
    logging.error("DeviceParameterCheckTest-----divice manage was wrong!")
# 关闭
app_main.关闭.click()
sleep(2)
app_main.关闭.Button.click()