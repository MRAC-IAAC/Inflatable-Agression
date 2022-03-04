# Inflatable-Aggression

This repo contains a set of instructions and requirements for the project Inflatable-Aggression//H2. The goal of this seminar is to understand different types of sensors and measurement principles, as well as data logging processs in real time and with buffers. This project is inspired by the potential of using softer and more flexible materials to exercise security and privacy, looking at the architecture of modern doors and considering how to re-shape them. For the input side, a camera Raspberry Pi Camera Module 2 detects the presence of a person, signals the other microcontroller to inflate the balloons until it detects a 'smile'. 

![GIF_0861](https://user-images.githubusercontent.com/96722124/156718527-369ac224-2ae1-4a01-8368-7b5e369056eb.gif)
## Components
The project comprises of two parts: input from Raspberry Pi Camera + Raspberry Pi output to ESP32 + Solenoid/DC Air Pump.The signal between the input and the output microcontroller is done by Mosquitto, thus it is required to use microcontrollers that can integrate WiFi. The scripts for the input are in Python3, whereas the output are in micropython. 
![components_2-01](https://user-images.githubusercontent.com/96722124/156724167-726de712-7b4b-4581-9f9f-efae88abe611.png)

  ### Requirements/Setup for Input
  The processing happens in the Raspberry Pi. The following installations are required for the Pi to be its own operating system, and be able to execute the python scripts. 
    Install Bullseye 64 bit
    Install zram
    SSH on 
    Wireless LAN updated
    Install OpenCV - build from source
    Install mosquitto-clients
    Install paho-mqtt
    Smile_recognition.py onto RPi
    $ Mosquitto -c MQTT/mosquitto.comf -d $ python smile_recognition.py

  ### Requirements/Setup for Output
  To test air pressure and the limits of the material (in this case, balloons), we used buttons. The wiring and setup of the buttons are separated in from the relay in the way that other input signals can be received later on. Bill of Materials are provided on the folders above for the prototype. Note that some requirements may change depending on the solenoid (such as tube sizes), but it is ideal to purchase a DC vacuum pump with the same voltage. 
  
  <img src="https://user-images.githubusercontent.com/96722124/156730054-d4a54719-0c00-4e52-8957-4151706456c9.png" width ="700" height = "500">

 
