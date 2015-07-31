def skew(genome):
	d = 0

	s = [0]

	for k in range(len(genome)):
		if genome[k] == 'G':
			d += 1
		if genome[k] == 'C':
			d -= 1

		s.append(d)

	return s

print(skew('CATGGGCATCGGCCATACGCC'))
