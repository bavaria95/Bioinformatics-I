def hamdist(str1, str2):
	return len(list(filter(lambda x : x[0] != x[1], zip(str1, str2))))

