from machine import Pin
import dht
import time

d = dht.DHT22(Pin(2))

while True:
    print("Measuring.")
    retry = 0
    while retry < 3:
        try:
            d.measure()
            break
        except:
            retry = retry + 1
            print(".", end = "")

    print("")
    if retry < 3:
        temp = d.temperature()
        hum = d.humidity()
        print('Humidity: {}%'.format(hum))
        print('Temperature: {}{}C'.format(temp, '\u00b0'))
    time.sleep(5)
