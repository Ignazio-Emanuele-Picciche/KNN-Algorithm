#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __import__(class evaluation)

# k = int(input("Inserire il numero di vicini k da utilizzare per il classificatore: ")) #numero di vicini da utilizzare per il classificatore
    #K = int(input("Inserire il numero di esperimenti K: ")) #numero di esperimenti
    #training = int(input("Inserire la percentuale di training: ")) #percentuale di training (la percentuale di test sarà ricavata automaticamente dal programma)
    #test = 100 - training #percentuale di test (ricavata dal programma per sottrazione
    #print(f"La percentuale di test è {test}")

class Input:
    def __init__(self):
        self.k=int(input("Inserire il numero di vicini k da utilizzare per il classificatore: ")) #numero di vicini k da utilizzare per il classificatore
        self.training=int(input("Inserire la percentuale di training: ")) #percentuale di training (la percentuale di test sarà ricavata automaticamente dal programma)
        self.test=100-self.training #percentuale di test (ricavata dal programma per sottrazione)
        self.K=0 #numero di esperimenti K per il random subsampling


    def scelta_metodo_evaluation(self):#l'utente sceglie se utilizzare l'holdout o il random subsampling
        scelta_evaluation=0

        while scelta_evaluation !="1" or scelta_evaluation !="2":

            scelta_evaluation = (input("Inserire 1 per scegliere l'holdout, 2 per il random subsampling: ")) #l'utente deve inserire 1 o 2, 1 per l'holdout, 2 per il random subsampling, il programma non va avanti finchè l'utente non sceglie

            if scelta_evaluation=="1":

                return int(scelta_evaluation)

            elif scelta_evaluation=="2":

                self.K = int(input("Inserire il numero di esperimenti K: ")) #se ha effettuato questa scelta, l'utente deve inserire il numero di esperimenti K per il random subsampling

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
            scelta_metriche = (input("Inserire 1 per scegliere tutte le metriche, 0 per scegliere manualmente le metriche: "))
            if scelta_metriche == "1":
                metriche_scelte = [1, 2, 3, 4, 5]
                return metriche_scelte
            elif scelta_metriche == "0":
                scelta_metriche_accuracy_rate = 0
                while scelta_metriche_accuracy_rate != "1" or scelta_metriche_accuracy_rate != "0":
                    scelta_metriche_accuracy_rate = (input("Inserire 1 per scegliere la metrica Accuracy Rate, 0 per non sceglierla: "))
                    if scelta_metriche_accuracy_rate == "1":
                        metriche_scelte.append(1)
                        break
                    elif scelta_metriche_accuracy_rate == "0":
                        break
                scelta_metriche_error_rate = 0
                while scelta_metriche_error_rate != "1" or scelta_metriche_error_rate != "0":
                    scelta_metriche_error_rate = (input("Inserire 1 per scegliere la metrica Error Rate, 0 per non sceglierla: "))
                    if scelta_metriche_error_rate == "1":
                        metriche_scelte.append(2)
                        break
                    elif scelta_metriche_error_rate == "0":
                        break
                scelta_metriche_sensitivity = 0
                while scelta_metriche_sensitivity != "1" or scelta_metriche_sensitivity != "0":
                    scelta_metriche_sensitivity = (input("Inserire 1 per scegliere la metrica Sensitivity, 0 per non sceglierla: "))
                    if scelta_metriche_sensitivity == "1":
                        metriche_scelte.append(3)
                        break
                    elif scelta_metriche_sensitivity == "0":
                        break
                scelta_metriche_specificity = 0
                while scelta_metriche_specificity != "1" or scelta_metriche_specificity != "0":
                    scelta_metriche_specificity = (input("Inserire 1 per scegliere la metrica Specificity, 0 per non sceglierla: "))
                    if scelta_metriche_specificity == "1":
                        metriche_scelte.append(4)
                        break
                    elif scelta_metriche_specificity == "0":
                        break
                scelta_metriche_geometric_mean = 0
                while scelta_metriche_geometric_mean != "1" or scelta_metriche_geometric_mean != "0":
                    scelta_metriche_geometric_mean = (input("Inserire 1 per scegliere la metrica Geometric Mean, 0 per non sceglierla: "))
                    if scelta_metriche_geometric_mean == "1":
                        metriche_scelte.append(5)
                        break
                    elif scelta_metriche_geometric_mean == "0":
                        break
                return metriche_scelte

#prova
#input1=Input()
#print(input1.k,input1.training,input1.test,input1.scelta_metodo_evaluation(),input1.scelta_metriche())

