import time
import logging.config
import Stop
import Start

logging.config.fileConfig('log_config.ini')


try:
    right_list = ['选择全部', '115200', '128000', '200000', '230400', '256000', '460800', '500000', '921600', '1000000', '1382400', '1500000', '2000000']
    app_start = Start.Start()
    app_start.start_ui()
    app_main = app_start.app['一维弦电机界面']
    app_main.查找设备.click()
    app_main_device = app_start.app.window(title_re=".*查找设备*")
except BaseException:
    logging.error("FindDeviceTest-----can't find the device window")

try:
    # 波特率设置及查看
    baud_rate = app_main_device.child_window(auto_id="ComboBox_Bitrate", control_type="ComboBox")
    if baud_rate.texts() != right_list:
        raise print("波特率列表出错了")
    for i in range(0, 13):
        baud_rate.select(right_list[i])
        time.sleep(2)
    baud_rate.select('选择全部')
except BaseException:
    logging.error("FindDeviceTest-----baud rate selecting was wrong!")
# 定义起始和终止输入以及各自的测试用例
start_address = app_main_device.Edit1
end_address = app_main_device.Edit2
start_address_text = ['', ' ad@#ad', '34234', 'sdsdfsfsdfdsfdsgfhjsdgjhfg']
end_address_text = ['', ' ad@#ad', '-23', '0', '100']


try:
    # 判断默认值
    if start_address.text_block() != '1' and end_address.text_block() != '253':
        raise print("The default of start address is wrong!")
except BaseException:
    logging.error("FindDeviceTest-----default value was wrong!")

try:
    # TODO：对测试的输入进行随机化，多样化，现在没时间，就自己写一些数进行测试了。后面进行随机生成
    # 超过11位的整数会让软件hung，所以先不进行测试
    #  起始地址输入测试
    for i in start_address_text:
        start_address.set_text(i)
        time.sleep(3)
        app_main_device.查询.click()
        time.sleep(3)
        app_main_device.Dialog2.确定.click()
        time.sleep(3)
except BaseException:
    logging.error("FindDeviceTest-----start address was wrong!")

try:
    # 终止地址输入测试
    for i in end_address_text:
        time.sleep(3)
        if start_address.text_block() == '':
            start_address.set_text('1')
        time.sleep(3)
        end_address.set_text(i)
        time.sleep(3)
        app_main_device.查询.click()
        time.sleep(3)
        if i != end_address_text[-1]:
            app_main_device.Dialog2.确定.click()
except BaseException:
    logging.error("FindDeviceTest-----end address was wrong!")

try:
    # 取消查找测试
    find_rate = app_start.app.window(title_re=".*查找进度*")
    time.sleep(1)
    find_rate.取消.click()
    time.sleep(2)
    find_rate.Button2.click()
    time.sleep(2)
    find_rate['取消'].click()
    time.sleep(2)
    find_rate.Button.click()
    time.sleep(2)
except BaseException:
    logging.error('FindDeviceTest-----cancel find was wrong!')

try:
    # 最终查找
    app_main.查找设备.click()
    end_address.set_text('20')
    app_main_device.查询.click()
    time.sleep(40)
except BaseException:
    logging.error("FindDeviceTest-----finally find device was wrong!")

try:
    # 关闭
    Stop.stop(app_main).immediate_exit()
except BaseException:
    logging.error("FindDeviceTest-----the app can't close")