#!/usr/bin/env python3

from pyjstat import pyjstat #pystat library
import collections
import unittest
import sys
import io
import unittest.mock

# UNIT TESTS


class MyTests(unittest.TestCase):

	@unittest.mock.patch('sys.stdout',new_callable=io.StringIO)
	def setUp(self,mock_stdout):

		print_countries(3)
		self.output = mock_stdout.getvalue()
		self.out = self.output.split("\n")

		self.wanted_output = "Norway\nKorea\nSwitzerland\nSpain\nGreece\nSlovak Republic\n"
		self.wanted_out = self.wanted_output.split("\n")

	def test_norway(self):
		self.assertEqual(self.out[0],self.wanted_out[0])#Norway

	def test_korea(self):
		self.assertEqual(self.out[1],self.wanted_out[1])#Korea

	def test_switzerland(self):
		self.assertEqual(self.out[2],self.wanted_out[2])#Switzerland

	def test_spain(self):
		self.assertEqual(self.out[3],self.wanted_out[3])#Spain

	def test_greece(self):
		self.assertEqual(self.out[4],self.wanted_out[4])#Greece

	def test_slovak_republic(self):
		self.assertEqual(self.out[5],self.wanted_out[5])#Slovak Republic

	def test_all(self):
		self.assertEqual(self.output,self.wanted_output)

	def test_count(self):
		self.assertEqual(len(self.out),len(self.wanted_out))


#-----------------------------------------------------------------------

# Function print_max_in have 3 parametres
# 1. param is count for printing "how many countries u want print" 
# 2. param is dict with flag and value of avg
# 3. param is dict with flag like key and value is name of country 
def print_max_min(count,dict_flags_vals,dict_flag_countries):
	#print("lowest:")
	try:
		for c in range(count):
			flag = (list((dict_flags_vals).keys())[c][1])
			print(dict_flag_countries[flag])
	except:
		sys.exit(-1)
	#print("highest")
	try:
		for c in range(count):
			flag2 = (list((dict_flags_vals).keys())[-(c+1)][1])
			print(dict_flag_countries[flag2])
	except:
		sys.exit(-1)

def print_countries(count):
	url = 'https://json-stat.org/samples/oecd.json'

	try:
		data = pyjstat.Dataset.read(url)
	except:
		print("Problem with the Internet connection!")
		sys.exit(-1)

	values = (data["value"])
	number_of_years = len(data["dimension"]["year"]["category"]["index"])
	countries = (data["dimension"]["area"]["category"]["index"])
	countries_name = (data["dimension"]["area"]["category"]["label"])


	clear_countries = [] # data containts EU and organizations which are not states
	index_nonstate = []

	for country in enumerate(countries):

		if(len(country[1]) == 2 ):# is country, every state have length 2(CZ,UK..)
			clear_countries.append(country)
		else:
			del countries_name[country[1]]
			index_nonstate.append(country[0])

	list_val_countries = []
	start = 0
	end = number_of_years

	while end != len(values):

		tmp = values[start:end]
		tmp = sum(tmp)/number_of_years
		list_val_countries.append(tmp)

		start = end
		end += number_of_years # number_of_years is step

	countries_avg = dict(zip(clear_countries,(list_val_countries)))
	sorted_coutries = dict(sorted(countries_avg.items(), key=lambda item: item[1]))

	print_max_min(count,sorted_coutries,countries_name)


if __name__ == '__main__':
	print_countries(3)
	unittest.main()


