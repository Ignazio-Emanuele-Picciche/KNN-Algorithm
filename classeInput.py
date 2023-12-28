class input():
    k = int(input("Inserire il numero di vicini k da utilizzare per il classificatore: ")) #numero di vicini da utilizzare per il classificatore
    K = int(input("Inserire il numero di esperimenti K: ")) #numero di esperimenti
    training = int(input("Inserire la percentuale di training: ")) #percentuale di training (la percentuale di test sarà ricavata automaticamente dal programma)
    test = 100 - training #percentuale di test (ricavata dal programma per sottrazione
    print(f"La percentuale di test è {test}")

