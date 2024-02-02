#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
- Definition of the methods of the Input class:
    - constructor
    - k_neighbors -> Asks the user to enter the number of neighbors k to use for the classifier
    - training_percentage -> Asks the user to enter the percentage for the training
    - evaluation_method -> Asks the user to choose the evaluation method (holdout or random subsampling)
    - metric_selection -> Asks the user to choose the metrics to use for the evaluation
'''


class Input:
    '''
    The Input class is necessary to manage the user input for the program.
    This class is structured as follows:
    - The constructor initializes the parameters k, training, and K.
    - The k_neighbors method asks the user to enter the number of neighbors k to use for the classifier.
    - The training_percentage method asks the user to enter the percentage for the training.
    - The evaluation_method method asks the user to choose the evaluation method (holdout or random subsampling).
    - The metric_selection method asks the user to choose the metrics to use for the evaluation.
    '''
    def __init__(self):   # Constructor of the Input class

        self.k=0   # number of neighbors k to use for the classifier
        self.training=1   # percentage for the training
        self.K=0   # number of experiments K for the random subsampling


    def k_neighbors(self):
        '''
        The k_neighbors method asks the user to enter the number of neighbors k to use for the classifier.
        The user must enter an integer number greater than 0.
        The program does not go on until the user enters a valid number.
        '''
        while True:   # the program does not go on until the user enters a valid number
            k = input("Enter the number of neighbors k to use for the classifier: ")   # the user is asked to enter the number of neighbors k
            if k.isdigit() and int(k) > 0:   # if the user enters a valid number (an integer greater than 0)
                self.k = int(k)   # the number of neighbors k is saved
                break   # the program goes on
        return self.k   # the number of neighbors k is returned


    def training_percentage(self):
        '''
        The training_percentage method asks the user to enter the percentage for the training.
        The user must enter an integer number between 0 and 100 (but not 0 or 100).
        The program does not go on until the user enters a valid number.
        '''
        while True:
            training = input("Enter the percentage for the training: ")   # the user is asked to enter the percentage for the training

            if training.isdigit() and 0 < int(training) < 100:   # if the user enters a valid number (an integer between 0 and 100 but not 0 or 100)
                self.training = int(training)   # the percentage for the training is saved
                break   # the program goes on

        return self.training
    def evaluation_method(self):
        '''
        The evaluation_method method asks the user to choose the evaluation method (holdout or random subsampling).
        The user must enter 1 or 2, 1 for the holdout, 2 for the random subsampling.
        The program does not go on until the user enters a valid number.
        If the user chooses the random subsampling, the user is asked to enter the number of experiments K.
        The program does not go on until the user enters a valid number for K
        '''
        evaluation=0

        while evaluation !="1" or evaluation !="2":   # the program does not go on until the user enters a valid number

            evaluation = (input("Enter 1 to choose holdout, 2 to choose random subsampling: "))   # the user is asked to enter 1 or 2

            if evaluation=="1":

                return int(evaluation)   # if the user enters 1, the method returns 1

            elif evaluation=="2":   # if the user enters 2
                while True:   #
                    K = input("Enter the number of experiments K for the random subsampling: ")   # the user is asked to enter the number of experiments K
                    if K.isdigit() and int(K) > 0:   # if the user enters a valid number (an integer greater than 0)
                        self.K = int(K)   # the number of experiments K is saved
                        break
                return int(evaluation)   # the method returns 2


    def metrics_selection(self):
        '''
        The metrics_selection method asks the user to choose the metrics to use for the evaluation.
        The available metrics are: Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean.
        At the beginning, the user is asked if he wants to use all the metrics (entering 1), if he answers no (entering 0), he can choose which metrics to use.
        If the user chooses 1, all the metrics are used.
        If the user chooses 0, he can choose which metrics to use.
        The user is asked to enter 1 to choose a metric, 0 to not choose it, and then the same thing is asked for each subsequent metric.
        The program does not go on until the user chooses.
        The chosen metrics are saved in a list, which is returned by the method.
        '''

        metrics = []   # the list of metrics to use is initialized
        metrics_selection = 0   # the variable that will contain the user's choice is initialized
        while metrics_selection != "1" or metrics_selection != "0":   # the program does not go on until the user enters a valid number
            metrics_selection = (input("Enter 1 to select all metrics, 0 to manually select metrics: "))   # the user is asked to enter 1 or 0
            if metrics_selection == "1":   # if the user enters 1
                metrics = [1, 2, 3, 4, 5]   # all the metrics are saved
                return metrics
            elif metrics_selection == "0":   # if the user enters 0, he has to choose which metrics to use
                accuracy_rate = 0
                while accuracy_rate != "1" or accuracy_rate != "0":
                    accuracy_rate = (input("Enter 1 to choose the Accuracy Rate metric, 0 to not choose it: "))   # the user is asked to enter 1 or 0 for the Accuracy Rate metric
                    if accuracy_rate == "1":
                        metrics.append(1)   # if the user enters 1, the Accuracy Rate metric is saved
                        break
                    elif accuracy_rate == "0":   # if the user enters 0, the program goes on without saving the Accuracy Rate metric
                        break
                error_rate = 0
                while error_rate != "1" or error_rate != "0":
                    error_rate = (input("Enter 1 to choose the Error Rate metric, 0 to not choose it: "))   # the user is asked to enter 1 or 0 for the Error Rate metric
                    if error_rate == "1":
                        metrics.append(2)   # if the user enters 1, the Error Rate metric is saved
                        break
                    elif error_rate == "0":   # if the user enters 0, the program goes on without saving the Error Rate metric
                        break
                sensitivity = 0
                while sensitivity != "1" or sensitivity != "0":
                    sensitivity = (input("Enter 1 to choose the Sensitivity metric, 0 to not choose it: "))   # the user is asked to enter 1 or 0 for the Sensitivity metric
                    if sensitivity == "1":
                        metrics.append(3)   # if the user enters 1, the Sensitivity metric is saved
                        break
                    elif sensitivity == "0":   # if the user enters 0, the program goes on without saving the Sensitivity metric
                        break
                specificity = 0
                while specificity != "1" or specificity != "0":
                    specificity = (input("Enter 1 to choose the Specificity metric, 0 to not choose it: "))   # the user is asked to enter 1 or 0 for the Specificity metric
                    if specificity == "1":
                        metrics.append(4)   # if the user enters 1, the Specificity metric is saved
                        break
                    elif specificity == "0":   # if the user enters 0, the program goes on without saving the Specificity metric
                        break
                geometric_mean = 0
                while geometric_mean != "1" or geometric_mean != "0":
                    geometric_mean = (input("Enter 1 to choose the Geometric Mean metric, 0 to not choose it: "))   # the user is asked to enter 1 or 0 for the Geometric Mean metric
                    if geometric_mean == "1":
                        metrics.append(5)   # if the user enters 1, the Geometric Mean metric is saved
                        break
                    elif geometric_mean == "0":   # if the user enters 0, the program goes on without saving the Geometric Mean metric
                        break
                return metrics   # the list of metrics to use is returned


