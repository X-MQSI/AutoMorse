from machine import Pin
from utime import sleep
from AutoMorse import AutoMorse

# Use GPIO 17 as the transmitting IO
# Use the PICO onboard LED (GPIO 25) as the transmitting light indicator
# And the transmitting speed is 22wpm
morse = AutoMorse(17, 25, 22)

while True:
    content = input("Please enter the message content: ") 
    phrase = list(content)
    print(phrase)
    morse.Morse(phrase)

# Example CQ CQ CQ CQ BG7ZDQ BG7ZDQ BG7ZDQ K
