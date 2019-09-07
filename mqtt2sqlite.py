import paho.mqtt.subscribe as subscribe

topics = ['outTopic','smoker/temp','smoker/WiFi/#']

while True:
    msg = subscribe.simple(topics, hostname="tanukimario.mushroomkingdom", retained=False, msg_count=2) #in order not to miss any messages you will want msg_count to equal the max number of messages you expect to be sent at once.
    for message in msg:
        if message.topic == "smoker/temp":
            tempC = int(message.payload)
            tempF = 9.0/5.0 * int(message.payload)+32
            print(f'{message.topic}:{tempC}° C')
            print(f'{message.topic}:{tempF}° F')
        else:
            print(f'{message.topic}:{message.payload}')
