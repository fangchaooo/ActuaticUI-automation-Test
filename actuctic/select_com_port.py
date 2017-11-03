import serial.tools.list_ports


class Port:

    def __init__(self):
        pass

    @staticmethod
    def find_com_port():
        com_list = serial.tools.list_ports.comports()
        connected = []
        for element in com_list:
            connected.append(element.device)
        return connected



