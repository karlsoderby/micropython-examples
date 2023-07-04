import urequests
import network

# Request a random cat fact from the Meowfacts API
url = "https://meowfacts.herokuapp.com/"

SSID=''
KEY=''

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, KEY)

print("Connected to ",SSID)

response = urequests.get(url)

print(response.text)