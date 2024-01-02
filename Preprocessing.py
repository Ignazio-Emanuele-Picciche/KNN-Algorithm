#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Le funzioni della classe preprocessing sono:
# caricare il dataset
# gestire i valori mancanti
# dividere i dati in features (x) e target label (y)
# normalizzare o standardizzare i dati a seconda della scelta
# passare i dati alla classe evaluation


import pandas as pd


class preprocessing():
    dati = pd.DataFrame()

    def __init__(self):
        pass

    def caricamento_dataset(self):  # creazione metodo caricamento dataset
        self.dati = pd.read_csv('breast_cancer.csv',
                                index_col="Sample code number")  # viene importato il dataset, e la prima colonna viene utilizzata per gli indici
        return self.dati

    def suddivisione_dati(self):  # i dati vengono suddivisi in features (le x) e target label (le y). Entrambi dovranno avere il corrispondente indice
        x = self.dati.iloc[:, :-1]  # features
        y = self.dati["Class"] #target label

        return x, y


#dati1 = preprocessing()
#dati1.caricamento_dataset()
#print(dati1.suddivisione_dati())
