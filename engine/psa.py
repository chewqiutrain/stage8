from pycota import logger

LOG_ = logger.getLogger() 


def cleanPSA(psa): 
	'''
		:param psa: String representing PSA value
		:returns: a cleaned and validated value for PSA 
	'''
	try: 
		res0 = float(psa.strip())
		assert(res0 > 0.0), "Casted PSA value must be greater than 0"
		return res0
	except Exception as e:
		LOG_.error(f"Failed to convert PSA value to float, {e}", stack_info = True, exc_info = True)


def test():
	psaTest0 = '10'
	LOG_.info(f"original input: {psaTest0}")
	res0 = cleanPSA(psaTest0)
	LOG_.info(f"psaTest0 = {res0}")

	psaTest1 = '-1'
	LOG_.info(f"original input: {psaTest1}")
	res1 = cleanPSA(psaTest1)
	LOG_.info(res1)

if __name__ == '__main__': 
	test()

