#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importazione delle classi necessarie
from Preprocessing import Preprocessing
from Input import Input
from Evaluation import Evaluation

if __name__ == '__main__ ':
    input_utente = Input() # Istanziata la classe Input, acquisizione dati di input dall'utente
    preprocessing = Preprocessing() # Istanziata la classe Preprocessing
    metodo_di_valutazione, K = input_utente.scelta_metodo_evaluation() #Chiamata al metodo scelta_metodo_evaluation della classe Input, scelta del metodo di valutazione e del valore di K

    preprocessing.caricamento_dataset() #Chiamata al metodo caricamento_dataset della classe Preprocessing, caricamento del dataset
    preprocessing.pulizia_dati() #Chiamata al metodo pulizia_dati della classe Preprocessing, pulizia del dataset
    features, target = preprocessing.suddivisione_dati() #Chiamata al metodo suddivisione_dati della classe Preprocessing, suddivisione del dataset in features e target label
    perc_train = input_utente.training #Percentuale di dati da utilizzare per l'addestramento del modello
    k = input_utente.k # Acquisizione del valore di k dall'utente

    evaluation = Evaluation(features, target, perc_train, k) # Istanziata la classe Evaluation, passaggio dei parametri features, target label, percentuale di dati da utilizzare per l'addestramento del modello e valore di k
    if metodo_di_valutazione == 1: #Se il metodo di valutazione scelto dall'utente è holdout
        evaluation.valutazione_holdout() #Chiamata al metodo valutazione_holdout della classe Evaluation
    else:  #Se il metodo di valutazione scelto dall'utente è random subsampling
        evaluation.valutazione_random_subsampling(K) #Chiamata al metodo valutazione_random_subsampling della classe Evaluation
    # Creazione delle istanze delle classi Input e Preprocessing
    input_utente = Input()
    preprocessing = Preprocessing()

    # Richiesta all'utente del metodo di valutazione e delle metriche da utilizzare
    metodo_di_valutazione= input_utente.scelta_metodo_evaluation()
    metriche_scelte = input_utente.scelta_metriche()
    K = input_utente.K

    # Caricamento, pulizia e standardizzazione del dataset
    preprocessing.caricamento_dataset()
    preprocessing.pulizia_dati()
    preprocessing.standardizzazione()
    
    # Suddivisione del dataset in features e target
    features, target = preprocessing.suddivisione_dati()

    # Richiesta all'utente della percentuale di dati da utilizzare per l'addestramento e del numero di vicini da considerare
    perc_train = input_utente.training
    k = input_utente.k

    # Creazione dell'istanza della classe Evaluation per valutare le prestazioni del modello
    evaluation = Evaluation(features, target, perc_train, k, metriche_scelte)

    if metodo_di_valutazione == 1:
        evaluation.valutazione_holdout()
    else:
        evaluation.valutazione_random_subsampling(K)
