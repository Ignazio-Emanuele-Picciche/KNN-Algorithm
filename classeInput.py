# __import__(class evaluation)

# k = int(input("Inserire il numero di vicini k da utilizzare per il classificatore: ")) #numero di vicini da utilizzare per il classificatore
    #K = int(input("Inserire il numero di esperimenti K: ")) #numero di esperimenti
    #training = int(input("Inserire la percentuale di training: ")) #percentuale di training (la percentuale di test sarà ricavata automaticamente dal programma)
    #test = 100 - training #percentuale di test (ricavata dal programma per sottrazione
    #print(f"La percentuale di test è {test}")

class Input:
    def __init__(self):
        self.k=int(input("Inserire il numero di vicini k da utilizzare per il classificatore: "))
        self.training=int(input("Inserire la percentuale di training: "))
        self.test=100-self.training


    #def scelta_metodo_evaluation(self):#l'utente sceglie se utilizzare l'holdout o il random subsampling
     #   scelta_effettuata=0
      #  while scelta_effettuata !=1 or scelta_effettuata !=2:
       #     scelta_evaluation = int(input("inserire 1 per scegliere l'holdout, 2 per il random subsampling"))

#prova
#input1=Input()
#print(input1.k,input1.training,input1.test)

