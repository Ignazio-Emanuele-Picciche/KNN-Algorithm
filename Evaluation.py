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

    def valutazione_holdout(self, x_train, y_train, x_test, y_test):
        
        '''this.x_train = x_train
        this.y_train = y_train
        this.x_test = x_test
        this.y_test = y_test'''

        pass

    def valutazione_random_subsampling(self, K):
        # this.K = K # Indica il numero di esperimenti da fare nel caso di valutazione di tipo "Random Subsampling"
        pass

    def calcolo_metrice(self):
        pass