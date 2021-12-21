import os

import requests

BASE = "http://127.0.0.1:5000/"

data = [{"Name": "11m pro", "Magnetic": True, "Size":56, "Brand":"GAN", "Cuber":0},
        {"Name": "RS3m", "Magnetic": True, "Size":55, "Brand":"Moyu", "Cuber":0},
        {"Name": "356xs", "Magnetic": True, "Size":56, "Brand":"GAN", "Cuber":0},
        ]

cuber = [{"name": "Zemdegs", "age": 26, "cuber_id": 0}]

cube = requests.put(BASE + "cuber/" + str(0), cuber[0])

for i in range(0, len(data)):
    adding = requests.put(BASE + "cubing/" + str(i), data[i])
    print(adding.json())
input()



response = requests.get(BASE + "cubing/1")
for row in response:
    print(row)


os.remove("database.db")