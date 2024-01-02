#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import KNNAlgorithm as KNNAlgorithm

'''

@author: Piccichè-Ignazio-Emanuele

Dic 28/12/2023
- Definizione dei metodi della classe Evaluation:
    - costruttore
    - valutazione_holdout -> Verrà richiamato questo metodo quando l'utente vorra fare la valutazione della predizione mediante la metodologia "Holdout"
    - valutazione_random_subsampling -> Verrà richiamato questo metodo quando l'utente vorra fare la valutazione della predizione mediante la metodologia "Random Subsampling"
    - calcolo_metrice -> Questo metodo viene richiamato, indipendentemente dal tipo di valutazione scelto, per calcolare le metriche come (Accuracy Rate, Error Rate, Sensitivity, ...)

Gen 02/01/2023
- Continuo sviluppo metodi della classe:
    - split_dati: implementato questo metodo dove, in base ai parametri features e target, vado a splittare i dati di train (X e y) e i dati di test (X e y) secondo la percentuale specificata in input
    - valutazione_holdout: sviluppato il cuore del metodo, dove vado a richiamare prima il metodo di splitting e poi i metodi della classe KNNAlgorithm per allennare il modello e fare la predizione
    - valutazione_random_subsampling: sviluppato il cuore del metodo, dove vado a richiamare prima il metodo di splitting e poi i metodi della classe KNNAlgorithm per allennare il modello e fare la predizione

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

        y_train = features[X_train.index == features.index]   # Mi salvo le y di train corrispondenti alle x di train
        y_test = features[X_test.index == features.index]   # Mi salvo le y di test corrispondenti alle x di test

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
        knnModel = KNNAlgorithm.__init__(k, X_train, y_train) # Alleno il modello fornendogli i dati di training
        prediction = knnModel.predizione_modello(X_test) # Svolgo la predizione con il modello allenato precedentemente

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

        Accuracy_rate_scores = []
        Error_rate_scores = []
        Sensitivity_scores = []
        Specificity_scores = []
        Geometric_mean_scores = []

        for _ in range(K):
            X_train, y_train, X_test, Y_test = self.split_dati(self.features, self.target, self.perc_train)

            knnModel = KNNAlgorithm.__init__(k, X_train, y_train) # Alleno il modello fornendogli i dati di training
            prediction = knnModel.predizione_modello(X_test) # Svolgo la predizione con il modello allenato precedentemente

            Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = self.calcolo_metrice(y_test, prediction)

            Accuracy_rate_scores.append(Accuracy_rate)
            Error_rate_scores.append(Error_rate)
            Sensitivity_scores.append(Sensitivity)
            Specificity_scores.append(Specificity)
            Geometric_mean_scores.append(Geometric_mean)

        # Calcolo i valori medi per ogni metrica calcolata
        Accuracy_rate_mean = np.mean(Accuracy_rate_scores)
        Error_rate_mean = np.mean(Error_rate_scores)
        Sensitivity_mean = np.mean(Sensitivity_scores)
        Specificity_mean = np.mean(Specificity_scores)
        Geometric_mean_mean = np.mean(Geometric_mean_scores)

        return Accuracy_rate_mean, Error_rate_mean, Sensitivity_mean, Specificity_mean, Geometric_mean  # per ora le ritorno, in futuro verrà implementato che questi indici vengono salvati in un file

    '''
    In questo metodo andremo a calcolare, grazie anche all'ausilio della confution matrix, le seguenti metriche:
    - Accuracy Rate
    - Error Rate
    - Sensitivity
    - SpeciCicity
    - Geometric Mean
    '''
    def calcolo_metrice(self, y_test, prediction):
        # Calcolo della confusion matrix
        True_Negative = sum(1 for y, pred in zip(y_test, prediction) if (y == pred and pred == 2))  
        True_Positive = sum(1 for y, pred in zip(y_test, prediction) if (y == pred and pred == 4))
        False_Positive = sum(1 for y, pred in zip(y_test, prediction) if (y != pred and pred == 2))
        False_Negative = sum(1 for y, pred in zip(y_test, prediction) if (y != pred and pred == 4))
        
        Accuracy_rate = (True_Negative + True_Positive) / y_test.size
        Error_rate = (False_Positive + False_Negative) / y_test.size
        Sensitivity = (True_Positive) / (True_Positive + False_Negative) 
        Specificity = (True_Negative) / (True_Negative + False_Positive)
        Geometric_mean = np.sqrt((Sensitivity*Specificity))

        return Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean