#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Preprocessing import Preprocessing
from Input import Input
from Evaluation import Evaluation

if __name__ == '__main__':
    input = Input()
    preprocessing = Preprocessing()
    metodo_di_valutazione, K = input.scelta_metodo_evaluation()

    preprocessing.caricamento_dataset()
    preprocessing.pulizia_dati()
    features, target = preprocessing.suddivisione_dati()
    perc_train = input.training
    k = input.k

    evaluation = Evaluation(features, target, perc_train, k)
    if metodo_di_valutazione == 1:
        evaluation.valutazione_holdout()
    else:
        evaluation.valutazione_random_subsampling(K)
