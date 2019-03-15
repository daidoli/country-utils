import json, sys, pdb
from operator import itemgetter


def main():
	cities = []
	with open('cities15000.txt') as f:
		while True:
			line = f.readline()
			if not line:
				break
			tokens = line.split('\t')
			cities.append({'names': tokens[3], 'country_code': tokens[8], 'population': int(tokens[14])})
	#print(len(cities))

	countries = {}
	with open('countryInfo.txt') as f:
		while True:
			line = f.readline()
			if not line:
				break
			if line[0] == '#':
				continue

			tokens = line.split('\t')
			countries[tokens[0]] = tokens[4]
	#print(countries)

	if sys.argv[1] == '-f':
		with open('./%s' % sys.argv[2]) as file:
			lines = file.readlines()

		key = ''
		for line in lines:
			line = line.strip()
			if line:
				if ':' in line:
					key = line[:-1]
					print(key)
				else:
					for name in line.split(','):
						name = name.strip()
						candidates = []
						for city in cities:
							"""
							if name == city['name_ascii']:
								country_code = city['country_code']
								country_name = countries[country_code]
								print('    %s, %s, %s' % (country_code, name, country_name))
								#result[key].add(city['country_code'])
								found = True
								break
							elif name in city['names']:
								candidates.append(city['country_code'])
							"""
							if name in city['names']:
								country_code = city['country_code']
								candidates.append((country_code, countries[country_code], city['population']))

						print('    %s' % name)
						candidates.sort(key=itemgetter(2, 0, 1), reverse=True)
						for x in candidates:
							print('        %s, %s, %s' % (x[0], x[1], x[2]))

if __name__=='__main__':
	main()
