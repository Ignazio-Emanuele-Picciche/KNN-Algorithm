#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
- Definition of the methods of the Input class:
    - constructor
    - loading_dataset -> Loads the dataset from the csv file
    - data_cleaning -> Manages missing values
    - standardization -> Performs feature scaling
    - data_split -> Splits the dataset into features (x) and target label (y)
'''


class Input:
    def __init__(self):
        self.k=0 # numero di vicini da utilizzare per il classificatore
        self.training=1
        self.K=0 #numero di esperimenti K per il random subsampling


    def k_neighbors(self): #l'utente sceglie il numero di vicini k da utilizzare per il classificatore
                        #il programma non va avanti finchè l'utente non inserisce un numero intero maggiore di 0
        while True:
            k = input("Enter the number of neighbors k to use for the classifier: ")
            if k.isdigit() and int(k) > 0:
                self.k = int(k)
                break
        return self.k


    def training_percentage(self): #l'utente sceglie la percentuale di training, il valore inserito deve essere un numero compreso tra 0 e 100, se non è così il programma non va avanti

        while True:
            training = input("Enter the percentage for the training: ")
            if training.isdigit() and 0 < int(training) < 100:
                self.training = int(training)
                break
        return self.training
    def evaluation_method(self):#l'utente sceglie se utilizzare l'holdout o il random subsampling
        evaluation=0

        while evaluation !="1" or evaluation !="2":

            evaluation = (input("Enter 1 to choose holdout, 2 to choose random subsampling: ")) #l'utente deve inserire 1 o 2, 1 per l'holdout, 2 per il random subsampling, il programma non va avanti finchè l'utente non sceglie

            if evaluation=="1":

                return int(evaluation)

            elif evaluation=="2":
                while True: #se è stata fatta la scelta 2, l'utente deve inserire il numero di esperimenti K
                    #il programma non va avanti finchè l'utente non inserisce un numero intero maggiore di 0
                    K = input("Enter the number of experiments K for the random subsampling: ")
                    if K.isdigit() and int(K) > 0:
                        self.K = int(K)
                        break

                return int(evaluation)


    def metrics_selection(self): #l'utente sceglie le metriche da utilizzare per la valutazione,
        # le metriche sono: Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean.
        # All'inizio all'utente viene chiesto se vuole utilizzare tutte le metriche (inserendo 1), se risponde di no (inserendo 0), può scegliere quali metriche utilizzare
        # viene chiesto all'utente di inserire 1 per scegliere una metrica, 0 per non sceglierla, e successivamente viene chiesta la stessa cosa per ogni metrica successiva
        # il programma non va avanti finchè l'utente non sceglie
        # le metriche scelte vengono salvate in una lista, che viene restituita dal metodo
        metrics = []
        metrics_selection = 0
        while metrics_selection != "1" or metrics_selection != "0":
            metrics_selection = (input("Enter 1 to select all metrics, 0 to manually select metrics: "))
            if metrics_selection == "1":
                metrics = [1, 2, 3, 4, 5]
                return metrics
            elif metrics_selection == "0":
                accuracy_rate = 0
                while accuracy_rate != "1" or accuracy_rate != "0":
                    accuracy_rate = (input("Enter 1 to choose the Accuracy Rate metric, 0 to not choose it: "))
                    if accuracy_rate == "1":
                        metrics.append(1)
                        break
                    elif accuracy_rate == "0":
                        break
                error_rate = 0
                while error_rate != "1" or error_rate != "0":
                    error_rate = (input("Enter 1 to choose the Error Rate metric, 0 to not choose it: "))
                    if error_rate == "1":
                        metrics.append(2)
                        break
                    elif error_rate == "0":
                        break
                sensitivity = 0
                while sensitivity != "1" or sensitivity != "0":
                    sensitivity = (input("Enter 1 to choose the Sensitivity metric, 0 to not choose it: "))
                    if sensitivity == "1":
                        metrics.append(3)
                        break
                    elif sensitivity == "0":
                        break
                specificity = 0
                while specificity != "1" or specificity != "0":
                    specificity = (input("Enter 1 to choose the Specificity metric, 0 to not choose it: "))
                    if specificity == "1":
                        metrics.append(4)
                        break
                    elif specificity == "0":
                        break
                geometric_mean = 0
                while geometric_mean != "1" or geometric_mean != "0":
                    geometric_mean = (input("Enter 1 to choose the Geometric Mean metric, 0 to not choose it: "))
                    if geometric_mean == "1":
                        metrics.append(5)
                        break
                    elif geometric_mean == "0":
                        break
                return metrics

#prova
#input1=Input()
#print(input1.k_neighbors(),input1.training_percentage(),input1.evaluation_method(),input1.metrics_selection())
