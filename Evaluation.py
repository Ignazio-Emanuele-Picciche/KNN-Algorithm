#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import KNNAlgorithm as KNNAlgorithm

'''

@author: Piccichè-Ignazio-Emanuele

Dic 28/12/2023
- Definizione dei metodi della classe Evaluation:
    - costruttore
    - valutazione_holdout -> Verrà richiamato questo metodo quando l'utente vorra fare la valutazione della predizione mediante la metodologia "Holdout"
    - valutazione_random_subsampling -> Verrà richiamato questo metodo quando l'utente vorra fare la valutazione della predizione mediante la metodologia "Random Subsampling"
    - calcolo_metrice -> Questo metodo viene richiamato, indipendentemente dal tipo di valutazione scelto, per calcolare le metriche come (Accuracy Rate, Error Rate, Sensitivity, ...)


'''

class Evaluation:

    def __init__(self, features, target, perc_train, k):
        self.features = features
        self.target = target
        self.perc_train = perc_train
        self.k = k
        


    def split_dati(features, target, perc_train):
        X_train = features.sample(frac = perc_train)    # Dai dati utilizzati per il training
        X_test = features.drop(X_train.index)   # Dai dati utilizzati per il testing

        y_train = y_train[X_train.index == y_train.index]   # Mi salvo le y di train corrispondenti alle x di train
        y_test = y_test[X_test.index == y_test.index]   # Mi salvo le y di test corrispondenti alle x di test

        return X_train, y_train, X_test, y_test


    '''   
    Il processo di valutazione holdout consiste in:
    1. Dividire i dati: i dati vengono divisi casualmente (viene specificata la percentuale in input) in dati di training e dati di test
    2. Addestramento del modello: il modello quindi si addestra dandogli "in pasto" i dati X_train e y_train
    3. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (x_test). Le prestazione del modello vengono calcolate tramite diverse metriche
    4. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti
    '''
    def valutazione_holdout(self):
        X_train, y_train, X_test, Y_test = self.split_dati(self.features, self.target, self.perc_train)

        # la classe KNN ha ora solo il costruttore dove viene passato K, X_train, y_train
        KNNAlgorithm.allenamento_dati(X_train, y_train) # Alleno il modello fornendogli i dati di training
        prediction = KNNAlgorithm.predizione_modello(X_test) # Svolgo la predizione con il modello allenato precedentemente

        return self.calcolo_metrice(y_test, prediction) # per ora le ritorno, in futuro verrà implementato che questi indici vengono salvati in un file

    
    ''' 
    Il processo di valutazione random subsampling consiste in:
    1. Specificare in input il numero di esperimenti (K) da effettuare
    2. Specificare in input la percentuale per i dati di train e test
    3. Addestramento del modello: il modello viene addestrato quindi utilizzando X_train e y_train
    4. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (X_test). Le prestazione del modello vengono calcolate tramite diverse metriche
    5. Iterazioni multiple: il processo viene ripetuto piu volte (K volte), con nuove suddivisioni casuali del dataset, per ottenere una stima più robusta della performance del modello. Infine le valutazioni multiple vengono aggregate per ottenere una misura comune delle prestazioni del modello.
    6. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti
    '''
    def valutazione_random_subsampling(self, K):
        # this.K = K # Indica il numero di esperimenti da fare nel caso di valutazione di tipo "Random Subsampling"
        pass

    '''
    In questo metodo andremo a calcolare, grazie anche all'ausilio della confution matrix, le seguenti metriche:
    - Accuracy Rate
    - Error Rate
    - Sensitivity
    - SpeciCicity
    - Geometric Mean
    '''
    def calcolo_metrice(self, y_test, prediction):
        pass