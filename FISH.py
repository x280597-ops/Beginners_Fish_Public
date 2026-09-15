from machine import Pin, SPI
from machine import Pin, I2C
import time
import st7789
import math
def color565(r, g, b):
    return (
        ((r & 0xf8) << 8) |
        ((g & 0xfc) << 3) |
        (b >> 3)
    )
BLACK = color565(0,0,0)
WHITE = color565(255,255,255)
YELLOW = color565(255,255,0)
RED   = color565(255,0,0)
GREEN = color565(0,255,0)
BLUE  = color565(0,0,255)
class Display():
    def __init__(self):
        self.spi = SPI( 0,baudrate=40000000,polarity=1,phase=1,sck=Pin(18),mosi=Pin(19))
        self.display = st7789.ST7789(self.spi,240,240,dc=Pin(16, Pin.OUT),rst=Pin(17, Pin.OUT))
    def fill(self,color):
        self.display.fill(color)
    def pixel(self,start_x,start_y,color):
        self.display.pixel(start_x,start_y, color)
    def line(self,start_x,start_y,end_x,end_y,color):
        self.display.line(start_x,start_y,end_x,end_y ,color)
    def h_line(self,start_x,start_y,length,color):
        self.display.hline(start_x,start_y,length,color)
    def v_line(self,start_x,start_y,length,color):
        self.display.vline(start_x,start_y,length,color)
    def rect(self,start_x,start_y,end_x,end_y,color):
        self.display.fill_rect(start_x,start_y,end_x,end_y ,color)
    def set_display(self):
        pass
    def clear(self):
        self.display.fill(st7789.BLACK)
    def text(self,text,start_x,start_y,color,text_scale):
        self.display.text(text,start_x,start_y,color,scale=text_scale)
class Button():
    def __init__(self):
        self.button_1 = Pin(14, Pin.IN, Pin.PULL_UP)
        self.button_2 = Pin(15, Pin.IN, Pin.PULL_UP)
        self.button_reset=Pin(13, Pin.IN, Pin.PULL_UP)
        self.button_start=Pin(12, Pin.IN, Pin.PULL_UP)
    def r_push(self):
        if self.button_2.value() == 0:
            flug=True
        else:
            flug=False
        return flug
    def l_push(self):
        if self.button_1.value() == 0:
            flug=True
        else:
            flug=False
        return flug
    def reset_btn(self):
        if self.button_reset.value() == 0:
            flug=True
        else:
            flug=False
        return flug
    def start_btn(self):
        if self.button_start.value() == 0:
            flug=True
        else:
            flug=False
        return flug
class Sensor():
    def __init__(self):
        self.i2c_temp = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)
        self.i2c_gyro = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)
        self.ADDR_temp = 0x44
        self.ADDR_gyro = 0x68
        
        #温湿度
        self.i2c_temp.writeto(self.ADDR_temp, b'\x24\x00')
        self.i2c_gyro.writeto_mem(self.ADDR_gyro,0x6B,b'\x00')
    def read_raw_data(self,addr):
        self.data = self.i2c_gyro.readfrom_mem(self.ADDR_gyro,addr,2)
        value = (self.data[0] << 8) | self.data[1]
        # 16bit signed
        if value >= 32768:
            value -= 65536

        return value
    def read_temp_hum(self):
        self.i2c_temp.writeto( self.ADDR_temp, b'\x24\x00')
        time.sleep_ms(20)
        data = self.i2c_temp.readfrom(self.ADDR_temp, 6 )
        temp_raw = (data[0] << 8) | data[1]
        hum_raw = (data[3] << 8) | data[4]
        temperature = -45 + 175 * temp_raw / 65535
        humidity = 100 * hum_raw / 65535
        return round(temperature, 2), round(humidity, 2)
    def temp(self):
        temperature, humidity = self.read_temp_hum()
        return temperature
    def hum(self):
        temperature, humidity = self.read_temp_hum()
        return humidity
    def gyro(self):
        # ジャイロ
        gx = self.read_raw_data(0x43)
        gy = self.read_raw_data(0x45)
        gz = self.read_raw_data(0x47)
        return gx,gy,gz
    def accel(self):
         # 加速度
         ax = self.read_raw_data(0x3B)
         ay = self.read_raw_data(0x3D)
         az = self.read_raw_data(0x3F)
         return ax,ay,az
    def gyro_switch(self):
        ax = self.read_raw_data(0x3B)
        ay = self.read_raw_data(0x3D)
        az = self.read_raw_data(0x3F)
        angle_x = math.atan2(ay, az) * 180 / math.pi
        angle_y = math.atan2(ax, az) * 180 / math.pi
        angle_z = math.atan2(ax, ay) * 180 / math.pi
        switch_x=False
        switch_y=False
        switch_z=False
        if (angle_x > 0):
            switch_x=True
        if (angle_y > 0):
            switch_y=True
        if (angle_z > 0):
            switch_z=True
        return switch_x,switch_y,switch_z
        
    def gyro_list(self,rate):
        ax = self.read_raw_data(0x3B)
        ay = self.read_raw_data(0x3D)
        az = self.read_raw_data(0x3F)
        angle_x = math.atan2(ay, az) * 180 / math.pi
        angle_y = math.atan2(ax, az) * 180 / math.pi
        angle_z = math.atan2(ax, ay) * 180 / math.pi
        if (angle_x > rate):
            sw_x=1
        elif (angle_x < -rate):
            sw_x=-1
        else:
            sw_x=0
        if (angle_y > rate):
            sw_y=1
        elif (angle_y < -rate):
            sw_y=-1
        else:
            sw_y=0
        if (angle_z > rate):
            sw_z=1
        elif (angle_z < -rate):
            sw_z=-1
        else:
            sw_z=0
       
        sw_list=[sw_x,sw_y,sw_z]
        return sw_list