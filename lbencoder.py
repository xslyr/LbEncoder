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
		self.labels = []


	def get_unique(self, data):
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
		
	
	def fit_by_order(self, data, sort_by=()):
		if not (isinstance(data, np.ndarray) or isinstance(data, pd.Series)):
			raise Exception('The data parameter must be Panda Series or Numpy Array')
		
		self.data = data.copy()
		super().fit(self.data)
		self.labels = self.classes_

		if isinstance(sort_by, str):
			if sort_by in ['desc','occurrence']:
				self.labels = self.get_current_sort(self.data)
				if sort_by == 'desc':
					self.labels.sort(reverse=True)
		elif isinstance(sort_by, list):
			self.labels = sort_by
		
		self.classes_ = np.array(self.labels, dtype=object)


	def fit_transform(self, data, sort_by=()):
		if not (isinstance(data, np.ndarray) or isinstance(data, pd.Series)):
			raise Exception('The data parameter must be Panda Series or Numpy Array')
		
		self.fit_by_order(data, sort_by=sort_by)
		self.data = super().transform(self.data)
		return self.data
