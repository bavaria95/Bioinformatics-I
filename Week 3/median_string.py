def hamdist(str1, str2):
	return len(list(filter(lambda x : x[0] != x[1], zip(str1, str2))))

def d(pattern, text):
	minim_dist = float('Inf')
	for i in range(len(text) - len(pattern) + 1):
		pattern_prim = text[i : i+len(pattern)]

		dist = hamdist(pattern, pattern_prim)
		if dist < minim_dist:
			minim_dist = dist

	return minim_dist
