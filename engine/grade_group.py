def cleanGradeGroup(gg): 
	'''
		:param gg: String representing gg value
		:returns: a cleaned and validated string representing Grade Group
	'''
	try: 
		res0 = int(gg.strip())
		assert((res0 >= 1) & (res0 <= 5)), "Casted GG value must be between 1 and 5 inclusive"
		return res0
	except Exception as e:
		raise e

def test():
	ggTest0 = ' 7 '
	print(f"original input: {ggTest0}")
	res0 = cleanGradeGroup(ggTest0)
	print(f"ggTest0 = {res0}")

if __name__ == '__main__': 
	test()


