"""
2025/07/26　2.13にてテストした
"""
import numpy as np
import RPi.GPIO as GPIO
import raspberrypi_epd
import logging
from bdfparser import Font

# Ejemplo de conexion
# BUSY          GPIO4
# RES           GPIO17
# D/C           GPIO27
# CS            GPIO22
# SCK           GPIO11 (SPI0 SCK)
# SDATA         GPIO10 (SPI0 MOSI)
# GND
# VCC
GPIO.setmode(GPIO.BCM)



def draw_text():
    display = raspberrypi_epd.WeAct213(busy=4, reset=17, dc=27, cs=22)
    display.init()
    display.fill(raspberrypi_epd.Color.WHITE)
    display.refresh(False)
    display.set_rotation(270)
    display.set_font('fonts/helvB14.bdf')
    display.draw_text('Raspberry', 10, 0, raspberrypi_epd.Color.BLACK)
    display.draw_text('Raspberry', 20, 30, raspberrypi_epd.Color.BLACK)
    display.draw_text('Raspberry', 30, 60, raspberrypi_epd.Color.BLACK)
    display.draw_text('Raspberry', 40, 90, raspberrypi_epd.Color.BLACK)
    display.write_buffer()
    display.close()


def main():
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info("Initializing display")
    # test_drawing()
    draw_text()



if __name__ == '__main__':
    main()
