import requests
from bs4 import BeautifulSoup
import os

count = 0

web = input("What website do you want to scrape images off? ")
r = requests.get(web)
data = r.text
soup = BeautifulSoup(data, 'lxml')
shortlink = web.split("/")[2]
fullshort ="http://" + shortlink
question_mark = "?"

for link in soup.find_all('img'):
	try:
		image = link.get('src')
		if "http" not in image:
			image = fullshort + image
		image.split(question_mark, maxsplit=1)[0]
		image_name = os.path.split(image)[1]
		image_name = image_name.split(question_mark, maxsplit=1)[0]
		r2 = requests.get(image)
		print(image_name)
		count+=1
		with open(image_name, 'wb') as f:
			f.write(r2.content)
	except:
		continue
print("--------")
print("--------")
print("--------")
print("Total images downloaded:", count)
print("--------")
print("--------")
print("--------")

input("Press ANY KEY to Exit.") 
