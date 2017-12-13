# A few simple tests

import pandas as pd
import warnings 

from preprocess_functions import get_filepaths, load_raw_data, load_data_relevant_cols, get_dummies

def correct_filenames(): 
	'''
	Tests whether the filepaths in preprocessing contain the actual filenames. 
	Assumes the names of the CSV files have not been changed.
	Should work even if you re-structure directories, as long as you update 
	the preprocess_functions.py file according. 


	'''
	path1, path2 = get_filepaths()
	csv_name_1 = 'globalterrorismdb_0617dist_1.csv'
	csv_name_2 = 'globalterrorismdb_0617dist_2.csv'
	assert csv_name_1 in path1, 'Filepath {} must include {}'.format(path1, csv_name_1)
	assert csv_name_2 in path2, 'Filepath {} must include {}'.format(path2, csv_name_2)

def raw_data_loads(): 
	'''
	Tests the load_raw_data() function in preprocess_functions.py
	Tests for 2 conditions: 
	1. The type of the raw data is a Dataframe. This is essential for the notebooks. 
	2. The data has the correct shape. Otherwise, somehow data went missing, likely due to 
	an error in getting the CSV files. 
	'''
	raw = load_raw_data()

	type_error_msg = '{} should be a Pandas dataframe but is type {}'.format(raw, type(raw))
	assert type(raw) == pd.core.frame.DataFrame, type_error_msg

	shape_error_msg = '{} has shape {} but should be (170350, 135)'.format(raw, raw.shape)
	assert raw.shape == (170350, 135), shape_error_msg


def data_loads_relevant_cols():
	'''
	Tests the load_data_relevant_cols() function in preprocess_functions.py

	Tests for 2 conditions: 
	1. The type of the data is a Dataframe. This is essential for the notebooks. 
	2. The data has all of the original attack incidents. 

	Note that we do not test for which columns were kept, as someone else might choose to 
	include columns we did not, or discard columns we used. 	
	'''
	limited_data = load_data_relevant_cols()

	type_error_msg = '{} should be a Pandas dataframe but is type {}'.format(limited_data, type(limited_data))
	assert type(limited_data) == pd.core.frame.DataFrame, type_error_msg

	assert limited_data.shape[0] == 170350, '{} should have 170350 rows but has {}'.format(limited_data.shape[0])

def dummies_test(): 
	'''
	Tests the get_dummies() function in function in preprocess_functions.py

	Tests for 3 conditions: 
	1. Dummies is a dataframe. This is essential for code in the notebooks
	2. The shape of a test one-hot dataframe is correct. 
	3. The one-hot array only contains the values 0, 1

	Assumes the raw data still contains all of the original values from the CSV file.
	'''
	dummies = get_dummies(load_raw_data(), ['country_txt'])

	type_error_msg = '{} should be a Pandas dataframe but is type {}'.format(dummies, type(dummies))
	assert type(dummies) == pd.core.frame.DataFrame, type_error_msg

	shape_error_msg = 'The dummy dataframe {} should have shape '.format(dummies)
	shape_error_msg += '(170350, 205), but has shape {}'.format(dummies, dummies.shape)

	assert dummies.shape == (170350, 205), shape_error_msg

	#mask array testing whether values of dummy are either 0, 1
	zero_one_mask = dummies.isin([0, 1])
	assert not(False in zero_one_mask.values), 'One-hot dataframe {} contains values outside [0, 1]'.format(dummies)


if __name__ == '__main__': 
	#Suppresses the DtypeWarning from Pandas when we use a CSV with mixed data types. 
	#It's safe to remove this line if you want. We included it to make output less confusing.
	warnings.filterwarnings("ignore")

	print('Running unit tests...')
	try: 
		correct_filenames()
		raw_data_loads()
		data_loads_relevant_cols()
		dummies_test()
		print('All tests passed!')
	except AssertionError as e: 
		print(e)
