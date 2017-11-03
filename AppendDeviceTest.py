import time
import logging.config
from Start import start
# 配置日志文件和级别
logging.config.fileConfig('log_config.ini')

try:
    # 连接舵机后启动
    url = 'C:\Program Files (x86)\EwayBot\ActuaticUI\ActuaticUI.exe'
    com = 'COM5'
    app_start = start(com, url)
    app_start.start_ui()
    app_main = app_start.app['一维弦电机界面']
except BaseException:
    logging.error("AppendDiviceTest-----starting app was wrong!")

try:
    # 点击添加设备按钮
    app_main.添加设备.click()
    app_main_appendDevice = app_start.app.window(title_re=".*添加设备*")
except BaseException:
    logging.error("AppendDiviceTest-----can't click append button")


# baud_rate select
right_list = ['115200', '128000', '200000', '230400', '256000', '460800', '500000', '921600', '1000000', '1382400', '1500000', '2000000']
baud_rate = app_main_appendDevice.child_window(auto_id="ComboBox_Bitrate", control_type="ComboBox")

try:
    # 修改baud_rate.text_block()为baud_rate.selected_text()
    if baud_rate.texts() != right_list and baud_rate.text_block() != '115200':
        raise print("波特率列表出错了")
    for i in range(0, 12):
        baud_rate.select(right_list[i])
        time.sleep(2)
    baud_rate.select('256000')
except BaseException:
    logging.error("AppendDiviceTest-----baud rate list and default was wrong!")

try:
    # adress input
    address = app_main_appendDevice.Edit
    address_text = ['2332', '-23', '4-2afd', 'sad@$$#', '0', '', 'sadsfsdgfdfsgdfgfsdgfsdgdfgsfdg', '20']
    if address.text_block() != '':
        raise print("The default of address is wrong!")

    # address test
    for i in address_text:
        time.sleep(3)
        address.set_text(i)
        time.sleep(3)
        app_main_appendDevice.Button2.click()
        time.sleep(3)
        if i != address_text[-1]:
            app_main_appendDevice.Dialog2.确定.click()
except BaseException:
    logging.error("AppendDiviceTest-----address input test was wrong!")

# 关闭
app_main.关闭.click()
time.sleep(2)
app_main.关闭.Button.click()