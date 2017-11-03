from time import sleep
import logging.config
import Start
import Stop
# 配置日志文件和级别
logging.config.fileConfig('log_config.ini')

# 测试启动

try:
    app_start = Start.Start()
    app_start.start_ui()
    app_main = app_start.app['一维弦电机界面']

except BaseException:
    logging.critical('TitleAndZoom---start error')

try:
    # minimize and maximize test
    app_main.minimize()
    sleep(2)
    app_main.maximize()
    sleep(2)
    app_main.TitleBar.还原.click()
    sleep(2)
except BaseException:
    logging.error("TitleAndZoom---the window can't change")

try:
    MenuItem = ['模式MenuItem', '窗口MenuItem', '帮助MenuItem']
    for i in range(0, 3):
        app_main[MenuItem[i]].click_input()
        sleep(2)
except BaseException:
    logging.error("TitleAndZoom---the menu can't click")

# close test
try:
    Stop.stop(app_main).anon_exit()

except BaseException:
    logging.error("TitleAndZoom---the app can't close")

