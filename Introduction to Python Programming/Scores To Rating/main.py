import random

def average(li=[]):
	avrg = 0
	for i in range(len(li)):
		avrg += li[i]

	avrg = avrg/len(li)
	return avrg

def mapScore(score):
	if(score>=0 and score<1):
		return "Terrible"

	if(score>=1 and score<2):
		return "Bad"

	if(score>=2 and score<3):
		return "OK"

	if(score>=3 and score<4):
		return "Good"

	if(score>=4 and score<=5):
		return "Excellent"

def readInput(numberOfInputs):
	li = []
	for x in range(numberOfInputs):
		inp = input()
		inp = float(inp)
		li.append(inp)

	return li

def quicksort(a, l, r):
	if l >= r:
		return a
	p = partition(a, l, r)
	quicksort(a, l, p)
	quicksort(a, p+1, r)
	return a

def partition(a, l, r):
	p = int(random.random() * (r-l))+l
	a[l], a[p] = a[p], a[l]
	pivot = a[l]
	i = l+1
	for j in range(i, r):
		if a[j] < pivot:
			a[j], a[i] = a[i], a[j]
			i += 1
	a[l], a[i-1] = a[i-1], a[l]
	return i-1

def disregardFirstAndLast(li):
	del li[-1]
	del li[0]
	return li


if __name__ == '__main__':
	li = readInput(5)
	li = quicksort(li, 0, len(li))
	li = disregardFirstAndLast(li)
	av = average(li)
	print(mapScore(av))



