
import requests
import json
import time
import subprocess


key="YOUR_KEY"
 
url = f'https://api.ipgeolocation.io/ipgeo?apiKey={key}'

headers = {'Accept': 'application/json'}
 

while 1:

	req = requests.get(url, headers=headers)
	js =req.json()

	ip=0
	country=''

	for key, value in js.items():
		if (key == 'ip'):
	 		ip=value 		
		elif (key == 'country_name'):
	 		country=value
	 		
	subprocess.run(["/usr/bin/notify-send", "--icon=error", country]) #making notification in linuxe
	time.sleep(10) #per second 		
#Programmed by MDshirzad
