from pycota import logger
from tumor import cleanT
from node import cleanN 
from metastasis import cleanM
from psa import cleanPSA
from grade_group import cleanGradeGroup

LOG_ = logger.getLogger() 

LOG_.info("Hello world!")

def cleanAll(t, n, m, psa, gg):
	tCleaned = cleanT(t)
	nCleaned = cleanN(n)
	mCleaned = cleanM(m)
	psaCleaned = cleanPSA(psa)
	ggCleaned = cleanGradeGroup(gg)
	return (tCleaned, nCleaned, mCleaned, psaCleaned, ggCleaned)


def prostate_engine(t, n, m, psa, gg):
	'''
	:param t: string representing t value
	:param n: string representing n value
	:param m: string representing m value
	:param psa: string representing psa value
	:param gg: string representing gg value
	'''
	tCleaned, nCleaned, mCleaned, psaCleaned, ggCleaned = cleanAll(t, n, m, psa, gg)

	return 'blah'

