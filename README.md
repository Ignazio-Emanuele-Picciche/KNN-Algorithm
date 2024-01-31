# KNN Algorithm - Progetto di Programmazione e metodi sperimentali per l'Intelligenza Artificiale (AA 23/24)


## General description of the project

This project, made by Alessia Rossi, Ignazio Emanuele Piccichè and Riccardo Polacchi, 
has the purpose to develop a program which takes a dataset with information and characteristics of some tumoral cells
and, after the processing of the data and the training of the model, predicts the type of the tumoral cell (if benign or malignant).
The final objective of the program is to test the performance of the machine learning model and to give and evaluation 
of the results, with plots and metrics.
The model uses the KNN algorithm, and for the evaluation it uses the holdout or the random subsampling method (the choice
is made by the user). 
It is structured with a pipeline of different classes, which are Input class, Preprocessing class, KNN class and Evaluation class,
all of them utilized in the main of the program.
The user can decide the value of the inputs and the type of evaluation and metrics (for further information read the section 
with the instructions for the user).
The dataset utilized is taken from http://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original,
it is a .csv file wich contains the following data for every single cell:

- A sample code number 

- 9 types of features, wich one with a value from 1 to 10, which are "clump thickness", "uniformity of cell size",
 "uniformity of cell shape", "marginal adhesion", "single epithelial cel size", "bare nuclei", "bland chromatin",
 "normal nucleoli", "mitoses".

- The class label, wich value is 2 if there is a benign tumor, and 4 it there is a malignant tumor

In the following parts there are the descriptions of the classes and then instructions for the user 
to correctly use the program.




### Descrizione delle classi implementate
TODO...

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




