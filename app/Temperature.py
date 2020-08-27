import time

sensor_file_path = ['/sys/devices/w1_bus_master1/28-811851516bff/w1_slave', '/sys/devices/w1_bus_master1/28-81185151c0ff/w1_slave']

def ReadTempRaw(sensor_number):
    f = open(sensor_file_path[sensor_number], 'r')
    lines = f.readlines()
    f.close()
    return lines

def ReadTemp(sensor_number):
    lines = ReadTempRaw(sensor_number)

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = ReadTempRaw()
    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = "{:.1f}".format(float(temp_string) / 1000.0)
        return temp_c