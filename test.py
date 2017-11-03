import os
import time
os.system("python no_device_start.py")
time.sleep(10)
os.system("python TitleAndZoomTest.py")
time.sleep(10)
os.system("python FindDeviceTest.py")
time.sleep(10)
os.system("python AppendDeviceTest.py")
time.sleep(10)
os.system("python DeviceParameterCheckTest.py")
time.sleep(10)
os.system("python ParameterPostTest.py")
