import paho.mqtt.client as mqtt

#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('cs3237/test')

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def main():
    client = mqtt.Client()

    # Specify callback function
    client.on_connect = on_connect
    client.on_message = on_message

    # Establish a connection
    client.connect('broker.emqx.io', 1883, 60)
    client.username_pw_set("cs3237", "public")
    # Publish a message
    with open("detection_result.txt", "r") as f:
        output =  f.read()
        client.publish('cs3237/test',payload = output ,qos=0)

    client.loop_forever()

if __name__ == '__main__':
    main()