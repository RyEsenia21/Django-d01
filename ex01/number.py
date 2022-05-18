def numbers():
	f = open('numbers.txt', 'r')
	s = f.read().strip().split(',')
	for i in s:
		print(i)


if __name__ == '__main__':
	numbers()
