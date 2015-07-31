def reverse_complement(pattern):
	comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

	return ''.join([comp[x] for x in pattern])[::-1]

pattern = input()
print(reverse_complement(pattern))
