class KNNAlgorithm:

    def __init__(self,k):
        pass

    def allenamento_dati(self,x_train,y_train): # aquisizione dei dati postprocessati
        # x_train rappresenta la matice delle features (B a J)
        # y_train rappresenta le y (K)
        pass

    def predizione_modello(self,x_test):
        #x_test rappresenta la matrice delle features che sono test
        # Classificazione in due gruppi (benigno, maligno)
        ''' confrontare ogni x_test con ogni x_train --> due cicli for
        in questo mi clacolo la distanza euclidea quindi richiamo il metodo della
         distanza euclidea
         per ciascun x_test mi conservo anche la y_test associata , oltre che la distanza
        '''
        # ordino in modo crescente le distanze (con associate y_test)
        # prendo le prime k distanze
        # analizzo (conto) le y_test e prendo la y_test più numerosa
        # OSS: nel caso sono di numero uguali ne prendo una a le due a caso

        # return: sarebbe il y_test trovata

    def calcolo_distanza_euclidea(self):
        #return: distanza euclidea tra vettore x_test e x_train

        pass




