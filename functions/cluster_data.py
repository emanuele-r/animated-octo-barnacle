import numpy as np
import logging
from sklearn.cluster import AffinityPropagation
import matplotlib.pyplot as plt
import pandas as pd
from functions.control import datatype_controll


def _clustering_data(data: np.array):
    logging.info(f"{_clustering_data.__name__}Started")

#check if array has the right dimmension 
#and if the datatype is an numpy array
    datatype_controll(data)

    if data.ndim == 1:
        data = data.values.reshape(-1, 1)
        logging.info(f"Data has been reshape to data :{data.ndim}")
        try :
            clustering=AffinityPropagation(random_state=5, max_iter=1000, damping=0.9).fit(data)
            plt.title("Affinity Matrix Plot")
            plt.imshow(clustering.affinity_matrix_, cmap='viridis', interpolation='nearest')
            plt.show()
            # print(clustering.affinity_matrix_, clustering.labels_, clustering.cluster_centers_)
            return clustering.affinity_matrix_        
        except Exception as e :
            print(f'{e}')
            logging.error(f'{e}')
        logging.info(f' function {_clustering_data.__name__} completed')
    elif data.ndim == 2:
        try:
            logging.info(f'Data dimension : {data.ndim}')
            clustering=AffinityPropagation(random_state=5, max_iter=1000, damping=0.9).fit(data)
            plt.title("Affinity Matrix Plot")
            plt.imshow(clustering.affinity_matrix_, cmap='viridis', interpolation='nearest')
            plt.show()
            # print(clustering.affinity_matrix_, clustering.labels_, clustering.cluster_centers_)
            return clustering.affinity_matrix_        
        except Exception as e :
            print(f'{e}')
            logging.error(f'{e}')
    logging.warning(f'{e}')
    logging.info(f' function {_clustering_data.__name__} completed')

