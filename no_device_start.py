import logging.config
from actuctic.start import Start


# 配置日志文件和级别
logging.config.fileConfig('log_config.ini')

# 测试没有进行设备连接的输入
try:
    app_start = Start()
    app_start.start_ui()
except BaseException:
    logging.critical('no_device_start------start error')
