from boltiot import Bolt,Sms
import json, time, pickle, cv2
from alarm_system import conf, Facerecognition_identification

mybolt = Bolt(conf.api_key,conf.device_id)

threshold = 15

while True:
	#reading LDR data
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	current_voltage = int(data['value'])
	print(current_voltage)
	try:
		if current_voltage < threshold:
			print('current voltage dropped')
			Facerecognition_identification.camera()
	except Exception as e:
		print('Error: ', e)
	time.sleep(30)
