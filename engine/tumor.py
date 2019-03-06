def cleanT(t): 
	'''
		:param t: String representing t value
		:returns: a cleaned and validated string representing T 
	'''
	try: 
		res0 = str(t.strip().lower())
		return res0
	except Exception as e:
		return None

def test():
	tTest0 = ' t0 '
	print(f"original input: {tTest0}")
	res0 = cleanT(tTest0)
	print(f"tTest0 = {res0}")

if __name__ == '__main__': 
	test()