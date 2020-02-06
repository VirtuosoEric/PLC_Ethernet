#!/usr/bin/python
import os
import sys
import time
import socket


TCP_IP = '192.168.5.4'
TCP_PORT = 8501
BUFFER_SIZE = 1024

def write_to_plc(TCP_IP,TCP_PORT,MESSAGE):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    # data = s.recv(BUFFER_SIZE)
    s.close()

MESSAGE = "WR"+"20".decode("hex")+"DM150.U"+"20".decode("hex")+"1000"+"0D".decode("hex")
write_to_plc(TCP_IP,TCP_PORT,MESSAGE)

