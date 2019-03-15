import json, sys, pdb
from operator import itemgetter

states = {
	'Alabama': ('AL', 'US'),
	'Alaska': ('AK', 'US'),
	'Arizona': ('AZ', 'US'),
	'Arkansas': ('AR', 'US'),
	'California': ('CA', 'US'),
	'Colorado': ('CO', 'US'),
	'Connecticut': ('CT', 'US'),
	'Delaware': ('DE', 'US'),
	'Florida': ('FL', 'US'),
	'Georgia': ('GA', 'US'),
	'Hawaii': ('HI', 'US'),
	'Idaho': ('ID', 'US'),
	'Illinois': ('IL', 'US'),
	'Indiana': ('IN', 'US'),
	'Iowa': ('IA', 'US'),
	'Kansas': ('KS', 'US'),
	'Kentucky': ('KY', 'US'),
	'Louisiana': ('LA', 'US'),
	'Maine': ('ME', 'US'),
	'Maryland': ('MD', 'US'),
	'Massachusetts': ('MA', 'US'),
	'Michigan': ('MI', 'US'),
	'Minnesota': ('MN', 'US'),
	'Mississippi': ('MS', 'US'),
	'Missouri': ('MO', 'US'),
	'Montana': ('MT', 'US'),
	'Nebraska': ('NE', 'US'),
	'Nevada': ('NV', 'US'),
	'New Hampshire': ('NH', 'US'),
	'New Jersey': ('NJ', 'US'),
	'New Mexico': ('NM', 'US'),
	'New York': ('NY', 'US'),
	'North Carolina': ('NC', 'US'),
	'North Dakota': ('ND', 'US'),
	'Ohio': ('OH', 'US'),
	'Oklahoma': ('OK', 'US'),
	'Oregon': ('OR', 'US'),
	'Pennsylvania': ('PA', 'US'),
	'Rhode Island': ('RI', 'US'),
	'South Carolina': ('SC', 'US'),
	'South Dakota': ('SD', 'US'),
	'Tennessee': ('TN', 'US'),
	'Texas': ('TX', 'US'),
	'Utah': ('UT', 'US'),
	'Vermont': ('VT', 'US'),
	'Virginia': ('VA', 'US'),
	'Washington': ('WA', 'US'),
	'West Virginia': ('WV', 'US'),
	'Wisconsin': ('WI', 'US'),
	'Wyoming': ('WY', 'US'),
	'American Samoa': ('AS', 'US'),
	'District of Columbia': ('DC', 'US'),
	'Washington D.C.': ('DC', 'US'),
	'Federated States of Micronesia': ('FM', 'US'),
	'Guam': ('GU', 'US'),
	'Northern Mariana Islands': ('MP', 'US'),
	'Palau': ('PW', 'US'),
	'Puerto Rico': ('PR', 'US'),
	'Virgin Islands': ('VI', 'US'),
	'Armed Forces Africa': ('AE', 'US'),
	'Armed Forces Americas': ('AA', 'US'),
	'Armed Forces Canada': ('AE', 'US'),
	'Armed Forces Europe': ('AE', 'US'),
	'Armed Forces Middle East': ('AE', 'US'),
	'Armed Forces Pacific': ('AP', 'US'),
	'Alberta': ('AB', 'CA'),
	'British Columbia': ('BC', 'CA'),
	'Manitoba': ('MB', 'CA'),
	'New Brunswick': ('NB', 'CA'),
	'Newfoundland and Labrador': ('NL', 'CA'),
	'Newfoundland': ('NL', 'CA'),
	'Nova Scotia': ('NS', 'CA'),
	'Northwest Territories': ('NT', 'CA'),
	'Nunavut': ('NU', 'CA'),
	'Ontario': ('ON', 'CA'),
	'Prince Edward Island': ('PE', 'CA'),
	'Quebec': ('QC', 'CA'),
	'Saskatchewan': ('SK', 'CA'),
	'Yukon': ('YT', 'CA'),
	'PEI': ('PE', 'CA'),
}

def main():
	if sys.argv[1] == '-f':
		result = []

		with open('./%s' % sys.argv[2]) as file:
			lines = file.readlines()

		key = ''
		for line in lines:
			line = line.strip()
			if line:
				if ':' in line:
					key = line[:-1].upper().replace(' ', '_')
					result.append([key, []])
				else:
					for name in line.split(','):
						name2 = name.strip().lower().replace(' ', '').replace('.', '')
						for k, v in states.items():
							if name2 == k.strip().lower().replace(' ', '').replace('.', ''):
								name = '%s, %s' % (v[0], v[1])
								break
						result[-1][1].append(name)
		j = json.dumps(result).replace('[', '(').replace(']', ')').replace('"', "'").replace('), ', '),\n')
		j = j.replace('{', '').replace('}', '')
		print(j)

if __name__=='__main__':
	main()
