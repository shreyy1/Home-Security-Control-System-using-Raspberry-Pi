# Home-Security-Control-System-using-Raspberry-Pi
This code is designed for a Raspberry Pi-based security system that uses various sensors to detect motion, gas leakage, fire, high temperature, and light conditions. When any of these conditions are detected, the system takes appropriate actions such as sounding a buzzer, sending emails or text messages, and controlling a relay and LED light.

1. **Import Statements:**
   - Various libraries and modules are imported, including `os`, `glob`, `RPi.GPIO`, `smtplib`, `time`, `cv2` (OpenCV), `Adafruit_DHT`, and the necessary email-related classes from the `email` package.

2. **GPIO Setup:**
   - The code sets up the GPIO (General Purpose Input/Output) pins on the Raspberry Pi for various components like PIR motion sensor, gas sensor, fire sensor, relay, buzzer, LED, and light-dependent resistor (LDR).

3. **Functions:**
   - `beep()`: This function activates the buzzer for a short period to create a beep sound.
   - `send_text(body)`: Sends an email with a text message. Captures an image from the camera and attaches it to the email.
   - `send_mail()`: Sends an email with an attached image.
   - `MotionDetect()`: Detects motion using the PIR sensor. If motion is detected, it triggers the `beep()` function and sends an email with an attached image.
   - `GasDetect()`: Detects gas leakage using the gas sensor. If gas is detected, it triggers the `beep()` function and sends a text message.
   - `FireDetect()`: Detects fire using the fire sensor. If fire is detected, it triggers the `beep()` function, activates a relay (possibly for controlling a fire suppression system), and sends a text message.
   - `getTemp()`: Reads temperature and humidity data using the DHT11 sensor. If the temperature is above a certain threshold, it triggers the `beep()` function and sends a text message.
   - `lightDetect()`: Detects ambient light conditions using the LDR. If low light (night) is detected, it turns on an LED.

4. **Main Loop:**
   - The code enters an infinite loop where it repeatedly calls the different detection functions (`MotionDetect()`, `GasDetect()`, `FireDetect()`, `getTemp()`, `lightDetect()`).
   - Depending on the sensor outputs, different actions are taken, such as beeping the buzzer, sending emails or text messages, turning on the LED, etc.

Note that the code seems to rely on the availability of sensors such as PIR motion sensor, gas sensor, fire sensor, DHT11 temperature and humidity sensor, and a camera connected to the Raspberry Pi. Additionally, it uses Gmail's SMTP server to send emails. You would need to have the appropriate hardware connected to the Raspberry Pi and provide valid sender and receiver email addresses and passwords to make the email sending functionality work. The code also appears to be capturing an image and attaching it to emails, so a camera module is expected to be available.
