## Notes

The scripts on the ESP32 side uses micropython. Due to limitations of importing libraries such as paho-mqtt, mqtt.py had to be placed inside the ESP32 to be called out in the main.py as functions. 
The mqtt.py file is from the link below: 
https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/MQTT/umqttsimple.py

Wifi connection could be performed in the main.py, but we chose to put it in the separate python file to simply call out the function. 

esp32_button_with_timelimit.py is to run the buttons prior to the mqtt signal setup. esp32_mqtt.py is the final product, connected with the raspberry pi. 
