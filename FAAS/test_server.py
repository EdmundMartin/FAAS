import requests
from random import randint

while True:
	rand_num = randint(5, 250)
	r = requests.get('http://localhost:8080/faas/{}'.format(rand_num))
	print(rand_num, r.text)