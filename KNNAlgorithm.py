#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Alessia Rossi

from operator import itemgetter
import numpy as np
'''
- Definition of the methods of the KNNAlgorithm class:
    - constructor
    - model_prediction -> Performs the prediction of the K-Nearest Neighbors (KNN) model on the provided test data
    - calculate_euclidean_distance -> Calculates the Euclidean distance between two points using the standard Euclidean distance formula
'''
class KNNAlgorithm:
    def __init__(self, k, x_train, y_train):
        # Constructor of the KNN algorithm
        # Initializes the parameters k, x_train, and y_train
        self.k = k
        # Model training parameters
        self.x_train = x_train  # Features (B a J)
        self.y_train = y_train  # Labels (K)

    def model_prediction(self, x_test):
        '''
           - The model_prediction method has two nested for loops, the first to scroll through the test points and the second to scroll through the training points.
             - For each test_point, the Euclidean distance between that point and all the points in the x_train training dataset is calculated.
             - The Euclidean distance is calculated using the euclidean_distance_calculation method.
             - For each test_point, a list of distances is created, containing the Euclidean distance between that point and all the points in the x_train training dataset,
               along with their respective classes in the y_train dataset.
             - The distance list is sorted in ascending order.
             - The first k distances from the sorted distance list are selected.
             - The first k classes of the training points are extracted.
             - The numerosity of the classes of the k neighbors is calculated.
             - The class (or classes) with the highest numerosity is selected.
             - In the case where there are more classes with the highest numerosity, one of the two classes is randomly chosen.
             - The chosen class is added to the list of predictions.
             - The steps are repeated for all the test points in the x_test dataset.
             - The list containing the predictions, i.e., the selected classes for each test point, is returned.
        '''
        # Method to perform the model prediction on the test data
        predictions = [] # List where the predictions will be saved
        for _, test_point in x_test.iterrows(): # Parameter that I don't use, it indicates the index
            distances = [] # List of distances between the x_test point and the x_train points
            for index, train_point in self.x_train.iterrows():
                # Calculation of the Euclidean distance between the x_test point and the x_train points
                dist = self.__calculate_euclidean_distance(train_point, test_point)  # Euclidean_distance_calculation method
                # We add to the distances list the pair distance, class of belonging
                distances.append(((dist),self.y_train[index]))

            # We sort the distances in ascending order
            distances= sorted(distances, key=itemgetter(0), reverse=False)
            # We select the first k distances from the sorted list of distances
            k_distances = distances[:self.k]
            # We extract the classes corresponding to the first k distances
            k_neighbors = np.array(k_distances)[:, 1].astype(int)

            # Count the numerosity of the classes of the k neighbors
            neighbors, numerosity = np.unique(k_neighbors, return_counts=True)
            # Convert neighbors into a list
            # Select those with higher numerosity
            max_numerosity = max(numerosity)
            # Create a list containing the class (or classes) with numerosity equal to the maximum
            most_common = [neighbors[i] for i, elem in enumerate(numerosity) if max_numerosity == elem]
            # If there is only one class in the list, add it to predictions
            # Otherwise, randomly choose one of them
            if len(most_common) == 1:
                predictions.append(most_common[0])  # If there is only one element, add it to the predictions list
            else:
                random_choice = np.random.choice(most_common)  # If there are multiple elements, make a random choice
                predictions.append(random_choice)

        # Return the list of predictions, containing the predicted classes for each x_test
        return predictions

    def __calculate_euclidean_distance(self, x1, x2):
        '''
        - The calculate_euclidean_distance method within the KNNAlgorithm class calculates the Euclidean distance between two points.
            - The method takes two points as input, x1 and x2, calculates the difference between the two points,
            squares it, sums it, and then calculates the square root of the result.
            - The method returns the Euclidean distance.
        '''
        # Method for calculating the Euclidean distance
        x3 = x1 - x2 # Difference between the two points
        distances = np.sqrt(np.sum(pow(x3, 2))) # Calculation of the Euclidean distance
        return distances

