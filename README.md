# LbEncoder
This library goals to provide greater freedom in the Label Encoding process when compared to the sklearn standard.

Methods:

  - ***get_unique***: return a unique values of pandas.Series or numpy.Array

  - ***get_current_sort***: return current sort of pandas.Series or numpy.Array.

  - ***fit_by_order***: do a fit process similar sklearn.LabelEncoder.
    The necessary parameters is data of column that we'll encoding and the sort_by that can be ('asc','desc','occurrence' or a list with elements sorted according your preference)

  - ***fit_transform***: do a fit process similar sklearn.LabelEncoder.
    The necessary parameters is data of column that we'll encoding and the sort_by that can be ('asc','desc','occurrence' or a list with elements sorted according your preference)
    
    
See the "Example Usage" file to more details.
