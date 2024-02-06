# Description of Implemented Classes
This section describes the classes implemented in the project and their functionalities. The project implements the K-Nearest Neighbors (KNN) algorithm for classification. The classes are designed to handle user interaction, data preprocessing, model evaluation, and the KNN algorithm itself.

## Index
1. [Main](#1-main)
2. [Input](#2-input)
3. [Preprocessing](#3-preprocessing)
4. [Evaluation](#4-evaluation)
5. [KNNAlgorithm](#5-knnalgorithm)

- [Return to README](../README.md)

### 1. **Main**
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

[Quickly return to the top](#description-of-implemented-classes)
 
### 2. **Input**

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

[Quickly return to the top](#description-of-implemented-classes)

### 3. **Preprocessing**

The purpose of this class is to preprocess the data given from the dataset. What the class do is:

- Importing the dataset: the class will import the csv file of the dataset for the preprocessing. The program asks the user to enter the path of the file.

- Data cleaning: if there is a line with missing values, that line is eliminated.

- Feature scaling (standardization): for the feature scaling, the choice was between the normalization and
the standardization. After some researches, the choice taken was for the standardization, also because
it is a type of feature scaling with an important characteristhic: if eventually there will be an outlayer (a value much bigger than the others, completely out of scale)
it will not falses the results of the algorithm.

- Data partitioning:  The class divides the data into two groups, features and target label. This is necessary for the data processing in the algorithm.

This class uses the Pandas library.

[Quickly return to the top](#description-of-implemented-classes)

### 4. **Evaluation**
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

[Quickly return to the top](#description-of-implemented-classes)

### 5. **KNNAlgorithm**
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
  
[Quickly return to the top](#description-of-implemented-classes)
  
