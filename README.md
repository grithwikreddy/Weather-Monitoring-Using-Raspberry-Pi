


# Weather Monitoring System with Raspberry Pi

This project uses a Raspberry Pi to monitor weather conditions using sensors like **DHT22** (for temperature and humidity), **MQ135** (gas sensor), **LDR** (light sensor), and displays the data on an **LCD** screen. The system also includes **LEDs** and a **buzzer** to alert when gas is detected.
![image](https://github.com/user-attachments/assets/069a470a-7ce1-4657-abae-6461bab1b9ef)
## Features

- **DHT22**: Measures temperature and humidity.
- **MQ135 Gas Sensor**: Detects the presence of harmful gases.
- **LDR**: Detects light intensity.
- **LCD Display**: Displays temperature and humidity readings.
- **Buzzer & LED**: Alerts when dangerous gas levels are detected.

## Components

- **Raspberry Pi** (any model with GPIO pins)
- **DHT22 Sensor**
- **MQ135 Gas Sensor**
- **LDR (Light Dependent Resistor)**
- **16x2 I2C LCD Display**
- **LED**
- **Buzzer**
- **Jumper wires and resistors**
## Output
![image](https://github.com/user-attachments/assets/9ff1b4e4-973f-4f7d-996b-a76fa5265083)
## Requirements

- Raspberry Pi with Raspbian OS
- Python 3.x
- Required Python libraries:
  - `RPi.GPIO`
  - `Adafruit_DHT`
  - `smbus2`

