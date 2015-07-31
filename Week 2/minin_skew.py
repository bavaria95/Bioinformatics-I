import numpy as np
import matplotlib.pyplot as plt

def skew(genome):
	d = 0

	s = []

	for k in range(len(genome)):
		if genome[k] == 'G':
			d += 1
		if genome[k] == 'C':
			d -= 1

		s.append(d)

	return s


# genome = raw_input()
genome = 'GATACACTTCCCGAGTAGGTACTG'
d = skew(genome)
i = list(range(1, len(genome) + 1))

m_index = 0
m_value = d[0]

for k in range(len(d)):
	if d[k] < m_value:
		m_index = k
		m_value = d[k]


# print(m_value, m_index)

f = []
for j in range(len(d)):
	if d[j] == m_value:
		f.append(j + 1)

for j in f:
	print(j),



plt.plot(i, d)
plt.show()