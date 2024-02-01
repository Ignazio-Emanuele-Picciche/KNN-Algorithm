#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from KNNAlgorithm import KNNAlgorithm

'''
@Author: Ignazio Emanuele Piccichè

In this class, the evaluation of the model is performed.
The evaluation is performed using two different methodologies:
    - Holdout
    - Random Subsampling

- Definition of the methods of the Evaluation class:
    - constructor
    - data_splitting -> Method that divides the data into training and testing data
    - holdout_validation -> Method that evaluates the model using the "Holdout" methodology
    - random_subsampling_validation -> Method that evaluates the model using the "Random Subsampling" methodology
    - metrics_calculation -> Method that calculates the requested evaluation metrics (Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean)
    - save_metrics -> Method that saves the calculated metrics in the Metrics.txt file
    - metrics_plot -> Method that plots the calculated metrics. Plot of the metrics as a function of the number of experiments and boxplot of the metrics.
'''
class Evaluation:
    

    '''
    constructor

        Parameters
        ----------
        features : pandas.DataFrame
            data that will be used to train and test the model
        target : pandas.Series
            data that will be used to train and test the model
        training_perc : int
            percentage of data that will be used to train the model
        k : int
            number of neighbors to consider
        chosen_metrics : list
            list of the metrics chosen by the user

        Returns
        -------
        None
    '''
    def __init__(self, features:pd.DataFrame, target:pd.Series, training_perc:int, k:int, chosen_metrics:list):
        self.features = features
        self.target = target
        self.training_perc = training_perc
        self.k = k
        self.chosen_metrics = chosen_metrics
        
    '''
    In this method the data are divided into training and testing data.

        The training data will be used to train the model, while the testing data will be used to test the model.

        Parameters
        ----------
        features : pandas.DataFrame
            data that will be used to train and test the model
        target : pandas.Series
            data that will be used to train and test the model
        training_perc : int
            percentage of data that will be used to train the model

        Returns
        -------
        X_train : pandas.DataFrame
            data that will be used to train the model
        y_train : pandas.Series
            target data that will be used to train the model
        X_test : pandas.DataFrame
            data that will be used to test the model
        y_test : pandas.Series
            target data that will be used to compare the predictions of the model
    '''
    def data_splitting(self, features:pd.DataFrame, target:pd.Series, training_perc:int):
        X_train = features.sample(frac = training_perc/100) # Get the training data according to a percentage specified in input
        X_test = features.drop(X_train.index) # Get the test data. These are all the data that were not taken for training

        y_train = target.drop(X_test.index) # Save the y train corresponding to the x train
        y_test = target.drop(X_train.index) # Save the y test corresponding to the x test

        return X_train, y_train, X_test, y_test


    '''   
    The holdout evaluation process consists of:
        1. Splitting the data: the data is randomly split (the percentage is specified in input) into training data and test data
        2. Training the model: the model is then trained by feeding it the X_train and y_train data
        3. Testing the model: the model is then tested with the test data (X_test)
        4. Evaluating performance: the newly trained model is then evaluated using the test data (y_test). The model's performance is calculated using various metrics.
        5. Analyzing the results: the metrics found are analyzed to understand how well the model generalizes on unknown data

        Parameters
        ----------
        None

        Returns
        -------
        None
    '''
    def holdout_validation(self):
        X_train, y_train, X_test, y_test = self.data_splitting(self.features, self.target, self.training_perc) # call the method that splits the data into training and testing data

        knnModel = KNNAlgorithm(self.k, X_train, y_train) # Train the model by providing it with the training data
        predictions = knnModel.model_prediction(X_test) # Make a prediction with the model trained previously

        # Call the method that calculates the metrics, passing it the test data and predictions
        Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = self.metrics_calculation(y_test, predictions) 

        # Call the method that saves the newly calculated metrics in the Metrics.txt file
        self.save_metrics(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean) 


    ''' 
    The random subsampling evaluation process consists of:
        1. Specifying the number of experiments (K) to be performed as input
        2. Specifying the percentage for the training and testing data as input
        3. Training the model: the model is then trained using X_train and y_train
        4. Evaluating performance: the newly trained model is then evaluated using the test data (y_test). The model's performance is calculated using various metrics
        5. Multiple iterations: the process is repeated multiple times (K times), with new random splits of the dataset, to obtain a more robust estimate of the model's performance. Finally, the multiple evaluations are aggregated to obtain a common measure of the model's performance.
        6. Analyzing the results: the metrics found are analyzed to understand how well the model generalizes on unknown data

        Parameters
        ----------
        K : int
            number of experiments 

        Returns
        -------
        None
    '''
    def random_subsampling_validation(self, K:int):
        # Initialize the lists that will contain the values of the metrics calculated for each iteration
        Accuracy_rate_scores = []
        Error_rate_scores = []
        Sensitivity_scores = []
        Specificity_scores = []
        Geometric_mean_scores = []

        # As provided by the random subsampling evaluation process, this is repeated K times
        for _ in range(K):
            # Call the method that splits the data into training data and testing data
            X_train, y_train, X_test, y_test = self.data_splitting(self.features, self.target, self.training_perc) 

            # Train the model by providing it with the training data
            knnModel = KNNAlgorithm(self.k, X_train, y_train) 

            # Make a prediction with the model trained previously
            predictions = knnModel.model_prediction(X_test) 

            # Call the method that calculates the metrics, passing it the test data and predictions
            Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = self.metrics_calculation(y_test, predictions) 
                    
            # Add the values of the calculated metrics, for this experiment, to the lists
            Accuracy_rate_scores.append(Accuracy_rate)
            Error_rate_scores.append(Error_rate)
            Sensitivity_scores.append(Sensitivity)
            Specificity_scores.append(Specificity)
            Geometric_mean_scores.append(Geometric_mean)

        # Calculate the average values for each metric calculated in the K experiments
        Accuracy_rate_mean = np.mean(Accuracy_rate_scores)
        Error_rate_mean = np.mean(Error_rate_scores)
        Sensitivity_mean = np.mean(Sensitivity_scores)
        Specificity_mean = np.mean(Specificity_scores)
        Geometric_mean_mean = np.mean(Geometric_mean_scores)

        # Call the method that saves the calculated metrics in the Metriche.txt file
        self.save_metrics(Accuracy_rate_mean, Error_rate_mean, Sensitivity_mean, Specificity_mean, Geometric_mean_mean) 

        # Call the method that plots the calculated metrics
        self.metrics_plot(Accuracy_rate_scores, Error_rate_scores, Sensitivity_scores, Specificity_scores, Geometric_mean_scores) 


    '''
    In this method, the confusion matrix values are first calculated, and then the requested metrics are calculated.

        Parameters
        ----------
        y_test : pandas.Series
            data that will be used to compare the predictions of the model
        prediction : list
            predictions made by the model

        Returns
        -------
        Accuracy_rate : float
            percentage of correct predictions out of the total predictions
        Error_rate : float
            percentage of incorrect predictions out of the total predictions
        Sensitivity : float
            ability of the model to correctly predict positive values
        Specificity : float
            ability of the model to correctly predict negative values
        Geometric_mean : float
            mean that balances positive and negative values
    '''
    def metrics_calculation(self, y_test:pd.Series, predictions:list):

        # Initialize the variables that will contain the values of the calculated metrics
        Accuracy_rate = 0
        Error_rate = 0
        Sensitivity = 0
        Specificity = 0
        Geometric_mean = 0

        # Calculation of the confusion matrix
        True_Negative = sum(1 for y, pred in zip(y_test.values, predictions) if (y == pred and pred == 2.0))
        True_Positive = sum(1 for y, pred in zip(y_test.values, predictions) if (y == pred and pred == 4.0))
        False_Positive = sum(1 for y, pred in zip(y_test.values, predictions) if (y != pred and pred == 4.0))
        False_Negative = sum(1 for y, pred in zip(y_test.values, predictions) if (y != pred and pred == 2.0))

        # Actual calculation of the requested metrics using the values of the confusion matrix, previously calculated
        if 1 in self.chosen_metrics:
            Accuracy_rate = (True_Negative + True_Positive) / y_test.size # Percentage of correct predictions out of the total predictions
        if 2 in self.chosen_metrics:
            Error_rate = (False_Positive + False_Negative) / y_test.size # Percentage of incorrect predictions out of the total predictions
        if 3 in self.chosen_metrics and (True_Positive + False_Negative) != 0:
            Sensitivity = (True_Positive) / (True_Positive + False_Negative) # Ability of the model to correctly predict positive values
        if 4 in self.chosen_metrics and (True_Negative + False_Positive) != 0:
            Specificity = (True_Negative) / (True_Negative + False_Positive) # Ability of the model to correctly predict negative values
        if 5 in self.chosen_metrics:
            Geometric_mean = np.sqrt((Sensitivity*Specificity)) # Mean that balances positive and negative values

        return Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean


    '''
    In this method, the calculated metrics are saved in a txt file.
        The name of the file will be: "Metrics.txt"

        Parameters
        ----------
        Accuracy_rate : float
            percentage of correct predictions out of the total predictions
        Error_rate : float
            percentage of incorrect predictions out of the total predictions
        Sensitivity : float
            ability of the model to correctly predict positive values
        Specificity : float
            ability of the model to correctly predict negative values
        Geometric_mean : float
            mean that balances positive and negative values

        Returns
        -------
        None
    '''
    def save_metrics(self, Accuracy_rate:float, Error_rate:float, Sensitivity:float, Specificity:float, Geometric_mean:float):
        # With the following operations, open the Metrics.txt file and write the calculated metrics into it
        with open('Metrics.txt', 'w') as file:
            file.write('Accuracy Rate: ' + str(Accuracy_rate) + '\n')
            file.write('Error Rate: ' + str(Error_rate) + '\n')
            file.write('Sensitivity: ' + str(Sensitivity) + '\n')
            file.write('Specificity: ' + str(Specificity) + '\n')
            file.write('Geometric Mean: ' + str(Geometric_mean) + '\n')
        # Close the Metrics.txt file
        file.close() 


    '''
    In this method, the metrics for each experiment are plotted and the metrics are represented with a boxplot.
        The representation is done using the matplotlib library.

        Parameters
        ----------
        Accuracy_rate : list
            list containing the values of the Accuracy Rate metric
        Error_rate : list
            list containing the values of the Error Rate metric
        Sensitivity : list
            list containing the values of the Sensitivity metric
        Specificity : list
            list containing the values of the Specificity metric
        Geometric_mean : list
            list containing the values of the Geometric Mean metric

        Returns
        -------
        None
    '''
    def metrics_plot(self, Accuracy_rate:list, Error_rate:list, Sensitivity:list, Specificity:list, Geometric_mean:list):
        labels = ['Accuracy Rate', 'Error Rate', 'Sensitivity', 'Specificity', 'Geometric Mean'] # Vector used to represent the labels of the graph
        values = [Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean] # Vector used to represent the values of the graph corresponding to the labels

        plt.figure(figsize=(10, 5)) # Set the size of the graph

        # With the following operations, we plot the requested metrics
        if 1 in self.chosen_metrics:
            plt.plot(Accuracy_rate, marker='o', linestyle='solid', linewidth=2, markersize=5, color='blue', label='Accuracy Rate')
        if 2 in self.chosen_metrics:
            plt.plot(Error_rate, marker='o', linestyle='solid', linewidth=2, markersize=5, color='green', label='Error Rate')
        if 3 in self.chosen_metrics:
            plt.plot(Sensitivity, marker='o', linestyle='solid', linewidth=2, markersize=5, color='red', label='Sensitivity')
        if 4 in self.chosen_metrics:
            plt.plot(Specificity, marker='o', linestyle='solid', linewidth=2, markersize=5, color='yellow', label='Specificity')
        if 5 in self.chosen_metrics:
            plt.plot(Geometric_mean, marker='o', linestyle='solid', linewidth=2, markersize=5, color='orange', label='Geometric Mean')

        plt.legend(loc='upper right') # Set the legend position in the graph
        plt.xlabel("Experiments") # Set the name of the x-axis label
        plt.ylabel("Values") # Set the name of the y-axis label
        plt.title("Metrics trend") # Set the title of the graph
        plt.tight_layout() # Optimizes the layout of the subpanels in the graph to avoid overlaps
        #plt.show() # Show the graph


        # Create a new figure to represent the boxplot of the metrics
        plt.figure(figsize=(10, 5))
        plt.boxplot(values)

        plt.xlabel("Metrics") # Set the name of the x-axis label
        plt.ylabel("Values") # Set the name of the y-axis label
        plt.title("Boxplot of metrics") # Set the title of the graph
        plt.xticks(range(1, len(labels) + 1) ,labels, rotation=45) # Set the labels of the x-axis and their rotation
        plt.tight_layout() # Optimizes the layout of the subpanels in the graph to avoid overlaps

        plt.show() # Show the graph