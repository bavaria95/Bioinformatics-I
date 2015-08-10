import sys
from itertools import product

def median_string(dna, k):
	distance = float('Inf')
	all_kmers = [''.join(kmer) for kmer in product('ACGT', repeat=k)]
	median = ''

	for pattern in all_kmers:
		if distance > d(pattern, dna):
			distance = d(pattern, dna)
			median = pattern

	return median

def hamdist(str1, str2):
	return len(list(filter(lambda x : x[0] != x[1], zip(str1, str2))))

def d_on_the_text(pattern, text):
	minim_dist = float('Inf')
	for i in range(len(text) - len(pattern) + 1):
		pattern_prim = text[i : i+len(pattern)]

		dist = hamdist(pattern, pattern_prim)
		if dist < minim_dist:
			minim_dist = dist

	return minim_dist

def d(pattern, dna):
	return sum([d_on_the_text(pattern, text) for text in dna])


k = int(input())
dna = []

for line in sys.stdin:
    dna.append(line.strip())

print(median_string(dna, k))
