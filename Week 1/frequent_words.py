def pattern_count(text, pattern):
	count = 0
	for i in range(len(text) - len(pattern) + 1):
		if text[i : i + len(pattern)] == pattern:
			count += 1

	return count

def frequent_words(text, k):
	frequent_patterns = set()
	count = []
	for i in range(len(text) - k + 1):
		pattern = text[i : i + k]
		count.append(pattern_count(text, pattern))
	max_count = max(count)
	for i in range(len(text) - k + 1):
		if count[i] == max_count:
			frequent_patterns.add(text[i : i + k])

	return frequent_patterns

text = input()
k = int(input())

for w in frequent_words(text, k):
	print(w, end=" ")

print()