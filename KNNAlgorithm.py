#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Alessia Rossi
from operator import itemgetter
import numpy as np

class KNNAlgorithm:
    def __init__(self, k, x_train, y_train):
        # Costruttore dell'algoritmo KNN
        #Inizializza i paramentri k, x_train e y_train
        self.k = k
        # Parametri di allenamento modello
        self.x_train = x_train  # Features (B a J)
        self.y_train = y_train  # Labels (K)

    def predizione_modello(self, x_test):
        # Metodo per effettuare la predizione del modello sui dati di test
        ''' confrontare ogni x_test con ogni x_train --> due cicli for
        in questo mi clacolo la distanza euclidea quindi richiamo il metodo della
         distanza euclidea
         per ciascun x_test mi conservo anche la y_train associata , oltre che la distanza
        '''
        predictions = [] # Lista dove verranno salvate le predizioni
        for _, punto_test in x_test.iterrows(): #_ paramentro che non uso, indica l'indice
            distanze = [] # Lista delle distanza tra il punto x_test ed i punti x_train
            for index, punto_train in self.x_train.iterrows():
                # Calcolo della distanza euclidea tra il punto x_test ed i punti x_train
                dist = self.calcolo_distanza_euclidea(punto_train, punto_test)  # Istanza calcolo_distanza_euclidea
                # Aggiungiamo alla lista distanze la coppia distanza,classe di appartenenza
                distanze.append((dist,self.y_train[index])) #loc mi restituisce la riga corrispondente all'indice

            # Ordiniamo in modo crescente le distanze
            distanze = sorted(distanze, key=itemgetter(0), reverse=True)
            # Selezioniamo le prime k distanze della lista ordinatata di distanze
            k_distanze = distanze[:self.k]
            # Estraiamo le classi corrispondenti ai primi k
            k_vicini = np.array(k_distanze)[:, 1]

            # Contiamo la numerosità delle classi dei k vicni
            vicini, numerosita = np.unique(k_vicini, return_counts=True)
            # Selezioniamo quelle con numerosità maggiore
            max_numerosita = max(numerosita)
            # Creo una lista contenente la classe ( o le classi) con numerosità pari a quella massima
            piu_comuni = [vicini[i] for i, elem in enumerate(numerosita) if max_numerosita == elem]
            # Nel caso sia presento sono una classe nella lista la aggiungo a predizioni
            # Altrimenti scelgo in modo cosuale una delle due
            if len(piu_comuni) == 1:
                predictions.append(piu_comuni)
            else:
                predictions.append(np.random.choice(piu_comuni))
        # Viene resituita la lista delle preizioni, contenente le classi prendette per ciasun x_test
        return predictions

    def calcolo_distanza_euclidea(self, x1, x2):
        # Metodo per il calcolo della distanza euclidea
        x3 = x1 - x2
        distanza = np.sqrt(np.sum(pow(x3, 2)))
        return distanza

