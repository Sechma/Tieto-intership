#!/usr/bin/env python3

from pyjstat import pyjstat #pystat library



from requests.exceptions import ConnectionError 
url = 'https://json-stat.org/samples/oecd.json'

try:
	data = pyjstat.Dataset.read(url)
except  ConnectionError as err:
	print(err)
	sys.exit(-1)

values = (data["value"])

years = (data["dimension"]["year"]["category"]["index"])
number_of_years = (len(years))

print(number_of_years)
countries = (data["dimension"]["area"]["category"]["index"])
#print(countries)


for country in enumerate(countries):
	if(len(country[1]) == 2 ):# is country
		print(country[1])
		print(country[0])
		for val in enumerate(values):
			print(val)


