import sys

def state():
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
	if len(sys.argv) == 2:
		if sys.argv[1] in cc1:
			print(s2[s1.index(cc2[cc1.index(sys.argv[1])])])
		else:
			print('Unknown state')

if __name__ == '__main__':
	state()
