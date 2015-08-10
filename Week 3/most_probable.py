def probability(pattern, p):
	prob = 1
	for i in range(len(pattern)):
		prob *= p[pattern[i]][i]

	return prob

def most_probable(text, k, p):
	max_prob = 0
	most_probable_kmer = None

	for i in range(len(text) - k + 1):
		pattern = text[i : i + k]
		prob = probability(pattern, p)
		if max_prob < prob:
			max_prob = prob
			most_probable_kmer = pattern

	return most_probable_kmer

text = input()
k = int(input())

p = {}
p['A'] = list(map(float, input().split()))
p['C'] = list(map(float, input().split()))
p['G'] = list(map(float, input().split()))
p['T'] = list(map(float, input().split()))

print(most_probable(text, k, p))
