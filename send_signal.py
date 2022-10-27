from detect import * 
import subprocess
# importing OpenCV library
import cv2
import os  
from time import time

previous = time()
delta = 0

path = 'C:\\Users\\Cui Xinyu\OneDrive - National University of Singapore\Desktop\cs3237\\project'
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(1) #change number to access different camera

# reading the input using the camera
seconds = 3

    
def run_command():
    # r = subprocess.Popen(['python', 'detect.py', '--source', '..\\test3237.png'], stdout=subprocess.PIPE)
    os.system("python detect.py --source ..\\test3237.png")
    

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

    