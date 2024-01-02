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
        self.dati = dati
        self.perc_train = perc_train


    '''   
    Il processo di valutazione holdout consiste in:
    1. Dividire i dati: i dati vengono divisi casualmente (viene specificata la percentuale in input) in dati di training e dati di test
    2. Addestramento del modello: il modello quindi si addestra dandogli "in pasto" i dati X_train e y_train
    3. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (x_test). Le prestazione del modello vengono calcolate tramite diverse metriche
    4. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti
    '''
    def valutazione_holdout(self):

        dati_di_training = self.dati_x.sample(frac =  self.perc_train) # Prendo una percentuali dei dati per il training
        
        dati_di_testing = df.drop(dati_di_training.index) # I dati rimanenti li utilizzo per il testing

        X_train = dati_di_training.drop(columns=['Class']) # Dai dati utilizzati per il training, elimino la colonna indicante l'etichetta di appartenenze. Mi creo X_train
        y_train = dati_di_trainig['Class'] # Dai dati per il train mi salvo solo la colonna indicante l'etichetta di appartenenza. Mi creo y_train
        X_test = dati_di_testing.drop(columns=['Class']) # Dai dati utilizzati per il testing, elimino la colonna indicante l'etichetta di appartenenza. Mi creo X_test
        y_yest = dati_di_testing['Class'] # Dai dati di test mi salvo solo la colonna indicante l'etichetta di appartentenza. Mi creo y_test

        # la classe KNN ha ora solo il costruttore dove viene passato K, X_train, y_train
        KNNAlgorithm.allenamento_dati(X_train, y_train) # Alleno il modello fornendogli i dati di training
        
        # Vettore di etichette (class)
        predizione = KNNAlgorithm.predizione_modello(X_test) # Svolgo la predizione con il modello allenato precedentemente

    
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
    def calcolo_metrice(self, X_test, y_test, prediction):
        pass