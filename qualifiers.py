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

	books_scores = list(map(int, line.split()))

	library = {}

	i = 0

	for line in f:
		library[i] = {}
		inputs = line.split()
		library[i]['num_books'] = inputs[0]
		library[i]['signup'] = inputs[1]
		library[i]['ship'] = inputs[2]
		line = f.readline()
		library[i]['books'] = list(map(int, line.split()))
		i += 1

	f.close()

	return(no_books, no_libs, no_days, books_scores, library)

def determine_high_score_lib(books_scores, library):
	
	for lib in library:
		total_score = 0
		for books in library[lib]['books']:
			total_score += books_scores[books]
		print(total_score)

def main():

	(no_books, no_libs, no_days, books_scores, library) = read_input()
	print(no_books)
	print(no_libs)
	print(no_days)
	print(books_scores)
	print(library)
	determine_high_score_lib(books_scores, library)


if __name__ == "__main__":
	main()