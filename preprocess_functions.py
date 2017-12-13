import pandas as pd

'''Change these filepaths depending on your local setup.

WARNING: If you change the names of the csv files, you will fail the 
correct_filenames() tests in test.py.'''

FILEPATH_1 = 'data/globalterrorismdb_0617dist_1.csv'
FILEPATH_2 = 'data/globalterrorismdb_0617dist_2.csv'

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

def load_raw_data(): 
    '''
    Output: A Pandas dataframe which contains all data points. 
    This is raw data, without cleaning or removal of unused columns.
    '''
    raw_1 = pd.read_csv(FILEPATH_1, header=0, encoding='ISO-8859-1')
    raw_2 = pd.read_csv(FILEPATH_2, header=0, encoding='ISO-8859-1')
    raw_1.dropna(0, how='all', inplace=True)
    raw_2.dropna(0, how='all', inplace=True)
    return pd.concat((raw_1, raw_2), axis=0, ignore_index=True)

def load_data_relevant_cols(): 
    '''
    Output: A pandas dataframe which contains all data points, 
    but only the columns we actually use.
    '''
    raw = load_raw_data()
    return raw.drop(unused_cols, axis=1)

def get_dummies(df, columns):
    '''
    Output: A Pandas dataframe which contains the one-hot-encoded versions 
    of the categorical columns specified in 'columns', on the data frame df
    '''
    output = pd.get_dummies(df[columns[0]], prefix=columns[0])
    for column in columns[1:]:
        output = output.join(pd.get_dummies(df[column], prefix=column))
    return output

def get_filepaths(): 
    '''
    Returns filepaths to the data CSV files. Used in tests.py. 
    '''
    return FILEPATH_1, FILEPATH_2
