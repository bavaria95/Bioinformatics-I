def hamdist(str1, str2):
	return len(filter(lambda x : x[0] != x[1], zip(str1, str2)))

str1 = raw_input()
str2 = raw_input()

print(hamdist(str1, str2))