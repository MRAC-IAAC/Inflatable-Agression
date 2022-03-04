import mqtt as mqtt
import time
import machine
import micropython
import sys
import connectWifi                          
import ubinascii
import esp

connectWifi.connect()
mqtt_broker = "your_rpi_address" 
broker_port = 1883

current_topic = ''
previous_topic = ''
def on_message(topic, message):
    global current_topic
    print("Message Received: "+ str(topic.decode()) + ": " + str(message))
    # Do something here with the message
    current_topic = topic.decode()
    #print(current_topic)
 

client = mqtt.MQTTClient("pico", mqtt_broker, broker_port,
                         user=None, password=None)
client.set_callback(on_message)


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
    resp = client.connect()
    print("Connected: " + str(resp))
except OSError as e:
    print("Could not connect!")
    restart_and_reconnect()

#subscribe to topic
client.subscribe("air_out",qos=1)
client.subscribe("air_in",qos=1)


#solenoid setups
solenoid = machine.Pin(12, machine.Pin.OUT)
dc_air = machine.Pin(14, machine.Pin.OUT)

#to see connection status from publisher side
#set time for counting
start = time.time()
solenoid_timer = 0.5
dc_timer = 12.0

while True:
    try:
        client.check_msg()
        #print("in wait loop")
        time.sleep(1) 
        #print("in main loop!")
    except OSError as e:
        restart_and_reconnect()
    
    solenoid.value(1)
    dc_air.value(1)

    if previous_topic != current_topic:
        previous_topic = current_topic
        start = time.time()
        
    if current_topic == 'air_in':
        print('Ready to blow up')
        pressed = time.time()
        if previous_topic == current_topic: 
            elapsed = pressed - start
        if current_topic == 'air_out':
            print(f'WAIT! Stop Air In')
            solenoid.value(1)
        elif elapsed <= solenoid_timer and current_topic != 'air_out':
            solenoid.value(0)
            print(f'Air In: {elapsed}')
        elif elapsed > solenoid_timer:
            solenoid.value(1)
            print(f'STOP Air In')
            
        else:
            solenoid.value(1)
            print('STOP Air In')
            
    elif current_topic == 'air_out':
        print('Okay, let go')
        pressed = time.time()
        elapsed = pressed - start
        if elapsed <= dc_timer:
            dc_air.value(0)
            print(f'Air out: {elapsed}')
        elif elapsed <= dc_timer and current_topic == 'air_in':
            dc_air.valve(1)
            print(f'STOP Air Out')
        else:
            dc_air.value(1)
            print(f'STOP Air out')
    else:
        solenoid.value(1)
        dc_air.value(1)

        