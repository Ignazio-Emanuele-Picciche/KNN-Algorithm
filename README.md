# **_KNN Algorithm - Programming and Experimental Methods for Artificial Intelligence (23/24)_**

## Index
1. [Project Description](#1-general-description-of-the-project)
    - [Project Structure](./myLib/Project_Structure.md)
2. [Classes](#2-description-of-implemented-classes)
3. [Configure the environment](#3-configure-the-environment)


## 1. General description of the project

This project, made by Alessia Rossi, Ignazio Emanuele Piccichè and Riccardo Polacchi, 
has the purpose to develop a program which takes a dataset with informations and characteristics of some tumoral cells
and, after the processing of the data and the training of the model, predicts the type of the tumoral cell (if benign or malignant).
The final objective of the program is to test the performance of the machine learning model and to give and evaluation 
of the results, with plots and metrics.
The model uses the KNN algorithm, and for the evaluation it uses the holdout or the random subsampling method (the choice
is made by the user). 
It is structured with a pipeline of different classes, which are Input class, Preprocessing class, KNN class and Evaluation class,
all of them utilized in the Main of the program.
The user can decide the value of the inputs and the type of evaluation and metrics (for further information read the [section](#inputs-required-by-the-program) 
with the instructions for the user).
The dataset utilized is taken from [here](http://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original),
it is a .csv file which contains the following data for every single cell:

- A sample code number. 

- 9 types of features, wich one with a value from 1 to 10, which are "clump thickness", "uniformity of cell size",
 "uniformity of cell shape", "marginal adhesion", "single epithelial cel size", "bare nuclei", "bland chromatin",
 "normal nucleoli", "mitoses".

- The class label, wich value is 2 if there is a benign tumor, and 4 it there is a malignant tumor.

###  K-Nearest Neighbors Algorithm
*The K-nearest neighbor (KNN) algorithm* is a classification technique that operates by evaluating the characteristics of objects close to the one under examination. In practice, KNN classifies an object based on its similarity to other known objects in the dataset. This is done by calculating the distance between the features of the object to be classified and those of the objects already present in the system. By using the "k" nearest objects, the algorithm determines the class of the object under examination.

To identify the nearest neighbors of a query point, KNN calculates the distance between the query point and the other data points in the dataset. Among the various distance measures available, the Euclidean distance (p=2) is often the most common choice, as it calculates a straight line between the query point and the other points.

*The parameter "k"*  in the KNN algorithm specifies the number of neighbors to consider for classifying a given point. For example, if k=1, the object will be assigned to the same class as its nearest neighbor. However, the choice of "k" is crucial and can affect the model's performance. Low values of "k" can lead to high variability but low bias, while high values can cause high bias and lower variability. The choice of "k" depends on the type of data and the level of noise in the dataset.

[Quickly return to the top](#knn-algorithm---programming-and-experimental-methods-for-artificial-intelligence-2324)

## 2. Description of Implemented Classes

- [KNNAlgorithm](#knnalgorithm)
- [Main](#main)
- [Input](#input)
- [Preprocessing](#preprocessing)
- [Evaluation](#evaluation)

### **KNNAlgorithm**  
This class implements the KNN algorithm.

It contains methods for calculating Euclidean distance and predicting the class of a point.



- __Method:model_prediction__
- The model_prediction method takes a test dataset x_test as input and returns a list of predicted class labels for the test dataset.
  - This method predicts the KNN model on the provided test data. 
  - For each point in the test dataset, it calculates the Euclidean distance from all points in the training dataset.
  - It sorts these distances in ascending order and selects the smallest k distances. 
  - Then it looks at the class labels of these k nearest neighbors.
  - The predicted class label for the test point is the most common class label among these k nearest neighbors.
  - In case of a tie, it randomly selects one of the most common class labels.
  - This process is repeated for all points in the test dataset, and a list of predicted class labels is returned.
  

- __Method: calculate_euclidean_distance__
- The calculate_euclidean_distance method calculates the Euclidean distance between two points.


- __Using the KNNAlgorithm Class__
  - To use the KNNAlgorithm class, you need a training dataset and a test dataset.
  - Create an instance of the class and pass the parameters k, x_train, and y_train to the constructor.
   ```python
    knn = KNNAlgorithm(k, x_train, y_train)
    ```
  -  Then, you can call the model_prediction method with the test dataset to get the predicted class labels.
   ```python
    y_pred = knn.model_prediction(x_test)
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

- Importing the dataset: the class will import the csv file of the dataset for the preprocessing. The program asks the user to enter the path of the file.

- Data cleaning: if there is a line with missing values, that line is eliminated.

- Feature scaling (standardization): for the feature scaling, the choice was between the normalization and
the standardization. After some researches, the choice taken was for the standardization, also because
it is a type of feature scaling with an important characteristhic: if eventually there will be an outlayer (a value much bigger than the others, completely out of scale)
it will not falses the results of the algorithm.

- Data partitioning:  The class divides the data into two groups, features and target label. This is necessary for the data processing in the algorithm.

This class uses the Pandas library.

### Evaluation
The purpose of this class is to evaluate the KNN model with two methodology _(Holdout or Random Subsamplig Validation)_.
- **Holdout Validation**:
  1. Splitting the data: the data is randomly split (the percentage is specified in input) into training data and test data
  2. Training the model: the model is then trained by feeding it the X_train and y_train data
  3. Testing the model: the model is then tested with the test data (X_test)
  4. Evaluating performance: the newly trained model is then evaluated using the test data (y_test). The model's performance is calculated using various metrics.
  5. Analyzing the results: the metrics found are analyzed to understand how well the model generalizes on unknown data
  
- **Random Subsampling Validation**:
  1. Specify in input the number of experiments (K) to be performed
  2. Specify in input the percentage for the training and testing data
  3. Training the model: the model is then trained using X_train and y_train
  4. Evaluating performance: the newly trained model is then evaluated using the test data (y_test). The model's performance is calculated using various metrics
  5. Multiple iterations: the process is repeated multiple times (K times), with new random splits of the dataset, to obtain a more robust estimate of the model's performance. Finally, the multiple evaluations are aggregated to obtain a common measure of the model's performance.
  6. Analyzing the results: the metrics found are analyzed to understand how well the model generalizes on unknown data

In this class the chosen metrics are calculated and these are represented graphically (with plot and boxplot).

At the end of the program the metrics are saved in Metrics.txt file. 

[Quickly return to the top](#knn-algorithm---programming-and-experimental-methods-for-artificial-intelligence-2324)

## 3. Configure the environment
Before running the code, there are some precautions to take.
1. Create your own virtual environment from the terminal, by typing the command:
    - `python -m venv venv`
2. If you want to work from the terminal, you need to activate the just created virtual environment with the command:
    - for Windows -> `.\venv\Scripts\activate`
    - for Unix or MacOS -> `source ./venv/Scripts/activate`
3. To deactivate the environment use the command:
    - `deactivate`
4. To install the application in a new context, after cloning the project and creating a virtual environment, use the command:
    - `pip install -r requirements.txt`
      (This command is used to download all the non-standard modules required by the application)

> [!WARNING]
Update pip if the Python version used to generate the virtual environment does not contain an updated version of pip.
Use the command: `pip install --upgrade pip`


Now that we have set up our virtual environment, we can run the application.
Just go to the main.py file and run it.

[Quickly return to the top](#knn-algorithm---programming-and-experimental-methods-for-artificial-intelligence-2324)