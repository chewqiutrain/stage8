import os 
import pandas as pd 
from shortcut_prostate_engine import prostate_engine
from shortcut_prostate_engine import loadAJCC
_THIS_DIR_ = os.path.dirname(os.path.realpath(__file__))
_PARENT_OF_THIS_DIR_ = os.path.dirname(_THIS_DIR_)
_TEST_DATA_DIR_ = os.path.join(_PARENT_OF_THIS_DIR_, 'data', 'test_data')

_AJCC_LOOK_UP_ = loadAJCC()

def cleanN(t,n):
	tPrefix = t[0]
	nPrefix = n[0]
	# if N has as prefix, ignore dependence on T
	if (nPrefix == 'p') or (nPrefix == 'c'): 
		return n

	if (tPrefix == 'p'):
		return 'p' + n 
	elif (tPrefix == 'c'):
		return 'c' + n 
	else:
		return n 


def cleanM(t,m):
	tPrefix = t[0]
	mPrefix = m[0]

	# if M has a prefix, ignore dependence on T
	if (mPrefix == 'p') or (mPrefix == 'c'):
		return m

	if (tPrefix == 'p'):
		return 'p' + m
	elif (tPrefix == 'c'):
		return 'c' + m
	else:
		return m

def rowWrap(row):
	t = row[0].strip()
	n = cleanN(t, row[1])
	m = cleanM(t, row[2])
	psa = row[3]
	gg = row[4]
	result = prostate_engine(t,n,m,psa,gg, _AJCC_LOOK_UP_)
	return result
	

def overRows(df):
	numRows, numCols = df.shape
	allResults = ['testId,t,n,m,psa,gg,calc_stages,calc_stages_type']
	for i in range(0, numRows):
		rowI = df.iloc[i]
		result = rowWrap(rowI)
		csvResI = result.makeCSV()
		testId = rowI[['t','n','m','psa','grade_group']].tolist()
		testId = ''.join(testId)
		allResults.append(testId + ',' + csvResI)
	return allResults



def main():
	fn = os.path.join(_TEST_DATA_DIR_, 'test_data_prostate.csv')
	df = pd.read_csv(fn, dtype = 'str')
	df.columns = ['t', 'n', 'm', 'psa', 'grade_group', 'expected_result', 'invalid_input_reason']
	# df['n'] = df['n'].apply(lambda n: 'c' + n)
	# df['m'] = df['m'].apply(lambda m: 'c' + m)

	# test = df.loc[0:3,:]
	# print(test)
	allResults = overRows(df)
	print('\n\n\n')

	with open('calculated.csv', 'w') as fd:
		for i in allResults:
			print(i)
			fd.write(i + '\n')
	# test['calc'] = test.apply(lambda row: rowWrap(row), axis = 1)
	# print(test)


	# df.to_csv('prostate_calculated_1.csv', index = False)
	

def test():
	x = _AJCC_LOOK_UP_.loc[0,:]
	print(type(x))
	print(x)
	print('\nSeries access ...? \n')
	t = x['t']
	n = x['n']
	m = x['m']
	psa = x['psa']
	gg = x['grade_group']

	# print(t)
	# print(n)
	# print(m)
	# print(psa)
	# print(gg)
	

	# z = _AJCC_LOOK_UP_.loc[(_AJCC_LOOK_UP_['t'] == t) & (_AJCC_LOOK_UP_['n'] == n) & \
	# 	(_AJCC_LOOK_UP_['m'] == m) & (_AJCC_LOOK_UP_['psa'] == psa) & (_AJCC_LOOK_UP_['grade_group'] == gg),:]

	z = _AJCC_LOOK_UP_.loc[(_AJCC_LOOK_UP_['t'] == t) & (_AJCC_LOOK_UP_['n'] == n) & \
		(_AJCC_LOOK_UP_['m'] == m) & (_AJCC_LOOK_UP_['psa'] == psa),:]
	print(z)
	print(type(z))

	numRows,numCols = z.shape
	for i in range(0, numRows):
		rowI = z.iloc[i]
		print(rowI)
		print(type(rowI))
		print(rowI.tolist())
		break

	# z0 = z[['stage','staging_type']]
	# z0a = list(map(tuple, z0.values))
	# print(z0)
	# print('\n')
	# print(z0a)

	# y = list(map(','.join, z0a))
	# print(y)

	# print(' | '.join(y))
	# print('\n\n')

	# z1 = z['stage'].tolist()
	# print(z1)






if __name__ == '__main__':
	main()