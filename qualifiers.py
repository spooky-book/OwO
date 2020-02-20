import sys

def read_input():
	input_file = str(sys.argv[1])

	f = open(input_file, "r")

	line = f.readline()

	inputs = line.split()
	no_books = inputs[0]
	no_libs = inputs[1]
	no_days = inputs[2]

	line = f.readline()

	books_scores = line.split()

	library = {}

	i = 0

	for line in f:
		library[i] = {}
		inputs = line.split()
		library[i]['num_books'] = inputs[0]
		library[i]['signup'] = inputs[1]
		library[i]['ship'] = inputs[2]
		line = f.readline()
		library[i]['books'] = line.split()
		i += 1


	f.close()

	print(no_books)
	print(no_libs)
	print(no_days)
	print(books_scores)
	print(library)

def main():

	read_input()


if __name__ == "__main__":
	main()