# AutoMorse  
## 适用于Raspberry Pi Pico的自动摩尔斯电码编码器

AutoMorse 是专为 Raspberry Pi Pico 设计的自动摩尔斯电码编码库。  
它可以将输入的文本信息转换为摩尔斯电码，并通过GPIO输出（您可以将GPIO连接到其他组件，例如继电器来操作无线电台）。  
该库适用于无线电业余爱好者和需要自动摩尔斯电码发送功能的用户，也可用于教学和演示。  

### 功能特点  
- **支持GPIO控制：** 您可以选择任何GPIO引脚作为信号发送器和指示灯。  
- **可调发送速度：** 您可以根据需要设置发送速度（wpm）。  
- **标准摩尔斯电码映射表：** 内置标准摩尔斯电码字典，支持字母、数字和常用符号。  
- **错误处理：** 对于无效字符，将发出错误信号。  

### 如何使用？

#### 步骤 1：下载并放置库  
下载库文件 `AutoMorse.py` 并将其放入 Raspberry Pi Pico 文件目录下的 `lib` 文件夹中。  
![image](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/7e8f5df4-7fd6-4f81-bc99-640456c506d8)  

#### 步骤 2：导入库  
在主脚本中调用库文件：  
```python
from AutoMorse import AutoMorse
```  
![2eca9c5e1978e0578abd742dc57672ca](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/16f9ce9e-f4e0-4f3c-928e-2440792cc70e)  

#### 步骤 3：初始化 AutoMorse 对象  
定义摩尔斯电码传输的参数：  
```python
morse = AutoMorse(buzzer_pin, led_pin, wpm)
```  
`buzzer_pin` 和 `led_pin`分别是蜂鸣器和 LED 的 GPIO 引脚， `wpm` 是每分钟的发送速度。  
![image](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/99fde3f8-71eb-467b-ba3f-42141b9199c5)  

#### 步骤 4：转换和发送摩尔斯电码  
将要发送的消息转换为列表，并使用库进行处理：  
```python
phrase = list(content) 
morse.Morse(phrase)
```  
这里，“content”是要转换的文本消息。 “Morse”方法将处理转换和传输。  
![image](https://github.com/HKEMS-STMO/Fully-automatic-Morse-coder/assets/118874898/5f82e961-a204-45eb-82ca-61073a220618)  

### 错误处理和注释  
- 确保所有字符都是有效的摩尔斯电码字符。对于无效字符，库将发出错误信号。  
- 如果遇到 GPIO 控制问题，请仔细检查引脚连接和配置。  
