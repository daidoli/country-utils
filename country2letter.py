import json, sys, pdb


def main():
	countries = {}
	with open('countryInfo.txt') as f:
		while True:
			line = f.readline()
			if not line:
				break
			if line[0] == '#':
				continue

			tokens = line.split('\t')
			countries[tokens[0]] = tokens[4].lower()

	key_order = []
	result_dict = {}
	if sys.argv[1] == '-f':
		result = ''
		with open('./%s' % sys.argv[2]) as file:
			lines = file.readlines()

		key = ''
		for line in lines:
			line = line.strip()
			if line:
				if ':' in line:
					key = line[:-1].upper().replace(' ', '_')
					result_dict[key] = []
					key_order.append(key)
					#result += ')\nDEF_%s = (' % line if result else 'DEF_%s = (' % line
				else:
					for name in line.split(','):
						name = name.strip().lower().replace('st.', 'saint')
						for country_code, country_name in countries.items():
							if name in country_name:
								name = country_code
								break
						result_dict[key].append(name)

		for x in key_order:
			text = tuple(result_dict[x])
			print('%s: %s,' % (x, text))

if __name__=='__main__':
	main()
