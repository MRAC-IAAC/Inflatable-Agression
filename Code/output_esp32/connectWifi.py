def connect():
    import network
    import time
    ssid = "your_wifi"
    password = "your_pw"
    
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    for i in range(1):
        try:
            sta_if.connect(ssid, password)
            print(f'Wifi Connection: {sta_if.isconnected()}')
            break
        except OSError:
            print(f'Wifi Connection: {sta_if.isconnected()}')
            pass
        time.sleep(1)
    
    print('network config: ', sta_if.ifconfig())
connect()

