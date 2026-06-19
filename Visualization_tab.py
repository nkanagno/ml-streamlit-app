from libraries import *

# Function for PCA visualization
def visualize_pca(data, labels_names):
    # t-SNE title
    st.write("## PCA Algorithm")
    st.write("### Plot:")
    # Perform PCA and fits dataset
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data)
    
    # get unique labels names
    unique_labels_names = np.unique(labels_names)
    
    # create plt fig
    plt.figure(figsize=(8, 6))
        
    # Plot PCA results
    try:
        # if there are labels it plots the data with different colors
        
        # each label point gets a different color
        for label in unique_labels_names:
            plt.scatter(pca_result[labels_names == label, 0], pca_result[labels_names == label, 1], 
                        label=label, cmap='viridis')
            
        # Display labels in right corner
        plt.legend(title='Labels', loc='center left', bbox_to_anchor=(1, 0.5))
    except:
        # if there are no labels it plots the data with the same color
        plt.scatter(pca_result[:,0], pca_result[:,1], color='blue')
    
    # set title, x-label, y-label names
    plt.title('PCA Visualization')
    plt.xlabel('features')
    plt.ylabel('features')

    # for streamlit pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    
    st.write("""
             ## Function and Usefulness 
             PCA is a popular dimensionality reduction technique used for analyzing and simplifying complex high-dimensional data. 
             The main function of this algorithm is to transform the original data into a new set of variables, 
             the principal components, which are linear combinations of the original variables. 
             These principal components retain as much information from the data as possible, 
             allowing redundant elements and noise to be removed.
             Finally, it helps significantly in data visualization while also improving the performance of machine learning algorithms 
             by reducing the number of dimensions.
             """)
    
# Function for t-SNE visualization
def visualize_tsne(data, labels_names):
    # t-SNE title
    st.write("## t-SNE Algorithm")
    st.write("### Plot:")
    # Perform t-SNE and fits dataset
    tsne = TSNE(n_components=2)
    tsne_result = tsne.fit_transform(data)
    
    # get unique labels names
    unique_labels_names = np.unique(labels_names)
    
    # create plt fig
    plt.figure(figsize=(8, 6))
        
    # Plots T-SNE results
    try:
        # if there are labels it plots the data with different colors
        
        # each label point gets a different color
        for label in unique_labels_names:
            plt.scatter(tsne_result[labels_names == label, 0], tsne_result[labels_names == label, 1], 
                        label=label, cmap='viridis')
            
        # Display labels in right corner
        plt.legend(title='Labels', loc='center left', bbox_to_anchor=(1, 0.5))
    except:
        # if there are no labels it plots the data with the same color
        plt.scatter(tsne_result[:,0], tsne_result[:,1], color='blue')
    
    # set title, x-label, y-label names
    plt.title('T-SNE Visualization')
    plt.xlabel('features')
    plt.ylabel('features')

    # for streamlit pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    st.write("""
             ### Function and Usefulness 
             t-SNE is very useful for users who wish to visualize high-dimensional data. 
             For images, text, or large datasets, t-SNE can reduce their dimensions to 2 or 3, 
             revealing hidden relationships, patterns, and clusters that are not apparent with other methods. 
             With its help, users can detect anomalies and identify groups with similar characteristics.
             In short, it is a very useful tool in modern data analysis and machine learning.
             """)
    


def Histogram_plot(data, dataset_name):
    # if Histogram Plot tab is select it plots a histogram
    st.write("## Histogram Graph")
    st.write("### Plot:")
    plt.figure(figsize=(10, 6))
    sns.histplot(data, x='value', hue=dataset_name, kde=True, multiple='stack')
    plt.title('Histogram of all columns')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend(title=dataset_name)
    st.pyplot()
    st.write("""
             ### Function and Usefulness 
             A histogram is a chart that shows the frequency of occurrence of different values in a dataset. 
             Each bar of the histogram corresponds to a range of values,
             while the height of the bar represents the number of observations falling within that range.
             """)


def Density_plot(data, dataset_name):
    # if Density Plot tab is select it plots a Density Plot
    st.write("## Density Graph")
    st.write("### Plot:")
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data, x='value', hue=dataset_name, shade=True)
    plt.title('Density Plot of all columns')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend(title=dataset_name)
    st.pyplot()
    st.write("""
             ### Function and Usefulness 
             Data density shows how frequently different values appear along a continuous variable, 
             providing a picture of the concentration or dispersion of the data. 
             In short, it shows how often data values occur along a continuous variable.
             """)
    
def Box_plot(data, dataset_name):
    # if Boxplot tab is select it plots a Boxplot
    st.write("## Boxplot Graph")
    st.write("### Plot:")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data, x=dataset_name, y='value')
    plt.title('Boxplot of all columns')
    plt.xlabel(dataset_name)
    plt.ylabel('Value')
    plt.xticks(rotation=45)  
    st.pyplot()
    st.write("""
             ### Function and Usefulness 
             A boxplot presents five key pieces of information for a dataset: 
                - Mean
                - First and Third Quartiles (which define the box limits)
                - Variance
                - Possible presence of extreme high values
             """)



# Main function to display the tab content
def Visualization_tab(data, dataset_name):
    
    # visualization tab title
    st.title('2D Visualization Tab')

    # Extract the labels by popping the last column
    labels = data.iloc[:, -1]
    # Extract features by dropping the last column
    features = data.iloc[:, :-1]
    # if the labels column is has any string then we encode this columns in numbers
    has_string = labels.dtype == 'object'
    if has_string:
        
        labels_encoded = labels.astype('category').cat.codes
        
        # we give to the encoded labels column name the labels column name
        labels_encoded.name = labels.name
        
        # we connect the encoded labels to the features dataset
        data = pd.concat([features, labels_encoded], axis=1)
    
    '''
        Data analysis - visualization tabs for users to choose from:
            - DRA: Dimensionality Reduction Algorithms (ex. PCA, T-SNE)
            - EDA: Exploratory Data Analysis (ex. histogram, density plot, boxplot)
    ''' 
    DRA, EDA = st.tabs(["Dimensionality Reduction Algorithms", "Exploratory Data Analysis"])
    
    with DRA:
        st.header("Select Dimensionality Reduction Algorithm (PCA, t-SNE)")
        PCA, TSNE = st.tabs(["PCA", "t-SNE"])
        with PCA:
            visualize_pca(data, labels)
        with TSNE:
            visualize_tsne(data, labels)
    
    with EDA:
        st.header('Exploratory Data Analysis')
        histogramplot, Densityplot, Boxplot = st.tabs(["Histogram", "Density", "Boxplot"])
        '''
        3 plots:
            - Histogram
            - Density plot
            - Boxplot
        '''
        # connects the dataset into a single column named 
        melted_data = data.melt(var_name=dataset_name)
        # Display exploratory data analysis
        with histogramplot:
            Histogram_plot(melted_data, dataset_name)
            
        with Densityplot:
            Density_plot(melted_data, dataset_name)
        
        with Boxplot:
            Box_plot(melted_data, dataset_name)