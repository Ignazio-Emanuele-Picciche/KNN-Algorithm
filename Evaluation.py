#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from KNNAlgorithm import KNNAlgorithm

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
    - calcolo_metrice: sviluppato il cuore del metodo, dove vado a calcolare le metriche richieste (Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean) e le ritorno

Gen 05/01/2023
- Continuo sviluppo metodi della classe:
    - salva_metriche: sviluppato il metodo che va a salvare le metriche calcolate nel file Metriche.txt
    - plot_delle_metriche: sviluppato il metodo che va a plottare le metriche calcolate. La rappresentazione avviene tramite un grafico a barre
'''

# La classe Evaluation viene utilizzata per valutare le performance del modello implementato (KNN).
# I metodi della classe per valutare il modello sono:
# - valutazione_holdout: metodo che va a valutare il modello mediante la metodologia "Holdout"
#   - il metood, quindi, divide i dati in un set di addestramento e un set di test. Il modello viene addestrato sul set di addestramento e poi testato sul set di test. Successivamente vengono calcolate le metriche di valutazione richieste.
# - valutazione_random_subsampling: metodo che va a valutare il modello mediante la metodologia "Random Subsampling"
#   - simile alla metodologia "Holdout", ma viene ripetuta più volte con diversi set di addestramento e test. Successivamente vengono calcolate le metriche di valutazione richieste.
# - calcolo_metrice: metodo che va a calcolare le metriche di valutazione richieste (Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean)
# - salva_metriche: metodo che va a salvare le metriche calcolate nel file Metriche.txt
# - plot_delle_metriche: metodo che va a plottare le metriche calcolate. La rappresentazione avviene tramite un grafico a barre
class Evaluation:
    
    def __init__(self, features, target, perc_train, k):
        self.features = features
        self.target = target
        self.perc_train = perc_train
        self.k = k
        
    '''
    In questo metodo vengono divisi i dati in dati di train e dati di test.

    I dati di train sono i dati che verranno utilizzati per addestrare il modello.
    I dati di test sono i dati che verranno utilizzati per testare il modello.
    '''
    def split_dati(self, features, target, perc_train):
        X_train = features.sample(frac = perc_train/100)    # Prendo i dati per il training secondo una percentuale specificata in input
        X_test = features.drop(X_train.index)   # Prendo i dati per il test, che sono tutti i dati che non sono stati presi per il training

        y_train = target.drop(X_test.index) # Mi salvo le y di train corrispondenti alle x di train
        y_test = target.drop(X_train.index) # Mi salvo le y di test corrispondenti alle x di test

        return X_train, y_train, X_test, y_test


    '''   
    Il processo di valutazione holdout consiste in:
    1. Dividire i dati: i dati vengono divisi casualmente (viene specificata la percentuale in input) in dati di training e dati di test
    2. Addestramento del modello: il modello quindi si addestra dandogli "in pasto" i dati X_train e y_train
    3. Test del modello: il modello viene quindi testato con i dati di test (X_test)
    4. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (y_test). Le prestazione del modello vengono calcolate tramite diverse metriche
    5. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti
    '''
    def valutazione_holdout(self):
        X_train, y_train, X_test, y_test = self.split_dati(self.features, self.target, self.perc_train) # richiamo il metodo che va a splittare i dati in dati di train e dati di test

        knnModel = KNNAlgorithm(self.k, X_train, y_train) # Alleno il modello fornendogli i dati di training
        prediction = knnModel.predizione_modello(X_test) # Effettuo la predizione con il modello allenato precedentemente

        Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = self.calcolo_metrice(y_test, prediction) # richiamo il metodo che va a calcolare le metriche, passandogli i dati di test e le predizioni
        self.salva_metriche(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean) # richiamo il metodo che va a salvare nel file Metriche.txt le metriche appena calcolate
        self.plot_delle_metriche(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean) # richiamo il metodo che va a plottare le metriche calcolate

    ''' 
    Il processo di valutazione random subsampling consiste in:
    1. Specificare in input il numero di esperimenti (K) da effettuare
    2. Specificare in input la percentuale per i dati di train e test
    3. Addestramento del modello: il modello viene addestrato quindi utilizzando X_train e y_train
    4. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (y_test). Le prestazione del modello vengono calcolate tramite diverse metriche
    5. Iterazioni multiple: il processo viene ripetuto piu volte (K volte), con nuove suddivisioni casuali del dataset, per ottenere una stima più robusta della performance del modello. Infine le valutazioni multiple vengono aggregate per ottenere una misura comune delle prestazioni del modello.
    6. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti
    '''
    def valutazione_random_subsampling(self, K):
        # Inizializzo le liste che conteranno i valori delle metriche calcolate per ogni iterazione
        Accuracy_rate_scores = []
        Error_rate_scores = []
        Sensitivity_scores = []
        Specificity_scores = []
        Geometric_mean_scores = []

        # Come previsto dal processo di valutazione random subsampling, il processo viene ripetuto K volte
        for _ in range(K):
            X_train, y_train, X_test, y_test = self.split_dati(self.features, self.target, self.perc_train) # richiamo il metodo che va a splittare i dati in dati di train e dati di test

            knnModel = KNNAlgorithm(self.k, X_train, y_train) # Alleno il modello fornendogli i dati di training
            prediction = knnModel.predizione_modello(X_test) # Effettuo la predizione con il modello allenato precedentemente

            Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = self.calcolo_metrice(y_test, prediction) # richiamo il metodo che va a calcolare le metriche, passandogli i dati di test e le predizioni
            
            # Aggiungo i valori delle metriche calcolate nelle liste
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

        self.salva_metriche(Accuracy_rate_mean, Error_rate_mean, Sensitivity_mean, Specificity_mean, Geometric_mean_mean) # richiamo il metodo che va a salvare le metriche calcolate, nel file Metriche.txt
        self.plot_delle_metriche(Accuracy_rate_mean, Error_rate_mean, Sensitivity_mean, Specificity_mean, Geometric_mean_mean) # richiamo il metodo che va a plottare le metriche calcolate

    '''
    In questo metodo vengono calcolate prima i valori della confusion matrix, per poi calcolare le metriche richieste.

    Le metriche calcolate sono:
    - Accuracy Rate
    - Error Rate
    - Sensitivity
    - SpeciCicity
    - Geometric Mean
    '''
    def calcolo_metrice(self, y_test, prediction):
        # Calcolo della confusion matrix
        True_Negative = sum(1 for y, pred in zip(y_test, prediction) if (y == pred and pred == 2)) # Calcolo il valore True Negative della confusion matrix
        True_Positive = sum(1 for y, pred in zip(y_test, prediction) if (y == pred and pred == 4)) # Calcolo il valore True Positive della confusion matrix
        False_Positive = sum(1 for y, pred in zip(y_test, prediction) if (y != pred and pred == 2)) # Calcolo il valore False Positive della confusion matrix
        False_Negative = sum(1 for y, pred in zip(y_test, prediction) if (y != pred and pred == 4)) # Calcolo il valore False Negative della confusion matrix
        
        # Calcolo effettivo delle metriche richieste mediante i valori della confusion matrix, precedentemente calcolati
        Accuracy_rate = (True_Negative + True_Positive) / y_test.size # Percentuale di predizioni corrette rispetto al totale delle predizioni
        Error_rate = (False_Positive + False_Negative) / y_test.size # Percentuale di predizioni errate rispetto al totale delle predizioni
        Sensitivity = (True_Positive) / (True_Positive + False_Negative) # Capacità del modello di predire correttamente i valori positivi
        Specificity = (True_Negative) / (True_Negative + False_Positive) # Capacità del modello di predire correttamente i valori negativi
        Geometric_mean = np.sqrt((Sensitivity*Specificity)) # Media che bilancia valori positivi e negativi

        return Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean


    '''
    In questo metodo vengono salvate le metriche calcolate in un file txt.
    
    Le metriche salvate sono:
    - Accuracy Rate
    - Error Rate
    - Sensitivity
    - SpeciCicity
    - Geometric Mean

    Il nome del file sarà: "Metriche.txt"
    '''
    def salva_metriche(self, Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean):
        # Con le seguenti operazioni apro il file Metriche.txt e ci scrivo dentro le metriche calcolate
        with open('Metriche.txt', 'w') as file:
            file.write('Accuracy Rate: ' + str(Accuracy_rate) + '\n')
            file.write('Error Rate: ' + str(Error_rate) + '\n')
            file.write('Sensitivity: ' + str(Sensitivity) + '\n')
            file.write('Specificity: ' + str(Specificity) + '\n')
            file.write('Geometric Mean: ' + str(Geometric_mean) + '\n')
        file.close() # Chiudo il file Metriche.txt

    '''
    In questo metodo viene plottato un grafico a barre che va a rappresentare le metriche calcolate.
    La rappresentazione avviene tramite la libreria matplotlib.
    '''
    def plot_delle_metriche(self, Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean):
        etichette = ['Accuracy Rate', 'Error Rate', 'Sensitivity', 'Specificity', 'Geometric Mean'] # Vettore utilizzato per rappresentare le etichette del grafico
        valori = [Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean] # Vettore utilizzato per rappresentare i valori del grafico corrispondenti alle etichette
        colori = ['blue', 'green', 'red', 'yellow', 'orange'] # Vettore utilizzato per i colori delle barre del grafico

        plt.figure(figsize=(10, 5)) # Imposto la dimensione del grafico
        plt.bar(etichette, valori, color=colori) # Creo il grafico a barre. In x metto le etichette, in y metto i valori
        plt.xlabel("Metriche") # Imposto l'etichetta dell'asse x
        plt.ylabel("Valori") # Imposto l'etichetta dell'asse y
        plt.title("Grafico delle metriche") # Imposto il titolo del grafico
        plt.show() # Mostro il grafico