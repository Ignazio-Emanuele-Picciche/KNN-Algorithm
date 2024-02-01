#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importo le librerie necessarie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from KNNAlgorithm import KNNAlgorithm

'''
@Author: Ignazio Emanuele Piccichè

- Definizione dei metodi della classe Evaluation:
    - constructor
    - data_splitting -> Metodo che va a dividere i dati in dati di train e dati di test
    - holdout_validation -> Metodo che va a valutare il modello mediante la metodologia "Holdout"
    - random_subsampling_validation -> Metodo che va a valutare il modello mediante la metodologia "Random Subsampling"
    - metrics_calculation -> Metodo che va a calcolare le metriche di valutazione richieste (Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean)
    - save_metrics -> Metodo che va a salvare le metriche calcolate nel file Metriche.txt
    - metrics_plot -> Metodo che va a plottare le metriche calcolate. Plot delle metriche in funzione al numero di esperimenti e boxplot delle metriche.
'''
class Evaluation:
    

    '''
    constructor

    Parameters
    ----------
    features : pandas.DataFrame
        dati che verranno utilizzati per addestrare e testare il modello
    target : pandas.Series
        dati che verranno utilizzati per addestrare e testare il modello
    training_perc : int
        percentuale di dati che verranno utilizzati per addestrare il modello
    k : int
        numero di vicini da considerare
    chosen_metrics : list
        lista che contiene le metriche scelte dall'utente

    Returns
    -------
    None
    '''
    def __init__(self, features:pd.DataFrame, target:pd.Series, training_perc:int, k:int, chosen_metrics:list):
        self.features = features
        self.target = target
        self.training_perc = training_perc
        self.k = k
        self.chosen_metrics = chosen_metrics
        
    '''
    In questo metodo vengono divisi i dati in dati di train e dati di test.

    I dati di train sono i dati che verranno utilizzati per addestrare il modello.
    I dati di test sono i dati che verranno utilizzati per testare il modello.

    Parameters
    ----------
    features : pandas.DataFrame
        dati che verranno utilizzati per addestrare e testare il modello
    target : pandas.Series
        dati che verranno utilizzati per addestrare e testare il modello
    training_perc : int
        percentuale di dati che verranno utilizzati per addestrare il modello

    Returns
    -------
    X_train : pandas.DataFrame
        dati che verranno utilizzati per addestrare il modello
    y_train : pandas.Series
        dati che verranno utilizzati per addestrare il modello
    X_test : pandas.DataFrame
        dati che verranno utilizzati per testare il modello
    y_test : pandas.Series
        dati che verranno utilizzati per testare il modello
    '''
    def data_splitting(self, features:pd.DataFrame, target:pd.Series, training_perc:int):
        X_train = features.sample(frac = training_perc/100) # Prendo i dati per il training secondo una percentuale specificata in input
        X_test = features.drop(X_train.index) # Prendo i dati per il test. Sono tutti i dati che non sono stati presi per il training

        y_train = target.drop(X_test.index) # Mi salvo le y di train corrispondenti alle x di train
        y_test = target.drop(X_train.index) # Mi salvo le y di test corrispondenti alle x di test

        return X_train, y_train, X_test, y_test


    '''   
    Il processo di valutazione holdout consiste in:
    1. Dividire i dati: i dati vengono divisi casualmente (viene specificata la percentuale in input) in dati di training e dati di test
    2. Addestramento del modello: il modello quindi si addestra fornendo "in pasto" i dati X_train e y_train
    3. Test del modello: il modello viene quindi testato con i dati di test (X_test)
    4. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (y_test). Le prestazione del modello vengono calcolate tramite diverse metriche.
    5. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    def holdout_validation(self):
        X_train, y_train, X_test, y_test = self.data_splitting(self.features, self.target, self.training_perc) # richiamo il metodo che va a splittare i dati in dati di train e dati di test

        knnModel = KNNAlgorithm(self.k, X_train, y_train) # Alleno il modello fornendogli i dati di training
        prediction = knnModel.model_prediction(X_test) # Effettuo la predizione con il modello allenato precedentemente

        Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = self.metrics_calculation(y_test, prediction) # richiamo il metodo che va a calcolare le metriche, passandogli i dati di test e le predizioni
        self.save_metrics(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean) # richiamo il metodo che va a salvare nel file Metriche.txt le metriche appena calcolate

    ''' 
    Il processo di valutazione random subsampling consiste in:
    1. Specificare in input il numero di esperimenti (K) da effettuare
    2. Specificare in input la percentuale per i dati di train e test
    3. Addestramento del modello: il modello viene addestrato quindi utilizzando X_train e y_train
    4. Valutazione delle performance: il modello appena addestrato viene quindi valutato utilizzando i dati di test (y_test). Le prestazione del modello vengono calcolate tramite diverse metriche
    5. Iterazioni multiple: il processo viene ripetuto piu volte (K volte), con nuove suddivisioni casuali del dataset, per ottenere una stima più robusta della performance del modello. Infine le valutazioni multiple vengono aggregate per ottenere una misura comune delle prestazioni del modello.
    6. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti

    Parameters
    ----------
    K : int
        numero di esperimenti da effettuare

    Returns
    -------
    None
    '''
    def random_subsampling_validation(self, K:int):
        # Inizializzo le liste che conteranno i valori delle metriche calcolate per ogni iterazione
        Accuracy_rate_scores = []
        Error_rate_scores = []
        Sensitivity_scores = []
        Specificity_scores = []
        Geometric_mean_scores = []

        # Come previsto dal processo di valutazione random subsampling, questo viene ripetuto K volte
        for _ in range(K):
            X_train, y_train, X_test, y_test = self.data_splitting(self.features, self.target, self.training_perc) # richiamo il metodo che va a splittare i dati in dati di train e dati di test

            knnModel = KNNAlgorithm(self.k, X_train, y_train) # Alleno il modello fornendogli i dati di training
            prediction = knnModel.model_prediction(X_test) # Effettuo la predizione con il modello allenato precedentemente

            Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = self.metrics_calculation(y_test, prediction) # richiamo il metodo che va a calcolare le metriche, passandogli i dati di test e le predizioni
            
            # Aggiungo i valori delle metriche calcolate, per questo esperimento, nelle liste
            Accuracy_rate_scores.append(Accuracy_rate)
            Error_rate_scores.append(Error_rate)
            Sensitivity_scores.append(Sensitivity)
            Specificity_scores.append(Specificity)
            Geometric_mean_scores.append(Geometric_mean)

        # Calcolo i valori medi per ogni metrica calcolata nei K esperimetni
        Accuracy_rate_mean = np.mean(Accuracy_rate_scores)
        Error_rate_mean = np.mean(Error_rate_scores)
        Sensitivity_mean = np.mean(Sensitivity_scores)
        Specificity_mean = np.mean(Specificity_scores)
        Geometric_mean_mean = np.mean(Geometric_mean_scores)

        self.save_metrics(Accuracy_rate_mean, Error_rate_mean, Sensitivity_mean, Specificity_mean, Geometric_mean_mean) # richiamo il metodo che va a salvare le metriche calcolate, nel file Metriche.txt
        self.metrics_plot(Accuracy_rate_scores, Error_rate_scores, Sensitivity_scores, Specificity_scores, Geometric_mean_scores) # richiamo il metodo che va a plottare le metriche calcolate


    '''
    In questo metodo vengono calcolate prima i valori della confusion matrix, per poi calcolare le metriche richieste.

    Parameters
    ----------
    y_test : pandas.Series
        dati che verranno utilizzati per testare il modello
    prediction : list
        predizioni effettuate dal modello

    Returns
    -------
    Accuracy_rate : float
        percentuale di predizioni corrette rispetto al totale delle predizioni
    Error_rate : float
        percentuale di predizioni errate rispetto al totale delle predizioni
    Sensitivity : float
        capacità del modello di predirre correttamente i valori positivi
    Specificity : float
        capacità del modello di predirre correttamente i valori negativi
    Geometric_mean : float
        media che bilancia valori positivi e negativi
    '''
    def metrics_calculation(self, y_test:pd.Series, prediction:list):

        # Inizializzo le variabili che conterranno i valori delle metriche calcolate
        Accuracy_rate = 0
        Error_rate = 0
        Sensitivity = 0
        Specificity = 0
        Geometric_mean = 0

        # Calcolo della confusion matrix
        True_Negative = sum(1 for y, pred in zip(y_test.values, prediction) if (y == pred and pred == 2.0))
        True_Positive = sum(1 for y, pred in zip(y_test.values, prediction) if (y == pred and pred == 4.0))
        False_Positive = sum(1 for y, pred in zip(y_test.values, prediction) if (y != pred and pred == 4.0))
        False_Negative = sum(1 for y, pred in zip(y_test.values, prediction) if (y != pred and pred == 2.0))
        

        # Calcolo effettivo delle metriche richieste mediante i valori della confusion matrix, precedentemente calcolati
        if 1 in self.chosen_metrics:
            Accuracy_rate = (True_Negative + True_Positive) / y_test.size # Percentuale di predizioni corrette rispetto al totale delle predizioni
        if 2 in self.chosen_metrics:
            Error_rate = (False_Positive + False_Negative) / y_test.size # Percentuale di predizioni errate rispetto al totale delle predizioni
        if 3 in self.chosen_metrics and (True_Positive + False_Negative) != 0:
            Sensitivity = (True_Positive) / (True_Positive + False_Negative) # Capacità del modello di predirre correttamente i valori positivi
        if 4 in self.chosen_metrics and (True_Negative + False_Positive) != 0:
            Specificity = (True_Negative) / (True_Negative + False_Positive) # Capacità del modello di predirre correttamente i valori negativi
        if 5 in self.chosen_metrics:
            Geometric_mean = np.sqrt((Sensitivity*Specificity)) # Media che bilancia valori positivi e negativi

        return Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean


    '''
    In questo metodo vengono salvate le metriche calcolate in un file txt.
    Il nome del file sarà: "Metriche.txt"

    Parameters
    ----------
    Accuracy_rate : float
        percentuale di predizioni corrette rispetto al totale delle predizioni
    Error_rate : float
        percentuale di predizioni errate rispetto al totale delle predizioni
    Sensitivity : float
        capacità del modello di predirre correttamente i valori positivi
    Specificity : float
        capacità del modello di predirre correttamente i valori negativi
    Geometric_mean : float
        media che bilancia valori positivi e negativi

    Returns
    -------
    None
    '''
    def save_metrics(self, Accuracy_rate:float, Error_rate:float, Sensitivity:float, Specificity:float, Geometric_mean:float):
        # Con le seguenti operazioni apro il file Metriche.txt e ci scrivo dentro le metriche calcolate
        with open('Metriche.txt', 'w') as file:
            file.write('Accuracy Rate: ' + str(Accuracy_rate) + '\n')
            file.write('Error Rate: ' + str(Error_rate) + '\n')
            file.write('Sensitivity: ' + str(Sensitivity) + '\n')
            file.write('Specificity: ' + str(Specificity) + '\n')
            file.write('Geometric Mean: ' + str(Geometric_mean) + '\n')
        file.close() # Chiudo il file Metriche.txt


    '''
    In questo metodo vengono plottate le metriche per ogni esperimento e vengono rappresentate le metriche con un boxplot.
    La rappresentazione avviene tramite la libreria matplotlib.

    Parameters
    ----------
    Accuracy_rate : list
        lista che contiene i valori della metrica Accuracy Rate
    Error_rate : list
        lista che contiene i valori della metrica Error Rate
    Sensitivity : list
        lista che contiene i valori della metrica Sensitivity
    Specificity : list
        lista che contiene i valori della metrica Specificity
    Geometric_mean : list
        lista che contiene i valori della metrica Geometric Mean

    Returns
    -------
    None
    '''
    def metrics_plot(self, Accuracy_rate:list, Error_rate:list, Sensitivity:list, Specificity:list, Geometric_mean:list):
        etichette = ['Accuracy Rate', 'Error Rate', 'Sensitivity', 'Specificity', 'Geometric Mean'] # Vettore utilizzato per rappresentare le etichette del grafico
        valori = [Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean] # Vettore utilizzato per rappresentare i valori del grafico corrispondenti alle etichette

        plt.figure(figsize=(10, 5)) # Imposto la dimensione del grafico

        # Con le seguenti operazioni plotto le metriche richieste
        if 1 in self.chosen_metrics:
            plt.plot(Accuracy_rate, marker='o', linestyle='solid', linewidth=2, markersize=5, color='blue', label='Accuracy Rate')
        if 2 in self.chosen_metrics:
            plt.plot(Error_rate, marker='o', linestyle='solid', linewidth=2, markersize=5, color='green', label='Error Rate')
        if 3 in self.chosen_metrics:
            plt.plot(Sensitivity, marker='o', linestyle='solid', linewidth=2, markersize=5, color='red', label='Sensitivity')
        if 4 in self.chosen_metrics:
            plt.plot(Specificity, marker='o', linestyle='solid', linewidth=2, markersize=5, color='yellow', label='Specificity')
        if 5 in self.chosen_metrics:
            plt.plot(Geometric_mean, marker='o', linestyle='solid', linewidth=2, markersize=5, color='orange', label='Geometric Mean')

        
        plt.legend(loc='upper right') # Imposto la posizione legenda nel grafico
        plt.xlabel("Esperimenti") # Imposto il nome dell'etichetta dell'asse x
        plt.ylabel("Valori") # Imposto il nome dell'etichetta dell'asse y
        plt.title("Andamento delle metriche") # Imposto il titolo del grafico
        plt.tight_layout() # Ottimizza la disposizione dei sottopannelli nel grafico per evitare sovrapposizioni
        #plt.show() # Mostro il grafico


        # Creo una nuova figura per rappresentare il boxplot delle metriche
        plt.figure(figsize=(10, 5))
        plt.boxplot(valori)
        
        plt.xlabel("Metriche") # Imposto il nome dell'etichetta dell'asse x
        plt.ylabel("Valori") # Imposto il nome dell'etichetta dell'asse y
        plt.title("Boxplot delle metriche") # Imposto il titolo del grafico
        plt.xticks(range(1, len(etichette) + 1) ,etichette, rotation=45) # Imposto le etichette dell'asse x e la rotazione di queste
        plt.tight_layout() # Ottimizza la disposizione dei sottopannelli nel grafico per evitare sovrapposizioni

        plt.show() # Mostro il grafico