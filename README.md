# KNN Algorithm - Programming and Experimental Methods for Artificial Intelligence (AA 23/24)

## General description of the project

This project, made by Alessia Rossi, Ignazio Emanuele Piccichè and Riccardo Polacchi, 
has the purpose to develop a program which takes a dataset with informations and characteristics of some tumoral cells
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

In the following parts there are the descriptions of the classes and then the instructions for the user 
to correctly use the program.

###  K-Nearest Neighbors Algorithm
*The K-nearest neighbor (KNN) algorithm* is a classification technique that operates by evaluating the characteristics of objects close to the one under examination. In practice, KNN classifies an object based on its similarity to other known objects in the dataset. This is done by calculating the distance between the features of the object to be classified and those of the objects already present in the system. By using the "k" nearest objects, the algorithm determines the class of the object under examination.

To identify the nearest neighbors of a query point, KNN calculates the distance between the query point and the other data points in the dataset. Among the various distance measures available, the Euclidean distance (p=2) is often the most common choice, as it calculates a straight line between the query point and the other points.

*The parameter "k"*  in the KNN algorithm specifies the number of neighbors to consider for classifying a given point. For example, if k=1, the object will be assigned to the same class as its nearest neighbor. However, the choice of "k" is crucial and can affect the model's performance. Low values of "k" can lead to high variability but low bias, while high values can cause high bias and lower variability. The choice of "k" depends on the type of data and the level of noise in the dataset.

## Description of Implemented Classes
### **Class: KNNAlgorithm**  A class implementing the KNN algorithm.

It contains methods for calculating Euclidean distance and predicting the class of a point.

- __Constructor__

-The KNNAlgorithm class is initialized with three parameters: k, x_train, and y_train.
   - k is the number of nearest neighbors to consider for classifying a given point.
   - x_train is the training dataset, containing feature vectors for the training dataset.
   - y_train is the training dataset, containing class labels for the training dataset.


- __Method: predizione_modello__
- The predizione_modello method takes a test dataset x_test as input and returns a list of predicted class labels for the test dataset.
  - This method predicts the KNN model on the provided test data. 
  - For each point in the test dataset, it calculates the Euclidean distance from all points in the training dataset.
  - It sorts these distances in ascending order and selects the smallest k distances. 
  - Then it looks at the class labels of these k nearest neighbors.
  - The predicted class label for the test point is the most common class label among these k nearest neighbors.
  - In case of a tie, it randomly selects one of the most common class labels.
  - This process is repeated for all points in the test dataset, and a list of predicted class labels is returned.
  

- __Method: calcolo_distanza_euclidea__
- The calcolo_distanza_euclidea method calculates the Euclidean distance between two points.


- __Using the KNNAlgorithm Class__
  - To use the KNNAlgorithm class, you need a training dataset and a test dataset.
  - Create an instance of the class and pass the parameters k, x_train, and y_train to the constructor.
   ```python
    knn = KNNAlgorithm(k, x_train, y_train)
    ```
  -  Then, you can call the model_prediction method with the test dataset to get the predicted class labels.
   ```python
    y_pred = knn.predizione_modello(x_test)
    ```
  

### **Main** 
The main function implements and evaluates the performance of a classification model using the K-Nearest Neighbors (KNN) algorithm with the holdout or random subsampling evaluation method.

- __Function: main__
  - The script begins by creating instances of the Input and Preprocessing classes, essential for handling user interaction and preparing data.
  - The user is involved in choosing the evaluation method and metrics to use for evaluating the model, as well as providing parameters like the number of neighbors to consider in the KNN algorithm.
  - Next, it proceeds with loading, cleaning, and standardizing the dataset through the Preprocessing class.
  - Then, it splits the dataset into training and test sets using the Input class.
  - The user needs to specify parameters such as the percentage of data to use for training and the number of neighbors to consider in the KNN algorithm.
  - Finally, the script creates an instance of the Evaluation class to evaluate the model's performance.
  - Depending on the evaluation method chosen by the user, the appropriate method of the Evaluation class is called to evaluate the model and return the results.

- __Required Classes:__
  - Preprocessing
  - Input
  - Evaluation
 
 ### **Input**

This class has the purpose to give to the user the choice of the input values.
These input values are: 

- k (with lower case), the number of neighbors to use in the KNN alghorithm.
- The percentage of dataset values to use for the training of the program (typical values are 70-80).
- The evaluation method (1 for holdout, 2 for the random subsampling).

If, and only if, in the evaluation method the choice was 2 (random subsampling) there will be another input for the user:

- K (with upper case), the number of experiments for the random subsampling.

Then the user can decide wich metrics use for valuating the performance of the program.
The metrics available are "Accuracy Rate", "Error Rate", "Sensitivity", "Specificity", "Geometric Mean".

-the user can decide if he want to use all the metrics (1) or if he want to use only some metrics (0).
 If, and only if, in the previous passage the user decide to use only some metrics (0), then
for every metric ther will be a question asking him if he wants to use that metric (1) or not (0).

The purpose of the class is also to verify if the user has insert for input a proper value.
If not, the program will ask again the user to insert the input, until it is an acceptable value.

### **Preprocessing**

The purpose of this class is to preprocess the data given from the dataset. What the class do is:

-Importing the dataset: the class will import the csv file of the dataset for the preprocessing

-Data clealing: if there is a line with missing values, that line is eliminated.

-Feature scaling (standardization): for the feature scaling, the choice was between the normalization and
the standardization. After some researches, the choice taken was for the standardization, also because
it is a type of feature scaling with an important characteristhic: if eventually there will be an outlayer (a value much bigger than the others, completely out of scale)
it will not falses the results of the algorithm.

-Data partitioning:  The class divides the data into two groups, features and target label. This is necessary for the data processing in the algorithm.

This class uses the Pandas library.




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




