
import requests

BASE = "http://127.0.0.1:5000/"

cuber = [{"name": "Zemdegs", "age": 26}]

cuber = requests.put(BASE + "cuber/" + str(0), cuber[0])

response = requests.get(BASE + "cuber/0")