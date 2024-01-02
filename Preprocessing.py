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
    def __init__(self):
        pass

    def caricamento_dataset(self, dati):    #creazione metodo caricamento dataset
        self.dati = pd.read_csv('breast_cancer', index_col="Sample code number") #viene importato il dataset, e la prima colonna viene utilizzata per gli indici

