def probability(pattern, p):
	prob = 1
	for i in range(len(pattern)):
		prob *= p[pattern[i]][i]

	return prob


text = input()
k = int(input())

p = {}
p['A'] = list(map(float, input().split()))
p['C'] = list(map(float, input().split()))
p['G'] = list(map(float, input().split()))
p['T'] = list(map(float, input().split()))
