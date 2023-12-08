counter = 0

def analyzeLine(line):
	first = ''
	last =  ''
	
	# check if whole line is a string first (easiest case)
	if (line.isdigit()):
		first = line[0]
		last = line[-1]
		return (int(first+last))	

	# well, let's do it the hard way, with a horrible complexity
	for char in line:
		if (not(first) and char.isdigit()):
			first = char
		if (char.isdigit()):
			last = char

	return int(first+last) if first+last else 0

with open('input.txt') as file:
	for line in file:
		counter += analyzeLine(line)	


print(counter)
