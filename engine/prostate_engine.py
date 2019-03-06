from pycota import logger
from tumor import cleanT
from node import cleanN 
from metastasis import cleanM
from psa import cleanPSA
from grade_group import cleanGradeGroup

def cleanAll(t, n, m, psa, gg):
	tCleaned = cleanT(t)
	nCleaned = cleanN(n)
	mCleaned = cleanM(m)
	psaCleaned = cleanPSA(psa)
	ggCleaned = cleanGradeGroup(gg)
	return (tCleaned, nCleaned, mCleaned, psaCleaned, ggCleaned)


def loadAJCC():
	'''
	:returns: pandas dataframe representing ajcc data
	'''
	pass

def getSuggestedStage(ajcc_df, input_vals):
	'''
	:param ajcc_df: AJCC source of truth / calc table
	:param input_vals: tuple representing t,n,m,psa,gg
	:returns: string representing calculated stage if found, None otherwise
	'''
	return None 

def prostate_engine(t, n, m, psa, gg):
	'''
	:param t: string representing t value
	:param n: string representing n value
	:param m: string representing m value
	:param psa: string representing psa value
	:param gg: string representing gg value
	'''
	tCleaned, nCleaned, mCleaned, psaCleaned, ggCleaned = cleanAll(t, n, m, psa, gg)
	
	# Load lookup table (AJCC table)

	# Find relevant value in lookup table

	# return relevant value if found, else return None

	return 'blah'

