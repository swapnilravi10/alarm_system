from boltiot import Bolt,Sms
import json, conf, time

mybolt = Bolt(conf.api_key,conf.device_id)
sms = Sms(conf.SID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)

threshold = 10

#function to turn on buzzer
def intruder():
	mybolt.digitalWrite('1','HIGH')
	mybolt.digitalWrite('2','LOW')

while True:
	#reading LDR data
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	current_voltage = int(data['value'])
	print(current_voltage)
	try:
		if current_voltage < threshold:
			print('current voltage dropped')
			intruder()
			print('Sending SMS via twilio')
			response = sms.send_sms('ALERT....Vault opened')
			print(str(response.status))
	except Exception as e:
		print('Error: ', e)
	time.sleep(30)
