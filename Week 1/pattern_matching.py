def pattern_matching(pattern, genome):
	k = len(pattern)
	matches = []

	for i in range(len(genome) - k + 1):
		if genome[i : i + k] == pattern:
			matches.append(i)

	return matches

pattern = input()
genome = input()

print(' '.join(list(map(str, pattern_matching(pattern, genome)))))