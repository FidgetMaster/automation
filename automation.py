import cv2
import time
import random
start_time = time.time()
def Task():
    task = "Hello World!"
    print(task)
    return task
def Main():
    while(True):
        if((time.time() - start_time) >= 20):
           Task()
Main()