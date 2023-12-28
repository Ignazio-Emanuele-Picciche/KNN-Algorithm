# __import__(class evaluation)

class input():
   # k = int(input("Inserire il numero di vicini k da utilizzare per il classificatore: ")) #numero di vicini da utilizzare per il classificatore
    #K = int(input("Inserire il numero di esperimenti K: ")) #numero di esperimenti
    #training = int(input("Inserire la percentuale di training: ")) #percentuale di training (la percentuale di test sarà ricavata automaticamente dal programma)
    #test = 100 - training #percentuale di test (ricavata dal programma per sottrazione
    #print(f"La percentuale di test è {test}")

    def percentuali_di_splitting(self):
        this.training = int(input("Inserire la percentuale di training: ")) #percentuale di training (la percentuale di test sarà ricavata automaticamente dal programma)
        this.test = 100 - training #percentuale di test (ricavata dal programma per sottrazione
        print(f"La percentuale di test è {test}")
        return training,test

    def scelta_vicini_k(self):
        this.k = int(input("Inserire il numero di vicini k da utilizzare per il classificatore: ")) #numero di vicini da utilizzare per il classificatore
        return k

    def scelta_metodo_evaluation(self):#l'utente sceglie se utilizzare l'holdout o il random subsampling
        scelta_effettuata=0
        while scelta_effettuata !=1 or scelta_effettuata !=2:
            this.scelta_evaluation = int(input("inserire 1 per scegliere l'holdout, 2 per il random subsampling"))





