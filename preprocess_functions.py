import numpy as np 
import zipfile 
import pandas as pd

#change this filepath depending on your local setup
FILEPATH = 'data/gtd.zip'

#Names of columns that we don't use. Change as desired. 
unused_cols = ['approxdate', 'resolution', 'eventid', 'extended', 'resolution', 
				'vicinity', 'location', 'summary', 'crit1', 'crit2', 'crit3', 'doubtterr', 
				'alternative', 'alternative_txt', 'multiple', 'suicide', 'attacktype2', 
				'attacktype2_txt', 'attacktype3', 'attacktype3_txt', 'corp1', 'target1', 
				'targtype2', 'targtype2_txt', 'targsubtype2', 'targsubtype2_txt', 'corp2', 
				'target2', 'natlty2', 'natlty2_txt', 'targtype3', 'targtype3_txt', 'targsubtype3', 
				'targsubtype3_txt', 'corp3', 'target3', 'natlty3', 'natlty3_txt', 'gsubname', 
				'gname2', 'gsubname2', 'gname3', 'gsubname3', 'guncertain1', 'guncertain2', 
				'guncertain3', 'guncertain3', 'individual', 'nperps', 'nperpcap', 'claimed', 
				'claimmode', 'claimmode_txt', 'claim2', 'claimmode2', 'claimmode2_txt', 'claim3', 
				'claimmode3', 'claimmode3_txt', 'compclaim', 'weaptype2', 'weaptype2_txt', 'weapsubtype2', 
				'weapsubtype2_txt', 'weaptype3', 'weaptype3_txt', 'weapsubtype3', 'weapsubtype3_txt', 
				'weaptype4', 'weaptype4_txt', 'weapsubtype4', 'weapsubtype4_txt', 'weapdetail', 'ishostkid', 
				'nhostkid', 'nhostkidus', 'nhours', 'ndays', 'divert', 'kidhijcountry', 'ransomamtus', 
				'ransompaid', 'ransompaidus', 'ransomnote', 'hostkidoutcome', 'hostkidoutcome_txt', 
				'nreleased', 'addnotes', 'scite1', 'scite2', 'scite3', 'dbsource', 'INT_LOG', 
				'INT_IDEO', 'INT_MISC', 'INT_ANY', 'related']

#format for dummy variables 
# raw.join(pd.get_dummies(raw.targtype1_txt, prefix='target'))

def load_raw_data(): 
	'''
	Output: A Pandas dataframe which contains all data points. 
	This is raw data, without cleaning or removal of unused columns.
	'''
	raw = pd.read_csv(FILEPATH, header=0, encoding='ISO-8859-1')
	return raw 

def load_cleaned_data(): 
	raw = load_raw_data()
	return raw.drop(unused_cols, axis=1)
	
	