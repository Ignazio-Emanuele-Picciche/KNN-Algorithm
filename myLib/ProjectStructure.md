# Project Structure
In this section, we will discuss the project structure of the application. The project structure refers to the organization of files and folders within the application. It plays a crucial role in maintaining the application, adding new features, and facilitating collaboration. A well-defined project structure enhances code readability and navigation.

## Index
1. [Flow Diagram](#1-flow-diagram)
2. [Class Structure](#2-class-structure)
3. [Branching Strategy](#3-branching-strategy)


## 1. Flow Diagram
The following diagram illustrates the flow of the application.
It provides a high-level overview of the application's architecture and the interaction between different components.



## 2. Class Structure


## 3. Branching Strategy
We have adopted the Gitflow branching strategy for managing the source code. It is a robust branching model that provides a clear path for creating new features, fixing bugs, and releasing new versions. The Gitflow model consists of two main branches: main and develop. The main branch contains the production-ready code, while the develop branch contains the latest code that is ready for release. Additionally, it uses feature, and hotfix branches to manage new features and bug fixes, respectively.

In particular, the Gitflow model consists of the following branches:
- **Main**: The main branch contains the production-ready code. It is the branch from which the application is deployed to the production environment.
- **Develop**: The develop branch contains the latest code that is ready for release. It is the branch from which the code is deployed to the staging environment for testing.
- **Feature**: The feature branches are used to develop new features. They are created from the develop branch and merged back into the develop branch once the feature is complete.
    - Feature branches are named using the following convention: `feature/<feature-name>`.
    - Feature branches should be created for each new feature and are deleted once the feature is merged into the develop branch.
- **Hotfix**: The hotfix branches are used to fix bugs in the production code. They are created from the main branch and merged back into both the main and develop branches once the bug is fixed.
    - Hotfix branches are named using the following convention: `hotfix/<bug-name>`.
    - Hotfix branches should be created for each bug fix and are deleted once the bug is merged into the main and develop branches.