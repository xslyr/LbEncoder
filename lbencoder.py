#/usr/bin/python3
#!encoding:utf8
#
#	Created at 26-05-2023
#	Coder: Wesley R. Silva
#	Library functionality extension of sklearn.LabelEncoder that allows us to change the numerical order of the results
#

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

class LbEncoder(LabelEncoder):
	
	def __init__(self):
		super().__init__()
		"""Sort Options Available:
	- 'asc': sort by column ascending
	- 'desc': sort by column descending
	- 'occurrence' : sort by occurrences of data on column 
	- ['a','c','d'] : sort by specific list ordering"""
		self.labels = []
		
	
	def get_unique_values(self, data):
		if isinstance(data, pd.Series):
			return data.unique()
		elif isinstance(data, np.ndarray) or isinstance(data, list):
			return np.unique(data)
		else:
			raise ValueError("The parameter isn't of knowed type")


	def get_current_sort(self,data):
		current_sort =[]
		for i in data:
			if i not in current_sort:
				current_sort.append(i)
		return current_sort
		
	
	def fit(self, data, sort_by=()):
		if not (isinstance(data, np.ndarray) or isinstance(data, pd.Series)):
			raise Exception('The data parameter must be Panda Series or Numpy Array')
		
		if isinstance(sort_by[0], str):
			if sort_by[0] == 'asc':
				super().fit(data)
			elif sort_by[0] in ['desc','occurrence']:
				super().fit(data)
				if sort_by[0] == 'desc':
					aux = data.sort_values(ascending=False, kind='heapsort')
				#self.classes_ = np.ndarray(self.get_current_sort(aux), dtype=object)
				self.classes_ = self.get_current_sort(aux)
		
		elif isinstance(sort_by[0], list):
			super().fit(data)
			#self.classes_ = np.ndarray(sort_by[0], dtype=object)
			self.classes_ = sort_by[0]
		
		#self.labels = self.classes_
		
		
	def fit_transform(self, data, sort_by=()):
		if not (isinstance(data, np.ndarray) or isinstance(data, pd.Series)):
			raise Exception('The data parameter must be Panda Series or Numpy Array')
		
		data_return = data
		if isinstance(sort_by[0], str):
			if sort_by[0] == 'asc':
				data_return = super().fit_transform(data_return)
			elif sort_by[0] in ['desc','occurrence']:
				super().fit(data_return)
				if sort_by[0] == 'desc':
					aux = data_return.sort_values(ascending=False, kind='heapsort')
				#self.classes_ = np.ndarray(self.get_current_sort(aux), dtype=object)
				self.classes_ = self.get_current_sort(aux)
				data_return = super().transform(data_return)
		
		elif isinstance(sort_by[0], list):
			super().fit(data)
			self.classes_ = sort_by[0]
			data_return = super().transform(data_return)
		
		return data_return
		

