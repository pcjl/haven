import cv2
import json
import sys
import requests
import os
import time

DEVICE_NUMBER = 0
IMAGE_FILE = "output.jpg"
no_face = True

while no_face:	
	vc = cv2.VideoCapture(DEVICE_NUMBER)
	retVal, frame = vc.read()
	small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
	cv2.imwrite(IMAGE_FILE, small)	
	vc.release()

	print("done reading image")

	response = requests.post("http://ec2-18-219-99-191.us-east-2.compute.amazonaws.com:5000/verify",files={"image":open('/home/linaro/Documents/AWS_IOT_Test/output.jpg', 'r')})
	
	print("done web response")

	if response.status_code == 200:
		user = json.loads(response.text)['user']
		confidence = json.loads(response.text)['confidence']	
		
		if confidence > 0.95:
			#homeActions
			first = user.split("-")[0]
			last = user.split("-")[1]			
			print(first + " " + last + " is home")
			
			#filename = sys/class/gpio/gpio36	
			#os.system('./Electronics/turnOnGPIO.sh')
			#filename = sys/class/gpio/gpio12
			#os.system('./Electronics/turnOnGPIO.sh')

			k = raw_input("")
			if k == 'q':
				sys.exit(1)
			#else:
				#filename = ~/sys/class/gpio/gpio36	
				#os.system('./Electronics/turnOnGPIO.sh')
				#filename = ~/sys/class/gpio/gpio12
				#os.system('./Electronics/turnOnGPIO.sh')		

