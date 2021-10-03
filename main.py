import os
import re


def exec_cmd(cmd):
    cmd = os.popen(cmd)
    cmd_result = cmd.read()
    cmd.close()
    return cmd_result


def get_device_ip(content):
    math_obj = re.search(r'inet\s(\d+\.\d+\.\d+\.\d+).*?wlan0', content)
    if math_obj and math_obj.group(1):
        return math_obj.group(1)
    return None


if __name__ == '__main__':
    result = exec_cmd('adb shell ip addr show wlan0')
    ip = get_device_ip(result)
    print(ip)

