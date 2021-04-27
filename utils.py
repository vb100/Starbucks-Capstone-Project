'''
This file is supplementary to Udacity Capstone Project: Starbuck Case
Prepared by Vytautas Bielinskas (2020)
'''

# Import modules and packages
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

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


# Calculate ECDF for a given series of values
def ecdf(values):
	'''
	Args:
		values - a given values from a dataframe : <Pandas DataFrame -> Series of Values>
	'''
	# Number of data points: n
	n = len(values)
	# x-data for the ECDF: x
	x = np.sort(values)
	# y-data for the ECDF: y
	y = np.arange(1, len(x)+1) / n

	return x, y


# Plot ECDF graph for a given dataset and series of data in such dataset
def plot_ecdf(x, y, dataset_name, feature_name):
	'''
	Args:
		x, y - list of values generated by ecdf procedure : <list>, <list>
		dataset_name - a given name of actual dataset : <string>
		feature_name - a given name of actual feature in a dataset : <string>
	'''
	plt.rcParams['figure.figsize'] = (11.25, 2.75)
	_ = plt.title(f'Checking distribution for {dataset_name}: {feature_name}', family='IBM Plex Arabic', fontsize=13)
	_ = plt.xlabel('Actual Values', family='IBM Plex Arabic', fontsize=10)
	_ = plt.ylabel('ECDF percentage', family='IBM Plex Arabic', fontsize=10)
	_ = plt.plot(x, y, c='#677478', marker='o', markersize=2, linewidth=0, linestyle=None, label=f'{feature_name} Record')
	_ = plt.axvline(x=np.median(x), color='magenta', linestyle='--', linewidth=1, label='Median value')
	_ = plt.yticks(np.linspace(0, 1, 11), family='IBM Plex Arabic', fontsize=9)
	_ = plt.grid(which='major', color='#cccccc', alpha=0.5)
	_ = plt.legend(shadow=True)
	plt.show()

	print(f'Average of {feature_name} = {np.mean(x)}')
	print(f'Median of {feature_name} = {np.median(x)}')
	print(f'Standard Deviation of {feature_name} = {np.std(x)}')
	print(f'Minimum value of {feature_name} = {np.min(x)}, Maximum value of {feature_name} = {np.max(x)}')

	return None