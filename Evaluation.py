#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    def __init__(self):
        pass

    '''   
    Il processo di valutazione holdout consiste in:
    1. Dividire i dati: i dati vengono divisi casualmente (viene specificata la percentuale in input dall'utente) in dati di training e dati di test
    2. Addestramento del modello: il modello quindi si addestra dandogli "in pasto" i dati x_train e y_train
    3. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (x_test). Le prestazione del modello vengono calcolate tramite diverse metriche
    4. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti
    '''
    def valutazione_holdout(self, x_train, y_train, x_test, y_test):
        
        '''
        this.x_train = x_train
        this.y_train = y_train
        this.x_test = x_test
        this.y_test = y_test
        '''

        pass

    
    ''' 
    Il processo di valutazione random subsampling consiste in:
    1. Specificare in input il numero di esperimenti (K) da effettuare
    2. Specificare in input la percentuale per i dati di train e test
    3. 
    '''
    
    def valutazione_random_subsampling(self, K):
        # this.K = K # Indica il numero di esperimenti da fare nel caso di valutazione di tipo "Random Subsampling"
        pass

    def calcolo_metrice(self):
        pass