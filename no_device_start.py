import logging.config
from Start import start

# 配置日志文件和级别
logging.config.fileConfig('log_config.ini')

# 测试没有进行设备连接的输入
try:
    app_start = start()
    app_start.start_ui()
except BaseException:
    logging.critical('no_device_start------start error')
