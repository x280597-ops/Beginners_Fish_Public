from machine import Pin, SPI
import st7789


spi = SPI(
    0,
    baudrate=40000000,
    polarity=1,
    phase=1,
    sck=Pin(18),
    mosi=Pin(19)
)


display = st7789.ST7789(
    spi,
    240,
    240,
    dc=Pin(16),
    rst=Pin(17),
    cs=Pin(20)
)


display.init()

display.fill(st7789.RED)