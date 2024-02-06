# Project Structure
In this section, we will discuss the project structure of the application. The project structure refers to the organization of files and folders within the application. It plays a crucial role in maintaining the application, adding new features, and facilitating collaboration. A well-defined project structure enhances code readability and navigation.

## Index
1. [Flow Diagram](#1-flow-chart)
2. [Class Structure](#2-class-structure)
3. [Branching Strategy](#3-branching-strategy)

- [Return to README](../README.md)


## 1. Flow Chart
The following diagram illustrates the flow of the application.
It provides a high-level overview of the application's architecture and the interaction between different components.

[Quickly return to the top](#project-structure)

## 2. Class Structure
The application is organized into several classes, each of which is responsible for a specific task. The following is the class structure of the application:

> Input and preoprocessing classes
><p>
><img src='https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/5af95837-6f12-4bb3-8e12-599d4bc351ce', width="200" >
><img src='https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/513880e3-03b4-4e41-83d7-c3ec73cdfd56', width="250" >
></p>

>Evaluation:
><p>
><img src='https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/8e450ad0-3f5d-45b9-b905-a561916df7fb', width="700">
></p>

> KNNAlgorithm:
><p>
><img src='https://github.com/Ignazio-Emanuele-Picciche/ProgettoProgrammazioneAA23-24/assets/82161529/5d093415-108a-4b97-ab54-743831ddb603', width="500">
></p>

[Quickly return to the top](#project-structure)

## 3. Branching Strategy
We have adopted the Gitflow branching strategy for managing the source code. It is a robust branching model that provides a clear path for creating new features and fixing bugs. The Gitflow model consists of two main branches: main and develop. The main branch contains the production-ready code, while the develop branch contains the latest code that is ready for release. Additionally, it uses feature, and hotfix branches to manage new features and bug fixes, respectively.

In particular, the Gitflow model consists of the following branches:
- **Main**: The main branch contains the production-ready code. It is the branch from which the application is deployed to the production environment.
- **Develop**: The develop branch contains the latest code that is ready for release. It is the branch from which the code is deployed to the staging environment for testing.
- **Feature**: The feature branches are used to develop new features. They are created from the develop branch and merged back into the develop branch once the feature is complete.
    - Feature branches are named using the following convention: `features/<feature-name>`.
    - Feature branches should be created for each new feature and are deleted once the feature is merged into the develop branch.
    - For example, we created some feature branches such as `features/classePreprocessing`, `features/classeEvaluation`, `features/classeKnn`, etc.
- **Hotfix**: The hotfix branches are used to fix bugs in the production code. They are created from the main branch and merged back into both the main and develop branches once the bug is fixed.
    - Hotfix branches are named using the following convention: `hotfix/<bug-name>`.
    - Hotfix branches should be created for each bug fix and are deleted once the bug is merged into the main and develop branches.
    - For example, we created some hotfix branches such as `hotfix/requirementsFile`, etc.

[Quickly return to the top](#project-structure)