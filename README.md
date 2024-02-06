# **_KNN Algorithm - Programming and Experimental Methods for Artificial Intelligence (23/24)_**

## Index
1. [Project Description](#1-general-description-of-the-project)
    - [Project Structure](./myLib/Project_Structure.md)
2. [Classes](#2-description-of-implemented-classes)
    - [Classes Description](./myLib/Classes_Description.md)
3. [Configure the environment](#3-configure-the-environment)
4. [Inputs & Outputs Program](./myLib/Inputs_%26_Outputs_Program.md)


### 1. General description of the project

This project, made by Alessia Rossi, Ignazio Emanuele Piccichè and Riccardo Polacchi, 
has the purpose to develop a program which takes a dataset with informations and characteristics of some tumoral cells
and, after the processing of the data and the training of the model, predicts the type of the tumoral cell (if benign or malignant).
The final objective of the program is to test the performance of the machine learning model and to give and evaluation 
of the results, with plots and metrics.
The model uses the KNN algorithm, and for the evaluation it uses the holdout or the random subsampling method (the choice
is made by the user). 
It is structured with a pipeline of different classes, which are Input class, Preprocessing class, KNN class and Evaluation class,
all of them utilized in the Main of the program.
The user can decide the value of the inputs and the type of evaluation and metrics (for further information read the [section](./myLib/Inputs_%26_Outputs_Program.md#1-inputs-required-by-the-program) 
with the instructions for the user).
The dataset utilized is taken from [here](http://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original),
it is a .csv file which contains the following data for every single cell:

- A sample code number. 

- 9 types of features, wich one with a value from 1 to 10, which are "clump thickness", "uniformity of cell size",
 "uniformity of cell shape", "marginal adhesion", "single epithelial cel size", "bare nuclei", "bland chromatin",
 "normal nucleoli", "mitoses".

- The class label, wich value is 2 if there is a benign tumor, and 4 it there is a malignant tumor.

####  K-Nearest Neighbors Algorithm
*The K-nearest neighbor (KNN) algorithm* is a classification technique that operates by evaluating the characteristics of objects close to the one under examination. In practice, KNN classifies an object based on its similarity to other known objects in the dataset. This is done by calculating the distance between the features of the object to be classified and those of the objects already present in the system. By using the "k" nearest objects, the algorithm determines the class of the object under examination.

To identify the nearest neighbors of a query point, KNN calculates the distance between the query point and the other data points in the dataset. Among the various distance measures available, the Euclidean distance (p=2) is often the most common choice, as it calculates a straight line between the query point and the other points.

*The parameter "k"*  in the KNN algorithm specifies the number of neighbors to consider for classifying a given point. For example, if k=1, the object will be assigned to the same class as its nearest neighbor. However, the choice of "k" is crucial and can affect the model's performance. Low values of "k" can lead to high variability but low bias, while high values can cause high bias and lower variability. The choice of "k" depends on the type of data and the level of noise in the dataset.

[Quickly return to the top](#knn-algorithm---programming-and-experimental-methods-for-artificial-intelligence-2324)

### 2. Description of Implemented Classes

- [Main](./myLib/Classes_Description.md#1-main)
- [Input](./myLib/Classes_Description.md#2-input)
- [Preprocessing](./myLib/Classes_Description.md#3-preprocessing)
- [Evaluation](./myLib/Classes_Description.md#4-evaluation)
- [KNNAlgorithm](./myLib/Classes_Description.md#5-knnalgorithm) 

[Quickly return to the top](#knn-algorithm---programming-and-experimental-methods-for-artificial-intelligence-2324)

### 3. Configure the environment
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