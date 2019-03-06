def cleanM(m): 
	'''
		:param m: String representing M value
		:returns res: Cleaned and validated String representing M
	'''
	try: 
		res0 = str(m.strip().lower())
		return res0
	except Exception as e:
		return None

def test():
	mTest0 = ' m1 '
	print(f"original input: {mTest0}")
	res0 = cleanM(mTest0)
	print(f"mTest0 = {res0}")

if __name__ == '__main__': 
	test()

