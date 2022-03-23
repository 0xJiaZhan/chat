
def read_file(filename):
	lines = []
	with open(filename, "r", encoding="utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert():
	

def main():
	lines = read_file("input.txt")
	print(lines)

main()