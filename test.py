def test(dict1):
	dict1['a'] = 3

if __name__ == '__main__':
	list1 = []
	list1.append(1)
	list1.append(2)
	dict1 = {}
	dict1['a'] = 1
	dict1['b'] = 2
	test(dict1)
	print(dict1)