# KNN Algorithm - Progetto di Programmazione e metodi sperimentali per l'Intelligenza Artificiale (AA 23/24)

## Descrizione del progetto
TODO...

###  Algoritmo K-Nearest Neighbors 
*L'algoritmo K-nearest neighbor (KNN)* è una tecnica di classificazione che opera valutando le caratteristiche degli oggetti vicini a quello in esame. In pratica, KNN classifica un oggetto basandosi sulla sua somiglianza con altri oggetti noti nel dataset. Questo avviene calcolando la distanza tra le caratteristiche dell'oggetto da classificare e quelle degli oggetti già presenti nel sistema. Utilizzando i "k" oggetti più vicini, l'algoritmo determina la classe dell'oggetto in esame.

Per individuare i vicini più prossimi di un punto di query, KNN calcola la distanza tra il punto di interrogazione e gli altri punti dati nel dataset. Tra le varie misure di distanza disponibili, la distanza euclidea (p=2) è spesso la scelta più comune, in quanto calcola una linea retta tra il punto di query e gli altri punti.

*Il parametro "k"* nell'algoritmo KNN specifica il numero di vicini da considerare per la classificazione di un dato punto. Se, ad esempio, k=1, l'oggetto verrà assegnato alla stessa classe del suo vicino più vicino. Tuttavia, la scelta di "k" è cruciale e può influenzare le prestazioni del modello. Valori bassi di "k" possono portare a un'elevata variabilità ma una bassa distorsione, mentre valori elevati possono causare una distorsione elevata e una variabilità inferiore. La scelta di "k" dipende dal tipo di dati e dal livello di rumore nel dataset.

## Descrizione delle classi implementate
### **Classe: KNNAlgorithm**  Classe che implementa l'algoritmo KNN. 

Contiene i metodi per il calcolo della distanza euclidea, per la predizione della classe di un punto.

- __Costruttore__

- La classe KNNAlgorithm è inizializzata con tre parametri: k, x_train e y_train.
   - k è il numero di vicini più vicini da considerare per la classificazione.
   - x_train è il dataset di addestramento, contenente i vettori delle caratteristiche.
   - y_train è il dataset target, contenente le etichette di classe per il dataset di addestramento.


- __Metodo: predizione_modello__
- Il metodo predizione_modello prende in input un dataset di test x_test e restituisce una lista di etichette di classe previste per il dataset di test.
  - Questo metodo effettua la predizione del modello KNN sui dati di test forniti. 
  - Per ciascun punto nel dataset di test, calcola la distanza euclidea da tutti i punti nel dataset di addestramento.
  - Ordina queste distanze in ordine crescente e seleziona le k distanze più piccole.
  - Poi guarda le etichette di classe di questi k vicini più vicini.
  - L'etichetta di classe prevista per il punto di test è l'etichetta di classe più comune tra questi k vicini più vicini.
  - In caso di parità, seleziona casualmente una delle etichette di classe più comuni.
  - Ripete questo processo per tutti i punti nel dataset di test e restituisce una lista di etichette di classe previste.


- __Metodo: calcolo_distanza_euclidea__
- Il metodo calcolo_distanza_euclidea calcola la distanza euclidea tra due punti.


- __Utilizzo della classe KNNAlgorithm__
  - Per utilizzare la classe KNNAlgorithm, è necessario disporre di un dataset di addestramento e un dataset di test.
  - Creare un'istanza della classe e passare i parametri k, x_train e y_train al costruttore.
   ```python
    knn = KNNAlgorithm(k, x_train, y_train)
    ```
  -  Successivamente, è possibile chiamare il metodo predizione_modello con il dataset di test per ottenere le etichette di classe previste.
   ```python
    y_pred = knn.predizione_modello(x_test)
    ```


## Come eseguire il codice e cosa viene richiesto in input
Prima di eseguire il codice ci sono delle accortezze da fare a priori.
- Creare il proprio virtual environment da terminale, scrivendo il comando:
  - python -m venv venv
- Se si desidera lavorare da terminale, bisogna attivare il virtual environment appena creato con il comando:
	- per Windows -> .\venv\Scripts\activate 
	- per Unix o MacOS -> source ./venv/Scripts/activate 
- Per disattivare l’environment usare il comando:
	- deactivate
- Per installare l’applicazione in un nuovo contesto, dopo aver effettuato il colone del progetto e aver creato un virtual environment, usare il comando:
	- pip install -r requirements.txt
   (Questo comando serve a scaricare tutti i moduli non standard richiesti dall'applicazione)

> [!WARNING]
Aggiornare pip nel caso la versione di Python usata per generare il virtual environment non contenga una versione di pip aggiornata.
Usare il comando: pip install --upgrade pip


Ora che abbiamo sistemato il nostro ambiente virtuale, possiamo eseguire l'applicazione.
Basterà recarsi nel file main.py ed eseguirlo.

Gli input richiesti dall'applicativo sono i seguenti:
- Inserire il numero di vicini k da utilizzare per il classificatore
- Inserire la percentuale di training
- Inserire 1 per scegliere l'holdout, 2 per il random subsampling (scelta del metodo di evaluation)
- Nel caso in cui venga scelto il metodo di evaluation Random Subsampling verrà richiesto di inserire il numero di esperimenti K
- Inserire 1 per scegliere tutte le metriche, 0 per scegliere manualmente le metriche
	- Nel caso in cui venga scelto 0, verrà richiesto per ogni singola metrica se si desidera calcolarla o meno. Considerare che se viene scelta la metrica Geometric Mean vengono calcolati automaticamente anche le metriche Sensitivity e Specificity dato che fanno parte del calcolo per la metrica scelta Geometric Mean).
   	- Le metriche possibili sono: Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean


## Come visualizzare ed interpretare i risultati ottenuti
Una vola inseriti tutti gli input richiesti, ci sono due opzioni di dati visualizzati.

Nel caso in cui viene scelto il metodo di evaluation Holdout, nel file Metriche.txt verranno scritte le metriche calcolate per il signolo esperimento

Nel caso in cui venga scelto il metodo di evaluation Random Subsampling, nel file Metriche.txt verranno rappresentate le medie delle metriche calcolate nei K esperimenti (K specificato negli input).
Inoltre verranno visualizzati due grafici, uno rappresentate l'andamento delle metriche calcolate per ogni esperimento e l'altro rappresentate i boxplot per ogni metrica calcolata.

_Esempio di plot delle metriche visualizzate._
<p float="left">
  <img src="https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/e7c766c2-1239-4f0c-94de-36322a8146ae" width="500" />
  <img src="https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/e9cdad10-6c63-4794-9ddf-d577ff557070" width="500" />
</p>




