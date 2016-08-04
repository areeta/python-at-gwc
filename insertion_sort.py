def insertion_sort(list):
	for index in range(1, len(list)):
		value = list[index]
		i = index - 1
		while i >= 0: # comparing what value is left of it 
		            # if less = box left shifts to right and value shift to right'
		            # compare value to one lower to it, i = i-1, then perform loop
			if value < list[i]:
				list[i + 1] = list[i] #shift number in slot i right to slot i + 1
				list[i] = value #shift value left into slot i
				i = i -1
			else: # no need to shift
				break
a = [3, 6, 2, 9, 3, 5, 1, 2, 5, 6, 8, 3, 9]

insertion_sort(a)

print(a)