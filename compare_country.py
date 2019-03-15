import difflib

ori = """American Samoa, Cook Islands, Federated States of Micronesia, Fiji, French Polynesia, Guam, Northern Mariana Islands, Marshall Islands, New Caledonia, Palau, Papua New Guinea, Tonga, Vanuatu, Samoa"""
exp = ('AS', 'CK', 'FM', 'FJ', 'PF', 'GU', 'MP', 'MH', 'NC', 'PW', 'PG', 'TO', 'VU', 'WS')

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

    ori_list = ori.split(', ')
    for i in range(len(ori_list)):
        code = exp[i]
        country_name_base = ori_list[i].lower()
        country_name = countries[code]
        ratio = difflib.SequenceMatcher(None, country_name_base, country_name).ratio()
        if ratio != 1.0:
        #if True:
            print('%s: %s, %s, %s(%s)' % (i, ratio, country_name_base, country_name, code))

if __name__=='__main__':
	main()
