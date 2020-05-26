# alarm_system
Alarm System for your personal vault at home.

<b>Objective</b>

The basic idea behind the project is to alert the user about intrusion or invalid access to their vault. The system will turn on a alarm, send a SMS and an email immediately to the owner. Incase of accidental alarm or otherwise to turn off the alarm owner can make use of google assistance to turn of alarm from any where.

Components and Setup-

The components of the alarm system are:

Hardware:

1.LDR

2.Buzzer

3.Jumper wires

4.Male-Female wires

5.Bolt iot module(used for this project)

Software:

1.Twillio(for free SMS)

2.IFTTT(to set up Google Assistance)

Setup:

I have used breadboard to make a connection since this is not the final setup. An advancement to this project will made. 
Setting up the buzzer you will require the use of male-female wires. Connect the buzzer to female end of the wire and connect the other end of wire with the positive end of buzzer to pin1 of bolt iot module and the negative end of buzzer to pin 2 of the module
Setting up the LDR. Place the LDR on the breadboard and connect one end of the LDR to pin A0 and the other to pin ground or GND of teh bolt using jumper wires respectively.
Setup to twillio and IFTTT can be easily found over internet and is too long to explain in words. A link to my hackster.io https://www.hackster.io/swapnilravi10/alarm-system-4489a3 explains an detailed setup of IFTTT

Working:

The working of the project is simple. When the LDR senses a change in the light it immediately causes the alarm to raise and send internally triggers the Twillio to send an SMS to registerted number. 
To turn off the buzzer use your phones google assistance and just the the phrase "Turn off the alarm" or "Turn off the buzzer" to let buzzer off.

Advancement:

This setup will make use of additional components to capture an image and send an email to registered user as a proof of intrusion.
