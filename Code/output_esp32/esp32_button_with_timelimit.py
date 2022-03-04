import machine
import time

button1 = machine.Pin(16, machine.Pin.OUT)
button2 = machine.Pin(17, machine.Pin.OUT)

solenoid1 = machine.Pin(12, machine.Pin.OUT)
solenoid2 = machine.Pin(14, machine.Pin.OUT)

solenoid1.value(1)
solenoid2.value(1)

#loop time, air_in limit, air_out limit
t = 0.5
air_in = 3
air_out = 6

start = time.time()
while True:
    time.sleep(0.5)
    if button1.value():
        pressed = time.time()
        elapsed = pressed - start
        if elapsed <= air_in:
            solenoid1.value(0)
            print(f'solenoid1 ON: {elapsed}')
        if elapsed > air_in:
            solenoid1.value(1)
            print('solenoid1 STOP')

    elif button2.value():
        pressed = time.time()
        elapsed = pressed - start
        if elapsed <= air_out:
            solenoid2.value(0)
            print(f'solenoid2 ON: {elapsed}')
        if elapsed > air_out:
            solenoid2.value(1)
            print('solenoid2 STOP')
            
    else:
        start = time.time()
        solenoid1.value(1)
        solenoid2.value(1)
        print('silence')
        
