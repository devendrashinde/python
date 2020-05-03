# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://localhost:10500/auth/v1/authentication/user-accounts/authenticate-requests"

REQUEST = {
	"username": "activeBroker",
	"password": "Passw0rd!"}

HEADERS={
        "content-type":"application/json",
        "sbsChannel": "BROKER",
        "sbsBrand": "SBS",
        "sbsReference": "12345",
        "accept": "application/json"}
  
# sending get request and saving the response as response object 
r = requests.post(url = URL, data = REQUEST, headers= HEADERS)

print(r.status_code)
  
# extracting data in json format 
RESPONSE = r.text 
  
#latitude = data['results'][0]['geometry']['location']['lat'] 
#longitude = data['results'][0]['geometry']['location']['lng'] 
#formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
print("URL:%s\nREQUEST:%s\nRESPONSE:%s"
      %(URL, REQUEST,RESPONSE))
