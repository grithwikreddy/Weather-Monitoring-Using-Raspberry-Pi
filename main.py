import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from smbus2 import SMBus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DHT_PIN = 4
GAS_SENSOR_PIN = 17
LDR_PIN = 27
BUZZER_PIN = 22
LED_PIN = 23

I2C_ADDR = 0x27
LCD_WIDTH = 16
LCD_CHR = 1
LCD_CMD = 0
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
ENABLE = 0b00000100

DHT_SENSOR = Adafruit_DHT.DHT22
GAS_THRESHOLD = 300

GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

bus = SMBus(1)

def lcd_init():
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(0.0005)

def lcd_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | 0x08
    bits_low = mode | ((bits << 4) & 0xF0) | 0x08
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, bits | ENABLE)
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, bits & ~ENABLE)
    time.sleep(0.0005)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def read_dht22():
    return Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

def read_gas_sensor():
    return GPIO.input(GAS_SENSOR_PIN)

def read_ldr():
    return GPIO.input(LDR_PIN)

def main():
    lcd_init()
    while True:
        humidity, temperature = read_dht22()
        gas_detected = read_gas_sensor()
        light_level = read_ldr()
        lcd_string(f"T: {temperature:.1f}C", LCD_LINE_1)
        lcd_string(f"H: {humidity:.1f}%", LCD_LINE_2)
        if gas_detected:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.LOW)
        if light_level:
            print("Light detected")
        else:
            print("Darkness detected")
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        lcd_string("Goodbye!", LCD_LINE_1)
        GPIO.cleanup()
