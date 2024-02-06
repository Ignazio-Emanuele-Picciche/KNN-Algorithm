#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the necessary classes
# Preprocessing for data cleaning and standardization
# Input for user input handling
# Evaluation for model performance evaluation
from Preprocessing import Preprocessing
from Input import Input
from Evaluation import Evaluation

if __name__ == '__main__':
    # Create instances of the Input and Preprocessing classes
    user_input = Input()
    preprocessing = Preprocessing()

    # Ask the user for the evaluation method and metrics to use
    evaluation_method = user_input.evaluation_method()
    chosen_metrics = user_input.metrics_selection()
    K = user_input.K

    # Ask the user for the percentage of data to use for training and the number of neighbors to consider
    training_perc = user_input.training_percentage()
    k = user_input.k_neighbors()

    # Load, clean, and standardize the dataset
    preprocessing.loading_dataset()
    preprocessing.data_cleaning()
    preprocessing.standardization()

    # Split the dataset into features and target label
    features, target = preprocessing.data_split()

    #  Create an instance of the Evaluation class to evaluate the model's performance
    evaluation = Evaluation(features, target, training_perc, k, chosen_metrics)

    if evaluation_method == 1:
        evaluation.holdout_validation()
    else:
        evaluation.random_subsampling_validation(K)
