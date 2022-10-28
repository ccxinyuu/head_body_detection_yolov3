from detect import * 
import subprocess
# importing OpenCV library
import cv2
import os  
from time import time
import paho.mqtt.client as mqtt

previous = time()
delta = 0

path = 'C:\\Users\\Cui Xinyu\OneDrive - National University of Singapore\Desktop\cs3237\\project'
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(0) #change number to access different camera

# reading the input using the camera
seconds = 3

    
def run_command():
    # r = subprocess.Popen(['python', 'detect.py', '--source', '..\\test3237.png'], stdout=subprocess.PIPE)
    os.system("python detect.py --source ..\\test3237.png")

#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('cs3237/test')

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def send_signal():
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

    client.loop_start() 
    

if __name__ == '__main__':
    while True:
        current = time()
        delta += current - previous
        previous = current

        if delta > seconds:
            result, image = cam.read()
            # saving image in local storage
            cv2.imwrite(os.path.join(path, "test3237.png"), image)
            # If keyboard interrupt occurs, destroy image 
            delta = 0
            run_command()
            send_signal()

    