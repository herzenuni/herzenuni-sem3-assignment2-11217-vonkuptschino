from timeit import timeit

def bubble(array):
	"""
	Сортировка пузырьком
	"""
	for i in range(len(array)):
		for j in range (i, len(array)):
			if (array[i] > array[j]):
				bub = array[i]
				array[i] = array[j]
				array [j] = bub
	return array

def qsort(lst):
	"""
	Быстрая сортировка
	"""
	if lst:
		head, *tail = lst
		return qsort([x for x in tail if x <= head]) + \
				[head] + \
				qsort([x for x in tail if x > head])
	return []

if __name__ == '__main__':
	print(bubble([5,3,7,9,2,1]))
	print(qsort([2,12,86,0,6,0]))
	print(timeit('bubble([5,3,7,9,2,1])', setup = 'from __main__ import bubble', number = 10))
	print(timeit('qsort([2,12,86,0,6])', setup = 'from __main__ import qsort', number = 10))