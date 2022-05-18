def html_table():
	head = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Document</title>\n<style>\ntable, tr, td {border: 2px solid rgb(128, 0, 255); border-collapse: collapse;font-size: smaller;}\n div, h4 {text-align: center;} table {width: min-content;height: min-content;}</style>\n</head>\n<body>\n<table>\n'
	f = open('periodic_table.txt', 'r')
	base = f.read().strip().split('\n')
	f.close()
	f = open('periodic_table.html', 'w')
	f.write(head)
	f.write('\n<tr>')
	num = 0
	for element in base:
		val = element.split(',')
		number = 0
		for i in val[4].split(':')[1].split():
			number += int(i)
		while num != int(val[0].split(':')[1]):
			f.write('<td></td>')
			num += 1
		f.write('<td>\n')
		f.write('<h4>' + val[0].split(' ')[0].strip() + '</h4>\n')
		f.write('<ul>\n<li>' + val[2].split(':')[1].strip() + '</li>\n')
		f.write('<li>' + val[3].split(':')[1] + '</li>\n')
		f.write('<li>' + val[4].split(':')[1] + '</li></ul>\n')
		f.write('<div> №' + str(number) + '</div>\n')
		f.write('</td>')
		num += 1
		if int(val[0].split(':')[1]) >= 17:
			f.write('\n</tr>')
			num = 0
			if element != base[-1]:
				f.write('<tr>')

	f.write('\n</table>\n</body>\n</html>')
	f.close()

if __name__ == '__main__':
	html_table()

#Hydrogen = position:0, number:1, small: H, molar:1.00794, electron:1