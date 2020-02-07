#!/usr/bin/env python
import rospy
import socket
from std_msgs.msg import *

class PLC_Ethernet:

    def __init__(self,ip,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))

    def force_set(self,register,set_value):
        if set_value:
            MESSAGE = "STS"+"20".decode("hex")+register+"20".decode("hex")+"01"+"0D".decode("hex")
        else:
            MESSAGE = "RSS"+"20".decode("hex")+register+"20".decode("hex")+"01"+"0D".decode("hex")
        self.s.send(MESSAGE)

    def write_dm_int(self,register,value):
        MESSAGE = "WR"+"20".decode("hex")+register+".S"+"20".decode("hex")+str(value)+"0D".decode("hex")
        self.s.send(MESSAGE)
        

plc = PLC_Ethernet('192.168.5.4',8501)

def force_set(data):
    plc.force_set('R500',data.data)

def write_dm(data):
    plc.write_dm_int('DM150',data.data)

if __name__ == '__main__':
    rospy.init_node('topic_to_plc', anonymous=False)
    rospy.Subscriber("force_set_r500", Bool, force_set)
    rospy.Subscriber("write_dm150",Int64,write_dm)
    rospy.spin()