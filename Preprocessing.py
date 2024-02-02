#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
- Definition of the methods of the Preprocessing class:
    - constructor
    - loading_dataset -> Loads the dataset from the csv file
    - data_cleaning -> Manages missing values
    - standardization -> Performs feature scaling
    - data_split -> Splits the dataset into features (x) and target label (y)
'''


import pandas as pd
import sys


class Preprocessing():

    '''
    The Preprocessing class is necessary to load and prepare the data for the program. It uses the pandas library.
    This class is structured as follows:
    - The constructor asks the user to enter the path of the dataset.
    - In the loading_dataset method, the dataset is loaded from the csv file.
    - Then, in the data_cleaning method, if there are missing values, the rows corresponding to the missing values are deleted.
      The first column (with "sample code number") is also deleted because it is not useful for classification.
    - Then, in the standardization method, the data are standardized.
      This process does not involve the last column, corresponding to the type of tumor of the cells. 
      This type of feature scaling is necessary because the data may have outlayers and different scales, 
      which would make the classification inaccurate.
    - Finally, in the data_split method, the data are divided into features (x) and target label (y).
      The features (called "x") are all the columns except the last one. These are the caractheristics of the cell,
      and the algorithm uses these to predict the type of tumor, which is the target label (called "y") is the last column.
      The features and target label have the corresponding index.
    '''


    def __init__(self): # Constructor of the Preprocessing class

        self.dataset_path = input("Enter the path of the dataset: ") # the user is asked to enter the path of the dataset


    def loading_dataset(self): # creation of the method to load the dataset from the csv file
        '''
        The loading_dataset method loads the dataset from the csv file.
        If the file is not found, the program says "File not found" and stops.

        self.data is the dataset. It is made up of rows (for every tumor cell) and columns (with the characteristics
        of every cell), and it is a pandas dataframe.
        self.dataset is preprocessed in this class.
        '''
        try:
            self.data = pd.read_csv(self.dataset_path) # the dataset is loaded from the csv file
        except FileNotFoundError: # if the file is not found
            print("File not found") # the program says "File not found"
            sys.exit(1) # and stops



    def data_cleaning(self): # creation of the method to manage missing values
        '''
        This method manages missing values. If there are missing values,
        the rows corresponding to the missing values are deleted.
        The first column (with "sample code number") is also deleted because it is not useful for classification.
        '''
        self.data = self.data.dropna() # rows with missing values are deleted
        self.data = self.data.drop(columns=['Sample code number']) # the sample code number column is deleted


    def standardization(self): # creation of the method to standardize the dat
        '''
        This method standardizes the data. The standardization process is necessary because the data
        may have outlayers and different scales. This process does not involve the last column,
        because it is the target label, and it is not useful to standardize it.
        The standardization process is done by subtracting the mean and dividing by the standard deviation.
        '''
        for i in range(0, len(self.data.columns) - 1): # for every column except the last one
            self.data.iloc[:, i] = (self.data.iloc[:, i] - self.data.iloc[:, i].mean()) / self.data.iloc[:, i].std() # the data are standardized,
            # for  every value in the column, the mean is subtracted and the result is divided by the standard deviation


    def data_split(self):  # creation of the method to split the dataset into features and target label
        '''
        In this method, the dataset is divided into features (x) and target label (y).
        The features (called "x") are all the columns except the last one. These are the caractheristics of the cell,
        and the algorithm uses these to predict the type of tumor, which is the target label (called "y") is the last column.
        '''
        x = self.data.iloc[:, :-1]  # all the columns except the last one are the features (x)
        y = self.data["Class"] # the last column (class) is the target label (y)
        y = y.astype(int) # the target label is converted to int
        return x, y # the features and the target label are returned





