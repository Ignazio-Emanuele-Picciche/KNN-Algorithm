#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the necessary classes
# Preprocessing for data cleaning and standardization
# Input for user input handling
# Evaluation for model performance evaluation
from Preprocessing import Preprocessing
from Input import Input
from Evaluation import Evaluation

if __name__ == '__main__ ':
    # Create instances of the Input and Preprocessing classes
    input_utente = Input()
    preprocessing = Preprocessing()



    # Ask the user for the evaluation method and metrics to use
    metodo_di_valutazione= input_utente.scelta_metodo_evaluation()
    metriche_scelte = input_utente.scelta_metriche()
    K = input_utente.K

    # Load, clean, and standardize the dataset
    preprocessing.caricamento_dataset()
    preprocessing.pulizia_dati()
    preprocessing.standardizzazione()
    
    # Split the dataset into features and target label
    features, target = preprocessing.suddivisione_dati()

    # Ask the user for the percentage of data to use for training and the number of neighbors to consider
    perc_train = input_utente.scelta_training()
    k = input_utente.scelta_k()

    #  Create an instance of the Evaluation class to evaluate the model's performance
    evaluation = Evaluation(features, target, perc_train, k, metriche_scelte)

    if metodo_di_valutazione == 1:
        evaluation.valutazione_holdout()
    else:
        evaluation.valutazione_random_subsampling(K)
