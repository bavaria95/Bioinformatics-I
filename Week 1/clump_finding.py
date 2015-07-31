def frequent_words(text, k, t):
	d = {}

	for i in range(len(text) - k + 1):
		pattern = text[i : i + k]
		d[pattern] = d.get(pattern, 0) + 1

	a = set()
	for x in d:
		if d[x] >= t:
			a.add(x)
	
	return a

def clump_finding(genome, k, L, t):
	clumps = set()

	for i in range(len(genome) - L + 1):
		if i % 10000 == 0:
			print(i)
			
		text = genome[i : i + L]
		clumps |= frequent_words(text, k, t)

	return clumps


genome = input()
k, L, t = map(int, input().split())

print(' '.join(list(clump_finding(genome, k, L, t))))

