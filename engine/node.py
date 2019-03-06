def cleanN(n): 
	'''
		:param n: String representing N value
		:returns: a cleaned and validated string representing N
	'''
	try: 
		res0 = str(n.strip().lower())
		return res0
	except Exception as e:
		return None

def test():
	nTest0 = ' n0 '
	print(f"original input: {nTest0}")
	res0 = cleanN(nTest0)
	print(f"nTest0 = {res0}")

if __name__ == '__main__': 
	test()

