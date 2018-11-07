def And(t1,t2,t3):
	# a =list_t1
	# b =list_t2
	# c =list_t3
	a=t1
	b=t2
	c=t3

	def compare(a,b):
		temp_list = []
		for i in a:
			for j in b:
				if i < j:
					continue
				elif i == j:
					temp_list.append(i)
		return temp_list

	if len(a) <= len(b):
		a_b_list = compare(a,b)

	elif len(a) > len(b):
		a_b_list = compare(b,a)

	if len(a_b_list) <= len(c):
		final_list = compare(a_b_list,c)
	else:
		final_list = compare(c, a_b_list)

	return final_list
a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 6, 7, 8]
c = [1, 2, 4, 5]

print(And(a,b,c))
