# AutoMorse  
## Automatic Morse Code Encoder for Raspberry Pi Pico  

AutoMorse is an automatic Morse code encoding library designed for the Raspberry Pi Pico.  
It can convert the input text message into Morse code and output it through GPIO (you can connect GPIO to other components such as relays to operate the wireless station).  
This library is intended for radio amateurs and users who need automated Morse code sending functionality, and can also be used for teaching and demonstration.

### Features
- **Supports GPIO control**: You can select any GPIO pin as a signal sender and indicator light.
- **Adjustable sending speed**: You can set the sending speed (in words per minute) according to your needs.
- **Standard Morse Code Mapping**: Built-in standard Morse code dictionary, supporting letters, numbers and common symbols.
- **Error Handling**: For invalid characters, an error is signaled.

### How to Use?
1. Download the library file `AutoMorse.py` and put it into the `lib` folder under the Raspberry Pi Pico file directory.  
![image](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/7e8f5df4-7fd6-4f81-bc99-640456c506d8)

2. Call library file: `from AutoMorse import AutoMorse`  
![2eca9c5e1978e0578abd742dc57672ca](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/16f9ce9e-f4e0-4f3c-928e-2440792cc70e)

3. Define parameters: `morse = AutoMorse(buzzer_pin, led_pin, wpm)`  
![image](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/99fde3f8-71eb-467b-ba3f-42141b9199c5)

4. Convert what you want to send into a list and process it using the library:
```MicroPython
phrase = list(content) 
morse.Morse(phrase)
```  
![image](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/5f82e961-a204-45eb-82ca-61073a220618)

