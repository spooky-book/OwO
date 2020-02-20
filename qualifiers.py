import sys
import operator
import math

def read_input():
	input_file = str(sys.argv[1])

	f = open(input_file, "r")

	line = f.readline()

	inputs = line.split()
	no_books = int(inputs[0])
	no_libs = int(inputs[1])
	no_days = int(inputs[2])

	line = f.readline()

	books_scores = list(map(int, line.split()))

	library = {}

	i = 0

	for line in f:
		print(i)
		print(line)
		library[i] = {}
		inputs = line.split()
		library[i]['num_books'] = int(inputs[0])
		library[i]['signup'] = int(inputs[1])
		library[i]['ship'] = int(inputs[2])
		line = f.readline()
		library[i]['books'] = list(map(int, line.split()))
		library[i]['shipped'] = []
		i += 1

	f.close()

	return(no_books, no_libs, no_days, books_scores, library)

def determine_high_score_lib(no_days, books_scores, library, signedup_libs):
	
	scores = {}

	for lib in library:
		total_score = 0
		if lib not in signedup_libs:
			for books in library[lib]['books']:
				total_score += books_scores[books]
			scores[lib] = total_score
	max_score_key = max(scores.items(), key=operator.itemgetter(1))[0]
	#print(max_score_key)
	return(max_score_key, max(scores.values()))

def output(signedup_libs, library):
	output = ''
	output += str(len(signedup_libs)) + '\n'
	for lib in signedup_libs:
		output += str(lib) + ' ' + str(len(library[lib]['shipped'])) + '\n'
		output += ' '.join(list(map(str, library[lib]['shipped']))) + '\n'
	
	output_file = str(sys.argv[1])[:-3] + 'out' 
	file = open(output_file, 'w')
	file.write(output)
	file.close()


def main():

	(no_books, no_libs, no_days, books_scores, library) = read_input()

	signedup_libs = []
	scanned_books = []

	signup = False
	signup_period = 0

	day_counter = 0

	while day_counter <= no_days:
		#print("it is currently day no." + str(day_counter))

		if signup == False and len(signedup_libs) < no_libs:
			(highest_score_lib, highest_score) = determine_high_score_lib(no_days, books_scores, library, signedup_libs)
			#print("signing up lib no." + str(highest_score_lib))
			signup = True
			signup_period += 1

		elif signup_period < library[highest_score_lib]['signup']:
			signup_period += 1

		elif signup_period == library[highest_score_lib]['signup']:
			signedup_libs.append(highest_score_lib)
			signup_period = 0
			#print("finished signing up lib no." + str(highest_score_lib))
			signup = False


		for lib in signedup_libs:
			to_ship = 0
			i = 0

			while to_ship < library[lib]['ship']:
				
				#print(scanned_books)
				##print(library[lib]['books'][i])
				#print(to_ship)
				if i >= library[lib]['num_books']:
					break

				elif library[lib]['books'][i] not in scanned_books:
					print("Scanning: " + str(library[lib]['books'][i]))
					library[lib]['shipped'].append(library[lib]['books'][i])
					scanned_books.append(library[lib]['books'][i])
					#print(scanned_books)
					to_ship += 1

				i += 1	


		day_counter += 1

	
	output(signedup_libs, library)



if __name__ == "__main__":
	main()