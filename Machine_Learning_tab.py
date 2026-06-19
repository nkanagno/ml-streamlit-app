from libraries import *

'''
    Machine learning tab (Main Function)
'''

def Machine_Learning_tab(data):
    # Tab title
    st.title("Machine Learning Algorithms")
    # tab to select classifiers or clusters 
    Classifiers, Clusters = st.tabs(
    ['Classifiers', 'Clusters']
    )
    
    with Classifiers:
        classifiers(data)
    with Clusters:
        clusters(data)


'''
        Classifiers
'''

    
def classifiers(data):
    # algorithm type
    st.write("# Classifiers")
    
    # classifiers inputs
    st.write("### Support Vector Machines")
    
    c = st.number_input("Enter the regularization parameter for the Support Vector Machines:", min_value=0.01, value=0.01)
    
    st.write("### K-Nearest Neighbors")
    k_neighbors = st.number_input("Enter the k neighbors for the K-Nearest Neighbors:", min_value=1, value=3)
    
    
    
    # Create a button to start the analysis
    if st.button("Start Analysis",key="classifiers"):
        # Separate the features (K-1 columns) and the target (last column) from the data
        features = data.iloc[:, :-1]
        labels = data.iloc[:, -1]
        
        ## Classification accuracy scores
        svm_accuracy = run_support_vector_machines(features, labels, c)
        knn_accuracy = run_KNN(features, labels, k_neighbors)
        
        
        # format %
        svm_accuracy_per = svm_accuracy * 100
        knn_accuracy_per = knn_accuracy * 100
        
        
        # Evaluation Results in a dataframe:
        Eval_results = {"Classication Algorithm": ["Support Vector Machines","K-Nearest Neighbors"],
                               "Parameter": [f'{c}'+" (regularization parameter)",f'{k_neighbors}'+" (k-neighbors)"],
                               "Score": [f'{svm_accuracy:.4f}' ,f'{knn_accuracy:.4f}'],
                               "%": [f'{svm_accuracy_per:.2f}%',f'{knn_accuracy_per:.2f}%']
                               }
        
        # Display the evaluation results in a table
        st.write("Evaluation Results (Accuracy Score):")
        st.write(pd.DataFrame(Eval_results))
        best_accuracy, algorthm_name = best_acc_algorithm(Eval_results, 'Classication Algorithm')
        st.write("Recommended Algorithm: `" + algorthm_name + "`")
        st.write("Best Accuracy: `" + str(best_accuracy) + "`.")
        st.write("""
             #### SVM vs KNN
             SVM and KNN are two very useful classification algorithms, meaning they are used for training data that provide labels.
             However, there are cases where their accuracy and performance may differ depending on the type of data.
             
             ##### SVM usefulness 
             More specifically, in the Support Vector Machine (SVM) approach we find
             a boundary to separate data into two classes. The algorithm finds the widest possible margin
             (to maximize accuracy through the regularization parameter). Finally, the data should be normalized.

             
             ##### KNN usefulness
             KNN is a simple algorithm that classifies new data based on the similarity of its features with the features of the k nearest neighbors in the training data.
             More specifically, the parameter k defines how many neighbors are considered for this similarity, which can be measured based on distance.
             
             ##### When is each one more suitable?
             The SVM algorithm is more accurate for high-dimensional and sparse data, and is ideal for minimizing errors and avoiding overfitting,
             but it is quite difficult to implement because it requires tuning the regularization parameter to achieve optimal accuracy.
             
             However, KNN is easier to understand and implement, and is good at handling new data,
             but it is slower and struggles to produce good results on large datasets.
             """)


def run_support_vector_machines(X, y, c):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # train the svm model and return accuracy
    svm = SVC(C=c)
    svm.fit(X_train, y_train)       
    y_pred = svm.predict(X_test)    
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


def run_KNN(X, y, k_neighbors):
    # Split the data into training and testing sets (70% training, 30% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # train the K-NN model and return accuracy
    knn = KNeighborsClassifier(n_neighbors=k_neighbors)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


'''
        Clusters
'''
def clusters(data):
    # algorithm type
    st.write("# Clusters")
    
    # Clusters inputs
    st.write("### Agglomerative Hierarchical Clustering")
    n_clusters_agg_clust = st.number_input("Enter the number of clusters for Agglomerative Hierarchical Clustering:", min_value=2, value=2)
    
    st.write("### Affinity Propagation")
    similarity_between_data_points = st.number_input("Enter the bandwidth parameter for Affinity Propagation Clustering:", min_value=0.5, max_value=0.91, value=0.7)

    
    # Create a button to start the analysis
    if st.button("Start Analysis", key="clusters"):
        
        try:
            st.write("""
                 ```
                    WARNING:
                    the results may not be correct if your dataset already has labels
                    (ex. 0 or 1)
                 ```                   
                 """)
            # Clustering Silhouette Score
            agg_clust_labels, agg_clust_score = run_agglomerative_clustering(data, n_clusters_agg_clust)
            aff_prop_labels, aff_prop_score = run_affinity_propagation(data, similarity_between_data_points)
            
            # format %
            agg_clust_per = agg_clust_score * 100
            aff_prop_per  = aff_prop_score  * 100
            
            # Evaluation Results in a dataframe:
            Eval_results = {"Cluster Algorithm": ["Agglomerative Hierarchical Clustering","Affinity Propagation"],
                                "Parameter": [f'{n_clusters_agg_clust}'+" (Clusters)", f'{similarity_between_data_points:.2f}'+" (Damping)"],
                                "Score": [f'{agg_clust_score:.4f}' , f'{aff_prop_score:.4f}'],
                                "%": [f'{agg_clust_per:.2f}%', f'{aff_prop_per:.2f}%']
                                }
            
            # Display the evaluation results in a table
            st.write("Evaluation Results (Silhouette Score):")
            st.write(pd.DataFrame(Eval_results))
            best_accuracy, algorthm_name = best_acc_algorithm(Eval_results, 'Cluster Algorithm')
            st.write("Recommended Algorithm: `" + algorthm_name + "`")
            st.write("Best Accuracy: `" + str(best_accuracy) + "`.")
            st.write("""
                #### Agglomerative Hierarchical Clustering vs Affinity Propagation
                Agglomerative Hierarchical Clustering and Affinity Propagation are two very useful clustering algorithms,
                meaning they are used for training data that does not provide labels but generates them as output.
                However, there are cases where their accuracy and quality may differ depending on the type of data.
                
                ##### Agglomerative Hierarchical Clustering usefulness 
                More specifically, Agglomerative Hierarchical Clustering first computes all initial distances between data points in a matrix based on a hierarchy.
                Then, it merges the pair of clusters with the closest distance and updates the distance matrix.
                The algorithm repeats until it reaches the required number of clusters.
                

                ##### Affinity Propagation usefulness
                Affinity Propagation is based on the idea of message passing between data points to find cluster centers (exemplars).
                Initially, all data points send and receive messages about how suitable each point is to be a cluster center.
                These message exchanges continue, gradually updating preferences and responsibilities.
                Eventually, the process converges, determining which points become centers and which belong to each cluster.
                The algorithm repeats until a stable solution is reached, without requiring the number of clusters in advance.

                
                ##### When is each one more suitable?
                Agglomerative Hierarchical Clustering is simple and more effective when we know the number of clusters and when we have smaller datasets with well-separated clusters.
                However, it is not very efficient for very large datasets.
                
                On the other hand, Affinity Propagation is very useful when we do not know the number of clusters, and it is ideal for complex and large datasets,
                although it requires many computations due to message passing.
                """)
        except ValueError as e:
            # if it has strings in the labels, it shows a specific error message
            if str(e).startswith("could not convert string to float:"):
                st.error("An error occurred: your dataframe already has labels (strings)")
            else:
                raise e


def run_agglomerative_clustering(data, n_clusters):
    # train the agglomerative clustering model and return the predicted labels plus the silhouette_score
    agglomerative = AgglomerativeClustering(n_clusters=n_clusters)
    labels = agglomerative.fit_predict(data)
    score = silhouette_score(data, labels)
    return labels, score


def run_affinity_propagation(data, similarity_between_data_points):
    # train the affinity propagation model and return the predicted labels plus the silhouette_score
    affinity_propagation = AffinityPropagation(damping=similarity_between_data_points)
    affinity_propagation.fit(data)
    labels = affinity_propagation.labels_
    score = silhouette_score(data, labels)
    return labels, score




'''
    Gets the Evaluation results dataframe and what category is:
        - Classification Algorithm  
                    or 
        - Cluster Algorithm
    And returns the score and the name of the algorithm with the best accuracy score 
'''

def best_acc_algorithm(Eval_results, category):
    # From a dict into a pandas dataframe
    df = pd.DataFrame(Eval_results)     
    
    # get highest score index
    max_index = df['Score'].idxmax()    
    print(df['Score'])
    # locate the algorithm with the best accuracy and their accuracy
    best_accuracy  = df.loc[max_index, '%']
    algorithm_name = df.loc[max_index, category]
    return best_accuracy, algorithm_name