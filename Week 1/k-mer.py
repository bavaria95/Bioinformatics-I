def find(text, k):
	most_freq_substr = ''
	occ_of_most_freq_substr = 0

	for i in range(len(text) - k):
		substr = text[i : i + k]
		if text.count(substr) > occ_of_most_freq_substr:
			occ_of_most_freq_substr = text.count(substr)
			most_freq_substr = substr
		print occ_of_most_freq_substr

	return most_freq_substr, occ_of_most_freq_substr

text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
print find(text, 3)

