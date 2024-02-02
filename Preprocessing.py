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
    - At first, in the loading_dataset method, the dataset is loaded from the csv file.
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


    def __init__(self):
        self.dataset_path = input("Enter the path of the dataset: ")


    def loading_dataset(self):  # creazione metodo caricamento dataset
        try:
            self.data = pd.read_csv(self.dataset_path) #importo il file csv
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)



    def data_cleaning(self): # creazione metodo pulizia dati che gestisce i valori mancanti
        self.data = self.data.dropna() # le righe corrispondenti ai valori mancanti vengono eliminate
        self.data = self.data.drop(columns=['Sample code number']) # la colonna Sample code number viene eliminata in quanto non utile per la classificazione


    def standardization(self): # creazione metodo standardizzazione per il feature scaling, da applicare a tutte le colonne tranne l'ultima (target label)
        for i in range(0, len(self.data.columns) - 1):
            self.data.iloc[:, i] = (self.data.iloc[:, i] - self.data.iloc[:, i].mean()) / self.data.iloc[:, i].std()


    def data_split(self):  # i dati vengono suddivisi in features (le x) e target label (le y). Entrambi dovranno avere il corrispondente indice
        x = self.data.iloc[:, :-1]  # features (x)
        y = self.data["Class"] #target label (y)
        y = y.astype(int) #trasformo le y in interi
        return x, y




prova = Preprocessing()
prova.loading_dataset()
prova.data_cleaning()
prova.standardization()
prova.data_split()
print(prova.data_split())
