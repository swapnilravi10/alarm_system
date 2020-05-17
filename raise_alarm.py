from boltiot import Bolt,Sms
from alarm_system import  conf

mybolt = Bolt(conf.api_key,conf.device_id)
sms = Sms(conf.SID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)

def intruder():
    mybolt.digitalWrite('1', 'HIGH')
    mybolt.digitalWrite('2', 'LOW')
    print('Sending SMS via twilio')
    response = sms.send_sms('Intruder ALERT....Check email for captured photos')
    print(str(response.status))