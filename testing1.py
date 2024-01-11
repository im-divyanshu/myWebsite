import requests
response=requests.get("https://worldtimeapi.org/api/timezone/Asia/Kolkata")
response=response.json()
hour=response["datetime"][11:13]
minute=response["datetime"][14:16]
if int(hour)>7 and int(hour)<20:
    print("Day Time")
else:
    print("Night Time")
print(hour,minute)