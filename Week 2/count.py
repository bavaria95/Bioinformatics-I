def hamdist(str1, str2):
	return len(list(filter(lambda x : x[0] != x[1], zip(str1, str2))))

def approx_pattern_count(genome, pattern, d):
	count = 0
	for i in range(len(genome) - len(pattern) + 1):
		if hamdist(genome[i : i + len(pattern)], pattern) <= d:
			count += 1

	return count

pattern = input()
genome = input()
d = int(input())

print(approx_pattern_count(genome, pattern, d))