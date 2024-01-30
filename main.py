#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importazione delle classi necessarie
from Preprocessing import Preprocessing
from Input import Input
from Evaluation import Evaluation

if __name__ == '__main__ ':
    input_utente = Input()
    preprocessing = Preprocessing()
    metodo_di_valutazione, K = input_utente.scelta_metodo_evaluation()

    preprocessing.caricamento_dataset()
    preprocessing.pulizia_dati()
    features, target = preprocessing.suddivisione_dati()
    perc_train = input_utente.training
    k = input_utente.k

    evaluation = Evaluation(features, target, perc_train, k)
    if metodo_di_valutazione == 1:
        evaluation.valutazione_holdout()
    else:
        evaluation.valutazione_random_subsampling(K)
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
