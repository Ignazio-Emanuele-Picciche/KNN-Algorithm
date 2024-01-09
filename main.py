#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Preprocessing import Preprocessing
from Input import Input
from Evaluation import Evaluation

if __name__ == '__main__':
    input_utente = Input()
    preprocessing = Preprocessing()

    metodo_di_valutazione= input_utente.scelta_metodo_evaluation()
    metriche_scelte = input_utente.scelta_metriche()
    K= input_utente.K

    preprocessing.caricamento_dataset()
    preprocessing.pulizia_dati()
    preprocessing.standardizzazione()
    features, target = preprocessing.suddivisione_dati()

    perc_train = input_utente.training
    k = input_utente.k

    evaluation = Evaluation(features, target, perc_train, k, metriche_scelte)

    if metodo_di_valutazione == 1:
        evaluation.valutazione_holdout()
    else:
        evaluation.valutazione_random_subsampling(K)
