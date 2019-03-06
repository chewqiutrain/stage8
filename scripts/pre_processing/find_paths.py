'''
Follow this template when needing to find paths to files
'''
import os 
_THIS_DIR_ = os.path.dirname(os.path.realpath(__file__)) # stage8/scripts/pre_processing
_PARENT_OF_THIS_DIR_ = os.path.dirname(_THIS_DIR_) # stage8/scripts/
_PARENT_OF_PARENT_DIR_ = os.path.dirname(_PARENT_OF_THIS_DIR_) # stage8/
_DATA_DIR_ = os.path.join(_PARENT_OF_PARENT_DIR_, 'data') # stage8/data/
_TARGET_FILE_ = os.path.join(_DATA_DIR_, 'converted', 'prostate_clinical.csv')

print(_THIS_DIR_)
print(_PARENT_OF_THIS_DIR_)
print(_PARENT_OF_PARENT_DIR_)
print(_DATA_DIR_)
print(_TARGET_FILE_)

print('\n')
print(f'reading first line from file: `{_TARGET_FILE_}` \n')
with open(_TARGET_FILE_, 'r') as fd:
	x = fd.readline()
	print(x)
