"""
# AutoMorse - Automatic Morse Code Transmitter for Raspberry Pi Pico
# Copyright (c) 2024 MQSI/BG7ZDQ (maqingshui@outlook.com)
# The Apache License 2.0 - see license file
"""

from machine import Pin
from utime import sleep

class AutoMorse:
    
    # Output port, external indication Led port, transmission speed
    def __init__(self, buzzer_pin, led_pin, wpm):
        self.buzzer = Pin(buzzer_pin, Pin.OUT)
        self.led = Pin(led_pin, Pin.OUT)
        

        # In standard conditions, the duration of a dot in Morse code is 1.2 times the words per minute (WPM) rate
        # (1.2 is the standard time unit). The duration of a dash is 3 times the duration of a dot. The interval between
        # letters is 3 times the duration of a dot, and the interval between words is 7 times the duration of a dot.
        self.dot_length = 1.2 / wpm
        self.dash_length = self.dot_length * 3
        self.letter_space = self.dot_length * 3
        self.word_space = self.dot_length * 7
        
        # dictionary mapping
        self.morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
            '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
            '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
            '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
            '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', 
            ' ': ' '
        }

    def long(self):
        print('-')
        self.buzzer.value(1)
        self.led.value(1)
        sleep(self.dash_length)
        self.buzzer.value(0)
        self.led.value(0)
        sleep(self.dot_length)

    def short(self):
        print('.')
        self.buzzer.value(1)
        self.led.value(1)
        sleep(self.dot_length)
        self.buzzer.value(0)
        self.led.value(0)
        sleep(self.dot_length)

    def lettersfeed(self):
        sleep(self.letter_space - self.dot_length)

    def wordsfeed(self):
        sleep(self.word_space - self.dot_length)

    def error(self):
        print("error")
        self.buzzer.value(1)
        sleep(self.word_space)
        self.buzzer.value(0)
        sleep(self.letter_space)

    def Morse(self, phrase):
        for letter in phrase:
            if letter in self.morse_code:
                morse_representation = self.morse_code[letter]
                print(letter, morse_representation)
                for symbol in morse_representation:
                    if symbol == '-':
                        self.long()
                    elif symbol == '.':
                        self.short()
                if letter != ' ':
                    self.lettersfeed()
                else:
                    self.wordsfeed()
            else:
                self.error()
