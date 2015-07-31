def approx_pattern_matching(pattern, genome, d):
	k = len(pattern)
	matches = []

	for i in range(len(genome) - k + 1):
		if hamdist(genome[i : i + k], pattern) <= d :
			matches.append(i)

	return matches

def hamdist(str1, str2):
	return len(list(filter(lambda x : x[0] != x[1], zip(str1, str2))))

pattern = input()
genome = input()
d = int(input())

print(' '.join(list(map(str, approx_pattern_matching(pattern, genome, d)))))