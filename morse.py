import machine
import utime
from machine import Pin
from utime import sleep

buzzer = Pin(16,Pin.OUT)
led = Pin(17,Pin.OUT)

#_.def
def long():#长
    print('-')
    buzzer.value(1)
    led.value(1)
    sleep(0.15)
    buzzer.value(0)
    led.value(0)
    sleep(0.07)
    
def short():#短
    print('.')
    buzzer.value(1)
    led.value(1)
    sleep(0.075)
    buzzer.value(0)
    led.value(0)
    sleep(0.07)
    
def lettersfeed():#分字
    sleep(0.2)
    
def wordsfeed():#分词
    sleep(0.1)
    
def error():#错误
    print("\033[0;31;40merror\033[0m")
    buzzer.value(1)
    sleep(0.4)
    buzzer.value(0)
    sleep(1)
    
# Morse def
def Morse(Phrase ):
    for letter in Phrase:
        print(letter)
        if letter == 'A' :
            short()#                .
            long()#                 -
            lettersfeed()
            
        elif letter == 'B' :
            long()#                 -
            short()#                .
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == 'C' :
            long()#                 -
            short()#                .
            long()#                 -
            short()#                .
            lettersfeed()
            
        elif letter == 'D' :
            long()#                 -
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == 'E' :
            short()#                .
            lettersfeed()
            
        elif letter == 'F' :
            short()#                .
            short()#                .
            long()#                 -
            short()#                .
            lettersfeed()
            
        elif letter == 'G' :
            long()#                 -
            long()#                 -
            short()#                .
            lettersfeed()
            
        elif letter == 'H' :
            short()#                .
            short()#                .
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == 'I' :
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == 'J' :
            short()#                .
            long()#                 -
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == 'K' :
            long()#                 -
            short()#                .
            long()#                 -
            lettersfeed()
            
        elif letter == 'L' :
            short()#                .
            long()#                 -
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == 'M' :
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == 'N' :
            long()#                 -
            short()#                .
            lettersfeed()
            
        elif letter == 'O' :
            long()#                 -
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == 'P' :
            short()#                .
            long()#                 -
            long()#                 -
            short()#                .
            lettersfeed()
            
        elif letter == 'Q' :
            long()#                 -
            long()#                 -
            short()#                .
            long()#                 -
            lettersfeed()
            
        elif letter == 'R' :
            short()#                .
            long()#                 -
            short()#                .
            lettersfeed()
            
        elif letter == 'S' :
            short()#                .
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == 'T' :
            long()#                 -
            lettersfeed()
            
        elif letter == 'U' :
            short()#                .
            short()#                .
            long()#                 -
            lettersfeed()
            
        elif letter == 'V' :
            short()#                .
            short()#                .
            short()#                .
            long()#                 -
            lettersfeed()
            
        elif letter == 'W' :
            short()#                .
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == 'X' :
            long()#                 -
            short()#                .
            short()#                .
            long()#                 -
            lettersfeed()
            
        elif letter == 'Y' :
            long()#                 -
            short()#                .
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == 'Z' :
            long()#                 -
            long()#                 -
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == '1' :
            short()#                .
            long()#                 -
            long()#                 -
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == '2' :
            short()#                .
            short()#                .
            long()#                 -
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == '3' :
            short()#                .
            short()#                .
            short()#                .
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == '4' :
            short()#                .
            short()#                .
            short()#                .
            short()#                .
            long()#                 -
            lettersfeed()
            
        elif letter == '5' :
            short()#                .
            short()#                .
            short()#                .
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == '6' :
            long()#                 -
            short()#                .
            short()#                .
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == '7' :
            long()#                 -
            long()#                 -
            short()#                .
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == '8' :
            long()#                 -
            long()#                 -
            long()#                 -
            short()#                .
            short()#                .
            lettersfeed()
            
        elif letter == '9' :
            long()#                 -
            long()#                 -
            long()#                 -
            long()#                 -
            short()#                .
            lettersfeed()
            
        elif letter == '0' :
            long()#                 -
            long()#                 -
            long()#                 -
            long()#                 -
            long()#                 -
            lettersfeed()
            
        elif letter == ' ':
            wordsfeed()
        
        else :
            error()
