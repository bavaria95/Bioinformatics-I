import itertools

def neighbors(pattern, d):
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


pattern = input()
d = int(input()) + 1

neighbors_words = neighbors(pattern, d)
for i in neighbors_words:
	print(i)