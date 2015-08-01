def frequent_words(genome, k):
	d = {}

	for i in range(len(genome) - k + 1):
		pattern = genome[i : i + k]
		d[pattern] = d.get(pattern, 0) + 1

	max_times = max(d.values())

	a = []
	for x in d:
		if d[x] == max_times:
			a.append(x)
	
	return d

genome = input()
k, d = list(map(int, input().split()))

print(frequent_words(genome, k))