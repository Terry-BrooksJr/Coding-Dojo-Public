def strange_sum(numbers):
	total = 0 # Accumulator Variable
	for i in numbers:
		if i % 3 != 0:
			total = total
		#	add_total = total +i
		#$	total = add_total
		else:
			total += i
			continue
		#print(total)
		return total


print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
