import sys

def get_right(s):
	res = ''
	f = s.split(' ')
	for i in f:
		res = res + ' ' + i.lower().capitalize()
	return res

def allin():
	states = {
			"Oregon" : "OR",
			"Alabama" : "AL",
			"New Jersey": "NJ",
			"Colorado" : "CO"
			}
	capital_cities = {
			"OR": "Salem",
			"AL": "Montgomery",
			"NJ": "Trenton",
			"CO": "Denver"
			}
	s1 = list(states.values())
	s2 = list(states.keys())
	cc1 = list(capital_cities.values())
	cc2 = list(capital_cities.keys())
	is_capital = 'is the capital of'
	no_found = 'is neither a capital city nor a state'

	if len(sys.argv) == 2:
		args = sys.argv[1].split(',')
		for i in args:
			temp = i.strip()
			i = get_right(i).strip()
			if i in cc1:
				print(i, is_capital, s2[s1.index(cc2[cc1.index(i)])])
			elif i in states:
				print(capital_cities[states[i]], is_capital, i)
			elif i == '':
				pass
			else:
				print(temp,no_found)
				
			

	

if __name__ == '__main__':
	allin()
