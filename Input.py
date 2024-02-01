#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class Input:
    def __init__(self):
        self.k=0 #numero di vicini da utilizzare per il classificatore
        self.training=1
        self.K=0 #numero di esperimenti K per il random subsampling

    def dataset_path(self): #the user enters the path of the dataset
        path = input("Enter the path of the dataset: ")
        return path
    def scelta_k(self): #l'utente sceglie il numero di vicini k da utilizzare per il classificatore
                        #il programma non va avanti finchè l'utente non inserisce un numero intero maggiore di 0
        while True:
            k = input("Enter the number of neighbors k to use for the classifier: ")
            if k.isdigit() and int(k) > 0:
                self.k = int(k)
                break
        return self.k


    def scelta_training(self): #l'utente sceglie la percentuale di training, il valore inserito deve essere un numero compreso tra 0 e 100, se non è così il programma non va avanti

        while True:
            training = input("Enter the percentage for the training: ")
            if training.isdigit() and 0 < int(training) < 100:
                self.training = int(training)
                break
        return self.training
    def scelta_metodo_evaluation(self):#l'utente sceglie se utilizzare l'holdout o il random subsampling
        scelta_evaluation=0

        while scelta_evaluation !="1" or scelta_evaluation !="2":

            scelta_evaluation = (input("Enter 1 to choose holdout, 2 to choose random subsampling: ")) #l'utente deve inserire 1 o 2, 1 per l'holdout, 2 per il random subsampling, il programma non va avanti finchè l'utente non sceglie

            if scelta_evaluation=="1":

                return int(scelta_evaluation)

            elif scelta_evaluation=="2":
                while True: #se è stata fatta la scelta 2, l'utente deve inserire il numero di esperimenti K
                    #il programma non va avanti finchè l'utente non inserisce un numero intero maggiore di 0
                    K = input("Enter the number of experiments K for the random subsampling: ")
                    if K.isdigit() and int(K) > 0:
                        self.K = int(K)
                        break

                return int(scelta_evaluation)


    def scelta_metriche(self): #l'utente sceglie le metriche da utilizzare per la valutazione,
        # le metriche sono: Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean.
        # All'inizio all'utente viene chiesto se vuole utilizzare tutte le metriche (inserendo 1), se risponde di no (inserendo 0), può scegliere quali metriche utilizzare
        # viene chiesto all'utente di inserire 1 per scegliere una metrica, 0 per non sceglierla, e successivamente viene chiesta la stessa cosa per ogni metrica successiva
        # il programma non va avanti finchè l'utente non sceglie
        # le metriche scelte vengono salvate in una lista, che viene restituita dal metodo
        metriche_scelte = []
        scelta_metriche = 0
        while scelta_metriche != "1" or scelta_metriche != "0":
            scelta_metriche = (input("Enter 1 to select all metrics, 0 to manually select metrics: "))
            if scelta_metriche == "1":
                metriche_scelte = [1, 2, 3, 4, 5]
                return metriche_scelte
            elif scelta_metriche == "0":
                scelta_metriche_accuracy_rate = 0
                while scelta_metriche_accuracy_rate != "1" or scelta_metriche_accuracy_rate != "0":
                    scelta_metriche_accuracy_rate = (input("Enter 1 to choose the Accuracy Rate metric, 0 to not choose it: "))
                    if scelta_metriche_accuracy_rate == "1":
                        metriche_scelte.append(1)
                        break
                    elif scelta_metriche_accuracy_rate == "0":
                        break
                scelta_metriche_error_rate = 0
                while scelta_metriche_error_rate != "1" or scelta_metriche_error_rate != "0":
                    scelta_metriche_error_rate = (input("Enter 1 to choose the Error Rate metric, 0 to not choose it: "))
                    if scelta_metriche_error_rate == "1":
                        metriche_scelte.append(2)
                        break
                    elif scelta_metriche_error_rate == "0":
                        break
                scelta_metriche_sensitivity = 0
                while scelta_metriche_sensitivity != "1" or scelta_metriche_sensitivity != "0":
                    scelta_metriche_sensitivity = (input("Enter 1 to choose the Sensitivity metric, 0 to not choose it: "))
                    if scelta_metriche_sensitivity == "1":
                        metriche_scelte.append(3)
                        break
                    elif scelta_metriche_sensitivity == "0":
                        break
                scelta_metriche_specificity = 0
                while scelta_metriche_specificity != "1" or scelta_metriche_specificity != "0":
                    scelta_metriche_specificity = (input("Enter 1 to choose the Specificity metric, 0 to not choose it: "))
                    if scelta_metriche_specificity == "1":
                        metriche_scelte.append(4)
                        break
                    elif scelta_metriche_specificity == "0":
                        break
                scelta_metriche_geometric_mean = 0
                while scelta_metriche_geometric_mean != "1" or scelta_metriche_geometric_mean != "0":
                    scelta_metriche_geometric_mean = (input("Enter 1 to choose the Geometric Mean metric, 0 to not choose it: "))
                    if scelta_metriche_geometric_mean == "1":
                        metriche_scelte.append(5)
                        break
                    elif scelta_metriche_geometric_mean == "0":
                        break
                return metriche_scelte

#prova
#input1=Input()
#print(input1.dataset_path(),input1.scelta_k(),input1.scelta_training(),input1.scelta_metodo_evaluation(),input1.scelta_metriche())
