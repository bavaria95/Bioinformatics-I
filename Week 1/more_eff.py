def frequent_words(text, k):
	d = {}

	for i in range(len(text) - k + 1):
		pattern = text[i : i + k]
		d[pattern] = d.get(pattern, 0) + 1

	max_times = max(d.values())

	a = []
	for x in d:
		if d[x] == max_times:
			a.append(x)
	
	return a

text = input()
k = int(input())

print(frequent_words(text, k))