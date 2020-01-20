import time
import board
import neopixel
import RPi.GPIO as GPIO

# Pino de conexao Raspberry = 18
pixel_pin = board.D18

# Numero de leds que serao controlados
num_pixels = 16

# Tempo do sinal em segundos
signal_time = 2

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, 
    brightness=1, auto_write=False,
    pixel_order=neopixel.GRB)

pixels.fill((255, 255, 255))
pixels.show()
time.sleep(signal_time)
pixels.fill((0,0,0))
pixels.show()
GPIO.cleanup()