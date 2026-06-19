from libraries import * 


def Info_tab():
    st.write("""
# Info Tab

## General App Information

This application is used for data visualization and comparison of machine learning algorithms. To achieve this functionality, the Streamlit tool is used. More specifically, the application supports various features such as: 
  - Loading tabular data (.csv).
  - Dataframe specifications. 
  - 2D visualizations based on different algorithms.
  - Machine Learning, where the user is given two types of algorithms to choose from (classification or clustering), and a comparison between the aforementioned algorithms can be performed in order to find the most efficient one. 
  - A presentation of how the application works (this page).

## How to Use it?

The usage of the application is simple and easy to understand for everyone. First, the user needs to upload their data in `CSV, Excel` format. After that, the user can decide which functionality of the application they want to use. On the left side of the window, the following options are available: `DataFrame_tab, Visualization_tab, Machine_Learning_tab, Info_tab`, each performing a different function with a detailed description below:

### Data Frame tab:

If the user is interested in `displaying their dataset` in table form, they can select DataFrame_tab to inspect it. First, various information about the dataset is displayed, and then the user is given the additional option to choose how to present the dataset with or without labels. 

#### Labels option
If the labels option is selected, the dataset is split into two parts, `Samples X Features` and `Labels`, taking the last column of the dataset:


![dataframe_labels](https://github.com/PanMour/image_1/assets/115315282/4eebce57-0759-4816-a8b8-3e23f2ae4c61)

#### No labels option
If the no labels option is selected, the entire dataset is displayed as `Samples X Features`.

![dataframe_no_labels](https://github.com/PanMour/image_1/assets/115315282/84048f00-cb49-4805-b880-85ed1b8a1667)

### Visualization tab:

If the user wants to perform 2D visualization based on two dimensionality reduction algorithms (PCA, t-SNE), they can select the Visualization_tab. Here, using the data provided by the user in the initial step, visualizations are created and displayed depending on the chosen algorithm.

- The two available algorithms are PCA and t-SNE.
- Additionally, three exploratory data analysis (EDA) plots are presented: a Histogram, a Density plot, and a Boxplot based on the user’s dataset.

### Machine Learning tab:

If the user wants to implement and compare Machine Learning algorithms, they can select the Machine_Learning_tab. Here, they can choose between classification algorithms (Support Vector Machines, K-Nearest Neighbors) and clustering algorithms (Agglomerative Clustering, Affinity Propagation). After selecting the desired algorithms, the user must provide values for each algorithm’s parameters.

#### **Classification Algorithms:**

**The user must provide:**

- **a)** the regularization C parameter for Support Vector Machines,
- **b)** the number of neighbors k for K-Nearest Neighbors

#### **Clustering Algorithms:**

**The user must provide:**

- **a)** the number of clusters for Agglomerative Clustering,
- **b)** the bandwidth parameter for Affinity Propagation Clustering.

Additionally, the user can compare the performance of the algorithms and find the most efficient one by pressing **"Start Analysis"**. After a short time, the performance of both selected algorithms will be displayed, along with which one performed best and its accuracy percentage.

### Info tab:

Finally, if the user needs help with how the application works or wants to see general information about it, they can select the Info_tab. This section provides general information about the application, how it works, the development team, and which tasks each member completed.

## Team Members

The development team of the application consists of Nikolas Anagnostopoulos, Achilleas Zervos, and Panagiotis Mouralatos, students at the Ionian University in their 3rd year of studies.

## Tasks Completed by each member

- ### Data Frame
  The development of the Data Frame was handled and completed by Nikolas Anagnostopoulos (ID: inf2021013)

- ### Visualization
  The development of Visualization was handled and completed by Achilleas Zervos (ID: inf2021055)

- ### Machine Learning
  The development of Machine Learning was handled and completed by Nikolas Anagnostopoulos (ID: inf2021013)

- ### Info
  The development of Info was handled and completed by Panagiotis Mouralatos (ID: inf2021147)

## github profiles (application repo):
#### organization:
  - Team: [github/TechTeam-inf2021](https://github.com/TechTeam-inf2021/data_analysis_dev_app)
#### members:
  - Panagiotis Mouralatos: [github/PanMour](https://github.com/PanMour/data_analysis_dev_app)
  - Nikolas Anagnostopoulos: [github/inf2021013](https://github.com/inf2021013/data_analysis_dev_app)
  - Achilleas Zervos: [github/Axileaszervos](https://github.com/Axileaszervos/data_analysis_dev_app)
""")