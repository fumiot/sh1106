‘’‘
Test hardware : esp32 board with SPIRAM，OLED wiring:  SCL -- IO32  ，   SDA -- IO33 ， VCC -- 3.3V ， GND -- GND  
代码对应的硬件连线： esp32核心板(带SPIRAM）, OLED屏连接4根线： SCL -- IO32  ，   SDA -- IO33 ， VCC -- 3.3V ， GND -- GND
’‘’

import utime
from machine import Pin,I2C  
from sh1106 import SH1106_I2C
import framebuf
#modify SCL、SDA pin number according to hardware wiring.
#按照硬件实际连线，修改SCL和SDA信号的引脚
i2c0= I2C(0, scl=Pin(33),sda=Pin(32),freq=400000)

oled = SH1106_I2C(132,64,i2c0)
utime.sleep_ms(500)
oled.fill(0)  #0 for dark, 1 for bright.

framebuf.set_font_path(framebuf.FONT_HZK16,'/data/pyamp/HZK16')
oled.text('孚沁科技',20,0,font=framebuf.FONT_HZK16)
             
#横坐标的范围跟硬件连线有关，SH1106/CH1116控制芯片支持132点宽度，测试用的屏实际连线在2-129,共128个点。
#可以使用oled.fill_rect(x=2,y=0,w=1,h=8,1)这样的代码,观察边缘点亮情况确定横坐标的有效范围。
oled.text('github/forchine',2,18)
oled.show()


    
