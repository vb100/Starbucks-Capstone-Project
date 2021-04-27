'''
This file is supplementary to Udacity Capstone Project: Starbuck Case
Prepared by Vytautas Bielinskas (2020)
'''

# Import modules and packages
import pandas as pd

# Get main information about the given dataset
def dataset_info(df, df_name):
	'''
	Args:
		df - a given dataset : <Pandas DataFrame>
	'''
	SEPARATOR = '- ' * 30
	print(f'{df_name} data shape = {df.shape}')
	print(f'Data Types:\n{df.dtypes}\n{SEPARATOR}')
	print(f'Dataframe Information:\n {df.describe()}\n{SEPARATOR}')
	print(f'Main Information:\n{df.info()}\n')

	return None