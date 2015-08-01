import itertools

def neighbors(pattern, d):
	d = d + 1
	alph = 'ACGT'   # alphabet
	a = list(range(len(pattern)))
	neighbors_words = []
	
	for i in range(d):
		possitions = list(itertools.combinations(a, i))

		for pos in possitions:
			sub_word = [pattern[x] for x in pos]

			all_combs = list(itertools.product(alph, repeat=len(sub_word)))
			filt_combs = filter(lambda z: all(map(lambda x, y: x != y, z, sub_word)), all_combs)

			for j in filt_combs:
				tmp = pattern
				for k in range(i):
					tmp = tmp[: pos[k]] + j[k] + tmp[pos[k] + 1 :]
				neighbors_words.append(tmp)

	return neighbors_words

def number_to_pattern(pos, k):
    alph = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    rem = pos
    pattern = ''
    while rem > 0:
        pos = rem % 4
        pattern = alph[pos] + pattern
        rem = rem // 4
    if len(pattern) < k:
        pattern = 'A' * (k - len(pattern)) + pattern
    return pattern

def pattern_to_number(pattern):
    alph = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    pos = 0
    for i in range(len(pattern)):
        pos = pos + 4 ** (len(pattern) - i - 1) * alph[pattern[i]]
    return pos

def hamdist(str1, str2):
	return len(list(filter(lambda x : x[0] != x[1], zip(str1, str2))))

def approx_pattern_count(genome, pattern, d):
	count = 0
	for i in range(len(genome) - len(pattern) + 1):
		if hamdist(genome[i : i + len(pattern)], pattern) <= d:
			count += 1

	return count

def reverse_complement(pattern):
	comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

	return ''.join([comp[x] for x in pattern])[::-1]

def approx_frequent_words_with_complements(genome, k, d):
	close = [0]*4**k
	frequency_array = [0]*4**k
	frequent_patterns = set()

	for i in range(len(genome) - k + 1):
		neighborhood = neighbors(genome[i : i + k], d)
		for pattern in neighborhood:
			index = pattern_to_number(pattern)
			close[index] = 1

	for i in range(4**k):
		if close[i]:
			pattern = number_to_pattern(i, k)
			frequency_array[i] = approx_pattern_count(genome, pattern, d) +\
				approx_pattern_count(genome, reverse_complement(pattern), d)
	max_count = max(frequency_array)

	for i in range(4**k):
		if frequency_array[i] == max_count:
			pattern = number_to_pattern(i, k)
			frequent_patterns.add(pattern)

	return frequent_patterns



genome = input()
k, d = map(int, input().split())

frequency_words = approx_frequent_words_with_complements(genome, k, d)

for word in frequency_words:
	print(word, end=' ')
print()
