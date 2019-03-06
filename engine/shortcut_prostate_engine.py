import os 
import pandas as pd 

_THIS_DIR_ = os.path.dirname(os.path.realpath(__file__)) # stage8/scripts/pre_processing
_PARENT_OF_THIS_DIR_ = os.path.dirname(_THIS_DIR_) # stage8/scripts/
_DATA_DIR_ = os.path.join(_PARENT_OF_THIS_DIR_, 'data') # stage8/data/
fn_prostate_clinical_cleaned = os.path.join(_DATA_DIR_, 'clean', 'prostate_clinical_cleaned.csv')
fn_prostate_path_cleaned = os.path.join(_DATA_DIR_, 'clean', 'prostate_path_cleaned.csv') 



def mapInputPSA(psa):
	'''
	:param psa: String representation of psa 
	'''
	try: 
		psaVal = int(psa.strip())
		if psaVal < 10:
			return 'less than 10'
		elif (psaVal >= 10) and (psaVal < 20):
			return 'greater than or equal to 10, but less than 20'
		elif (psaVal >= 20):
			return 'greater than or equal to 20'
		else:
			return ''
	except:
		print('Failed to cast Pathological PSA')
		return ''


def validateGG(gg):
	try:
		ggVal = int(gg.strip())
		if ((ggVal >=1) and (ggVal <= 5)):
			return str(ggVal)
		else:
			return None
	except:
		print('Failed to cast GG')
		return None


def loadAJCC():
	dfProstateClin = pd.read_csv(fn_prostate_clinical_cleaned, dtype = 'str')
	dfProstatePath = pd.read_csv(fn_prostate_path_cleaned, dtype = 'str')
	# print(dfProstateClin.head())
	# print(dfProstateClin.shape)

	# print('\n')
	# print(dfProstatePath.head())
	# print(dfProstatePath.shape)

	# ----- clean ajcc tables ----- 
	#print('\nPath')
	#print(dfProstatePath['psa'].unique().tolist())
	# print('\nClinical')
	# print(dfProstateClin['psa'].unique().tolist())

	dfProstateClin['staging_type'] = 'clinical'
	dfProstatePath['staging_type'] = 'pathological'

	dfCombined = pd.concat([dfProstateClin, dfProstatePath])
	#print(dfCombined.head())
	#print(dfCombined.shape)
	return dfCombined


def prostate_engine(t,n,m,psa,gg,lookup):
	'''
	:param lookup: AJCC dataframe 
	'''
	

	# map / clean t,n,m,psa,gg.
	# used cleaned values to lookup into dfLookup

	t = str(t.strip())
	n = str(n.strip())
	m = str(m.strip())
	gg = validateGG(gg)
	psa = mapInputPSA(psa)


	# Filter to find stage
	result = lookup[(lookup.t == t)]
	if(result.shape[0] == 0):
		print("incorrect T value, please check")
		return None

	result = result[(result.n == n)]
	if(result.shape[0] == 0):
		print("incorrect N value, please check")
		return None

	result = result[(result.m == m)]
	if(result.shape[0] == 0):
		print("incorrect M value, please check")
		return None

	result = result[(result.grade_group == gg)]
	if(result.shape[0] == 0):
		print("incorrect Grade Group value, please check")
		return None

	result = result[(result.psa == psa)]
	if(result.shape[0] == 0):
		print("incorrect PSA value, please check")
		return None

	return result


def main():
	t = 'cT1'
	n = 'cN0'
	m = 'cM0'
	psa = '100'
	gg = '1'
	lookupDF = loadAJCC()
	result = prostate_engine(t,n,m,psa,gg, lookupDF)
	print(result)
	

if __name__ == '__main__':
	main()