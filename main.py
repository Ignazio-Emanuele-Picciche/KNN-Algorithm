#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Preprocessing import Preprocessing
from Input import Input
from Evaluation import Evaluation
from KNNAlgorithm import KNNAlgorithm

if __name__ == '__main__':
   input=Input()
   preprocessing=Preprocessing()
   metodo_di_valutazione,K=input.scelta_metodo_evaluation()

   preprocessing.caricamento_dataset()
   preprocessing.pulizia_dati()
   features,target=preprocessing.suddivisione_dati()





