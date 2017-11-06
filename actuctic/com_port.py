import serial.tools.list_ports


class Port:

    def __init__(self):
        pass

    @staticmethod
    def find_com_port():
        com_list = serial.tools.list_ports.comports()
        if com_list == '':
            return ''
        connected = []
        for element in com_list:
            connected.append(element.device)
        return connected

    @staticmethod
    def find_one_port():
        com = Port.find_com_port()
        if not com:
            return ''
        else:
            return com[0]



