from machine import Pin
from utime import sleep
from morse import Morse
import utime
import machine

start = Pin(25,Pin.OUT)# 定义启动指示端口，使用GPIO5
for i in range (1,2):
    start.value(1)# 指示端口初始化为导通
    sleep(i)
    start.value(0)# 指示端口初始化为断开
    sleep(0.1)
start.value(1)# 指示端口初始化为导通

while True:
    Content = input("请输入发报内容（仅限英文大写与数字）:") 
    Phrase  = list(Content)
    print(Phrase )
    Morse(Phrase )

