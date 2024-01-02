#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter
import numpy as np
import pandas as pb

class KNNAlgorithm:
    def __init__(self,k,x_train,y_train):
        self.k = k
        # parametri di allenamento modello
        self.x_train = x_train# x_train rappresenta la matice delle features (B a J)
        self.y_train = y_train  # y_train represent le y (K)


    def predizione_modello(self,x_test):
        #x_test rappresenta la matrice delle features che sono test
        # Classificazione in due gruppi (benigno, maligno)
        ''' confrontare ogni x_test con ogni x_train --> due cicli for
        in questo mi clacolo la distanza euclidea quindi richiamo il metodo della
         distanza euclidea
         per ciascun x_test mi conservo anche la y_train associata , oltre che la distanza
        '''
        distanze=[]
        categoria=[]
        for punto_test in x_test:
            for y,punto_train in enumerate(self.x_train):
                dist= self.calcolo_distanza_euclidea(punto_train,punto_test) #istanza calcolo distanza euclidea
                distanze.append(dist, self.y_train.iloc[y]["Class"]) # mascheramento per la selezione delle y_train associate

            # ordino in modo crescente le distanze (con associate y_test)
            sorted(distanze, key=itemgetter(0), reverse=True)
            k_vicini = distanze[:self.k]
            vicini, numerosita = np.unique(k_vicini, return_counts=True)
            max_numerosita = max(numerosita)

            for i in k_vicini[0]:
                if k_vicini[1] == max_numerosita:
                    categoria.append(k_vicini[0])



        # ordino in modo crescente le distanze (con associate y_test)
        # prendo le prime k distanze
        # analizzo (conto) le y_test e prendo la y_test più numerosa
        # OSS: nel caso sono di numero uguali ne prendo una a le due a caso

        # return: sarebbe il y_test trovata

    def calcolo_distanza_euclidea(self,x1,x2):
        #return: distanza euclidea tra vettore x_test e x_train
        x3=x1-x2
        distanza= np.sqrt(np.sum(pow(x3,2)))
        return distanza






