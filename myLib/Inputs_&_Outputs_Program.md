# Inputs & Outputs Program

In this file, we will explain the inputs required by the program and the outputs that the program will generate.

## Index
1. [Inputs required by the program](#1-inputs-required-by-the-program)
2. [Program outputs](#2-program-outputs)

- [Return to README](../README.md)


## 1. Inputs required by the program
The inputs required by the application are as follows:
1. The path of the dataset file.
2. Choice of evaluation method (Holdout or Random Subsampling)
    - If you choose the Random Subsampling evaluation method, you will be asked to enter the number of K experiments.
3. Choose if you want all metrics or some specifics metrics:
    - If you choose the second option, you will be asked for each individual metric whether you want to calculate it or not. Consider that if you choose the Geometric Mean metric, the Sensitivity and Specificity metrics are also automatically calculated as they are part of the calculation for the chosen Geometric Mean metric.
      - The possible metrics are: Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean
4. The percentage of training.
5. The number of k neighbors to use for the classifier.


[Quickly return to the top](#inputs--outputs-program)

## 2. Program outputs
Once all the required inputs have been entered, there are two options for data displayed.

If you choose the Holdout validation method, the calculated metrics for the single experiment will be written in the Metrics.txt file

If you choose the Random Subsampling validation method, the averages of the calculated metrics in the K experiments (K specified in the inputs) will be represented in the Metrics.txt file.
In addition, two graphs will be displayed, one representing the trend of the calculated metrics for each experiment and the other representing the boxplots for each calculated metric.

_Example of a graph of the metrics displayed_
<p float="left">
  <img src="https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/95869d8d-832f-4577-8ebb-75de6df093b0" width="500" />
  <img src="https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/9c97b52e-a8e9-4ea7-9f65-80896b6fbf26" width="500" />
</p>

[Quickly return to the top](#inputs--outputs-program)