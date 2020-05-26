from boltiot import Bolt,Sms
from alarm_system import  conf
import smtplib, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


mybolt = Bolt(conf.api_key,conf.device_id)
sms = Sms(conf.SID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)

def alarm():
	mybolt.digitalWrite('1', 'HIGH')
	mybolt.digitalWrite('2', 'LOW')
	print('Sending SMS via twilio')
	try:
		response = sms.send_sms('Intruder ALERT....Check email for captured photos')
		print(str(response.status))
	except:
		print("Error sending sms",str(sys.exc_info()))

def sendEmail(image):
	try:
		print("Sending email")
		msgRoot = MIMEMultipart('related')
		msgRoot['Subject'] = 'Security Update'
		msgRoot['From'] = conf.fromEmail
		msgRoot['To'] = conf.toEmail
		msgRoot.preamble = 'Security system alert'

		msgAlternative = MIMEMultipart('alternative')
		msgRoot.attach(msgAlternative)
		msgText = MIMEText('Smart security cam found object')
		msgAlternative.attach(msgText)

		msgText = MIMEText('<img src="cid:image1">', 'html')
		msgAlternative.attach(msgText)

		msgImage = MIMEImage(image)
		msgImage.add_header('Content-ID', '<image1>')
		msgRoot.attach(msgImage)

		smtp = smtplib.SMTP('smtp.gmail.com', 587)
		smtp.starttls()
		smtp.login(conf.fromEmail, conf.fromEmailPassword)
		smtp.sendmail(conf.fromEmail, conf.toEmail, msgRoot.as_string())
		smtp.quit()

		print("Done sending email")

	except:
		print("Error sending email: ", str(sys.exc_info()))