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


class Preprocessing():
    data = pd.DataFrame()



    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        pass

    def loading_dataset(self):  # creazione metodo caricamento dataset
        self.data = pd.read_csv(self.dataset_path) #importo il file csv



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




#prova = Preprocessing()
#prova.loading_dataset()
#prova.data_cleaning()
#prova.standardization()
#prova.data_split()
#print(prova.data_split())
