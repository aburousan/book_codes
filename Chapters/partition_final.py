n = 300
odd_pos = []
even_pos= []
pos_d = []
for i in range(1,n+1):
	even_pos.append(i)
	odd_pos.append(2*i+1)

m = 0; k = 0
for i in range(n-1):
	if i % 2 == 0:
		pos_d.append(even_pos[m])
		m += 1
	else:
		pos_d.append(odd_pos[k])
		k += 1
		
initial = 1
pos_index = [initial]; count = 1
for i in pos_d:
	d = initial + i
	pos_index.append(d)
	initial = d
	count += 1
	if count > n:
		break

sign = []
for i in range(n):
	if i % 4 == 2 or i % 4 == 3:
		sign.append(-1)
	else:
		sign.append(1)
		
pos_sign = []; k = 0
for i in range(1,n+1):
	if i in pos_index:
		ps = (i,sign[k])
		k = k + 1
		pos_sign.append(ps)
	else:
		pos_sign.append(0)
if len(pos_sign) != n:
	print("Error in position and sign list.")

partition = [1]
f_pos = []
for i in range(n):
	if pos_sign[i]:
		f_pos.append(pos_sign[i])
	partition.append(sum(partition[-p]*s for p,s in f_pos))
print(partition[-1])
