def pattern_count(text, pattern):
	count = 0
	for i in range(len(text) - len(pattern) + 1):
		# print(text[i : i + len(pattern)] +)
		if text[i : i + len(pattern)] == pattern:
			count += 1

	return count

t = input()
p = input()

print(pattern_count(t, p))