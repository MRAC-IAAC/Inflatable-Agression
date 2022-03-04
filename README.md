# Inflatable-Aggression

This repo contains a set of instructions and requirements for the project Inflatable-Aggression//H2. The goal of this seminar is to understand different types of sensors and measurement principles, as well as data logging processs in real time and with buffers. This project is inspired by the potential of using softer and more flexible materials to exercise security and privacy, looking at the architecture of modern doors and considering how to re-shape them. For the input side, a camera Raspberry Pi Camera Module 2 detects the presence of a person, signals the other microcontroller to inflate the balloons until it detects a 'smile'. 

![GIF_0861](https://user-images.githubusercontent.com/96722124/156718527-369ac224-2ae1-4a01-8368-7b5e369056eb.gif)


## Components
The project comprises of two parts: input from Raspberry Pi Camera + Raspberry Pi output to ESP32 + Solenoid/DC Air Pump.The signal between the input and the output microcontroller is done by Mosquitto, thus it is required to use microcontrollers that can integrate WiFi. 
![components_1](https://user-images.githubusercontent.com/96722124/156721960-82e25bf9-4028-41e0-9783-eda28dd324d4.png)

  ### Requirements/Setup for Input

  ### Requirements/Setup for Output
