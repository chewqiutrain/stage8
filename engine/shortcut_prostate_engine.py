import os 
import pandas as pd 

_THIS_DIR_ = os.path.dirname(os.path.realpath(__file__)) # stage8/scripts/pre_processing
_PARENT_OF_THIS_DIR_ = os.path.dirname(_THIS_DIR_) # stage8/scripts/
_DATA_DIR_ = os.path.join(_PARENT_OF_THIS_DIR_, 'data') # stage8/data/
fn_prostate_clinical_cleaned = os.path.join(_DATA_DIR_, 'clean', 'prostate_clinical_cleaned.csv')
fn_prostate_path_cleaned = os.path.join(_DATA_DIR_, 'clean', 'prostate_path_cleaned.csv') 

class ResultPayload(object):
	def __init__(self, t, n, m, psa, psaKey, gg):
		self.t = t 
		self.n = n 
		self.m = m 
		self.psa = psa 
		self.psaKey = psaKey
		self.gg = gg 
		self.calculatedStage = None 
		self.calculatedStageType = None 
		self.numResults = None

	def __repr__(self):
		return f"ResultPayload(T = {self.t}, N = {self.n}, M = {self.m}, PSA = {self.psa}, Grade Group = {self.gg} | calcStage: {self.calculatedStage} , calcStageType = {self.calculatedStageType}, numResults = {self.numResults})"

	def parseResult(self, result):
		# multiple rows from lookup
		if isinstance(result, pd.DataFrame):
			if result.shape[0] > 1:
				print('Multiple results')

			print(result)
			stages = result['stage'].tolist()
			stagingType = result['staging_type'].tolist()
			self.calculatedStage = stages
			self.calculatedStageType = stagingType
			self.numResults = len(stages)
		elif result is None:
			print(f'No result found for (T = {self.t}, N = {self.n}, M = {self.m}, PSA = {self.psa}, Grade Group = {self.gg})')
		else:
			print(f'Failed Parsing result for T: {self.t} | N: {self.n} | M: {self.m} | PSA: {self.psa} | Grade Group: {self.gg} | resultType {str(type(result))}')

	def makeStageResultString(self):
		if self.calculatedStage is None:
			return 
		return '|'.join(self.calculatedStage)
		

	def makeStageTypeResultString(self):
		if self.calculatedStageType is None:
			return 
		return '|'.join(self.calculatedStageType)

	def makeCSV(self):
		return f"{self.t},{self.n},{self.m},{self.psa},{self.gg},{self.makeStageResultString()},{self.makeStageTypeResultString()}"






def mapInputPSA(psa):
	'''
	:param psa: String representation of psa 
	'''
	try: 
		psaVal = float(psa.strip())
		if psaVal < 10:
			return (psaVal, 'less than 10')
		elif (psaVal >= 10) and (psaVal < 20):
			return (psaVal, 'greater than or equal to 10, but less than 20')
		elif (psaVal >= 20):
			return (psaVal, 'greater than or equal to 20')
		else:
			return (psaVal, '')
	except:
		print('Failed to cast Pathological PSA')
		return (psaVal, '')


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

	dfProstateClin['staging_type'] = 'clinical'
	dfProstatePath['staging_type'] = 'pathological'

	dfCombined = pd.concat([dfProstateClin, dfProstatePath])
	dfCombined.reset_index(inplace = True, drop = True)
	
	return dfCombined


def prostate_engine(t,n,m,psa,gg,lookup):
	'''
	:param lookup: AJCC dataframe 
	:returns: None if no value was found, dataframe if something was found
	'''
	

	# map / clean t,n,m,psa,gg.
	# used cleaned values to lookup into dfLookup

	t = str(t.strip())
	n = str(n.strip())
	m = str(m.strip())
	gg = validateGG(gg)
	psaVal, psaKey = mapInputPSA(psa)

	resultPayload = ResultPayload(t, n, m, psaVal, psaKey, gg)
	# Filter to find stage
	result = lookup[(lookup.t == t)]
	if(result.shape[0] == 0):
		print(f"incorrect T value, please check: {t}")
		resultPayload.parseResult(None)
		return resultPayload

	result = result[(result.n == n)]
	if(result.shape[0] == 0):
		print(f"incorrect N value, please check: {n}")
		resultPayload.parseResult(None)
		return resultPayload

	result = result[(result.m == m)]
	if(result.shape[0] == 0):
		print(f"incorrect M value, please check: {m}")
		resultPayload.parseResult(None)
		return resultPayload

	result = result[(result.grade_group == gg)]
	if(result.shape[0] == 0):
		print(f"incorrect Grade Group value, please check: {gg}")
		resultPayload.parseResult(None)
		return resultPayload

	result = result[(result.psa == psaKey)]
	if(result.shape[0] == 0):
		print(f"incorrect PSA value, please check: {psaVal} | {psaKey}")
		resultPayload.parseResult(None)
		return resultPayload

	resultPayload.parseResult(result)
	return resultPayload


def main():
	t = 'cT1'
	n = 'cN0'
	m = 'cM0'
	psa = '100'
	gg = '1'
	lookupDF = loadAJCC()
	result = prostate_engine(t,n,m,psa,gg, lookupDF)
	print(result)

	print(result.makeStageResultString())
	print(result.makeStageTypeResultString())
	

if __name__ == '__main__':
	main()