import os 
import pandas as pd 

_THIS_DIR_ = os.path.dirname(os.path.realpath(__file__)) # stage8/scripts/pre_processing
_PARENT_OF_THIS_DIR_ = os.path.dirname(_THIS_DIR_) # stage8/scripts/
_DATA_DIR_ = os.path.join(_PARENT_OF_THIS_DIR_, 'data') # stage8/data/
fn_prostate_clinical_cleaned = os.path.join(_DATA_DIR_, 'clean', 'prostate_clinical_cleaned.csv')
fn_prostate_path_cleaned = os.path.join(_DATA_DIR_, 'clean', 'prostate_path_cleaned.csv') 

def ajccCleanMap():
	#['less than 10', 'greater than or equal to 10, but less than 20', 'greater than or equal to 20']
	clin = {
	'a':1
	}
	path = {
	'a':1
	}
	return clin, path

def mapInputClinicalPSA(psa):
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
		print('Failed to cast Clinical PSA')
		return ''


def mapInputPathPSA(psa):
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





def loadAJCC():
	dfProstateClin = pd.read_csv(fn_prostate_clinical_cleaned, dtype = 'str')
	dfProstatePath = pd.read_csv(fn_prostate_path_cleaned, dtype = 'str')
	print(dfProstateClin.head())
	print(dfProstateClin.shape)

	print('\n')
	print(dfProstatePath.head())
	print(dfProstatePath.shape)

	# ----- clean ajcc tables ----- 
	print('\nPath')
	print(dfProstatePath['psa'].unique().tolist())
	print('\nClinical')
	print(dfProstateClin['psa'].unique().tolist())

	dfProstateClin['staging_type'] = 'clinical'
	dfProstatePath['staging_type'] = 'pathological'

	dfCombined = pd.concat([dfProstateClin, dfProstatePath])
	print(dfCombined.head())
	print(dfCombined.shape)
	return dfCombined


def prostate_engine(t,n,m,psa,gg,lookup):
	'''
	:param lookup: AJCC dataframe 
	'''
	

	# map / clean t,n,m,psa,gg.
	# used cleaned values to lookup into dfLookup

	result = 'hello'# find row where t,n,m,psa,gg in lookup 
	return result


def main():
	t = 't'
	n = 'n'
	m = 'm'
	psa = '100'
	gg = '3'
	lookupDF = loadAJCC()
	result = prostate_engine(t,n,m,psa,gg, lookupDF)


if __name__ == '__main__':
	main()