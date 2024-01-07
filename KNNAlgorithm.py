#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Alessia Rossi
from operator import itemgetter
import numpy as np
'''
- Definizione dei metodi della classe KNNAlgorithm:
    - costruttore
    - predizione_modello -> Effettua la predizione del modello K-Nearest Neighbors (KNN) sui dati di test forniti
    - clacolo_distanza_euclidea -> Calcola la distanza euclidea tra due punti utilizzando la formula della distanza euclidea standard
'''
class KNNAlgorithm:
    def __init__(self, k, x_train, y_train):
        # Costruttore dell'algoritmo KNN
        #Inizializza i paramentri k, x_train e y_train
        self.k = k
        # Parametri di allenamento modello
        self.x_train = x_train  # Features (B a J)
        self.y_train = y_train  # Labels (K)

    def predizione_modello(self, x_test):
        '''
        - Il metodo predizione_modella presenta due cicli for annidati, il primo per scorrere i punti di test e il secondo per scorrere i punti di allenamento.
          - Per ogni punto_test, viene calcolata la distanza euclidea tra quel punto e tutti i punti presenti nel dataset di addestramento x_train.
          - La distanza euclidea viene calcolata utilizzando il metodo calcolo_distanza_euclidea.
          - Per ogni punto_test, viene creata una lista di distanze, contenente la distanza euclidea tra quel punto e tutti i punti presenti nel dataset di addestramento x_train,
            insieme alle rispettive classi di appartenenza nel dataset y_train.
          - La lista di distanza viene ordinata in modo crescente.
          - Vengono selezionate le prime k distanze della lista ordinata di distanza.
          - Vengono estratte le prime k classi di appartenenza dei punti di allenamento.
          - Viene calcolata la numerosita delle classi dei k vicini.
          - Viene selezionata la classe (o classi) con numerosita maggiore.
          - Nel caso in cui ci siano più classi con numerosità maggiore, viene scelta in modo casuale una delle due classi.
          - La classe scelta viene aggiunta alla lista delle predizioni.
          - I passaggi sono ripetuti per tutti i punti di test presenti nel dataset x_test.
          - Viene restituita la lista contenente le predizioni, ovvero le classi selezionate per ciascun punto di test.
        '''
        # Metodo per effettuare la predizione del modello sui dati di test
        predictions = [] # Lista dove verranno salvate le predizioni
        for _, punto_test in x_test.iterrows(): #_ paramentro che non uso, indica l'indice
            distanze = [] # Lista delle distanza tra il punto x_test ed i punti x_train
            for index, punto_train in self.x_train.iterrows():
                # Calcolo della distanza euclidea tra il punto x_test ed i punti x_train
                dist = self.calcolo_distanza_euclidea(punto_train, punto_test)  # metodo calcolo_distanza_euclidea
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
        '''
        -Il metodo calcolo_distanza_euclidea all'interno della classe KNNAlgorithm, calcola la distanza euclidea tra due punti.
          - Il metodo calcolo_distanza_euclidea riceve in input due punti x1 e x2 e calcola la differenza tra i due punti,
            la eleva al quadrato e ne fa la somma, per poi calcolare la radice quadrata del risultato.
          - Restituisce la distanza euclidea tra i due punti.
        '''
        # Metodo per il calcolo della distanza euclidea
        x3 = x1 - x2 # Differenza tra i due punti
        distanza = np.sqrt(np.sum(pow(x3, 2))) # Calcolo della distanza euclidea
        return distanza

