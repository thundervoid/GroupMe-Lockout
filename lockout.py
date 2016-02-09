import time
import json
import requests
import ConfigParser

def main():
	# Read config file
	config = ConfigParser.RawConfigParser()
	config.readfp(open('key.cfg'))
	
	GROUP_ID = "12676716"
	BASE_URL = "https://api.groupme.com/v3/groups/"
	ACCESS_TOKEN = config.get('key', 'api')
	
	FORMATTED_URL_MEMBERS = BASE_URL + GROUP_ID + "/" + "members/" 

	while True:
		try:
			message_request = requests.get(url=BASE_URL+GROUP_ID+'/messages', params={'token':ACCESS_TOKEN, 'limit':30}).content
			member_request = requests.get(url=BASE_URL+GROUP_ID, params={'token':ACCESS_TOKEN, 'limit':30}).content
			
			messages = json.loads(message_request)
			members = json.loads(member_request)["response"]["members"]

			print "MESSAGE REQUEST: ", message_request
			print "MEMBER REQUEST: ", member_request
		except:
			pass
		
		if not members:
			print "Error fetching."
			pass
		else:
			for member in members:
				if (member["nickname"] == "Alfred") or (member["nickname"] == "Jav - EN"):
					try:
						response = requests.post(url=FORMATTED_URL_MEMBERS+str(member["id"])+"/remove", params={'token':ACCESS_TOKEN, 'limit':30})
						print response.content
						print "Removed: ", member["nickname"]
					except requests.exceptions.RequestException as err:
						print err
					except:
						pass
				if member["nickname"] == "Test":
					try:
						response = requests.post(url=FORMATTED_URL_MEMBERS+str(member["id"])+"/remove", params={'token':ACCESS_TOKEN, 'limit':30})
						print response.content
						print "Removed: ", member["nickname"]
					except requests.exceptions.RequestException as err:
						print err
					except:
						pass

			print "Not in group..."

		time.sleep(2)

if __name__ == "__main__":
	main()

