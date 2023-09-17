import pandas as pd 
import numpy as np
from functions.voronoi import graph_voronoi, generate_data, graph_delaunay, graph_simple, rent_estimation
from functions.standardize_scale import standardize_scale
from functions.cluster_data import _clustering_data

pf=pd.read_csv("data_folder/edited_data.csv")
# oo=pd.read_csv("real.csv", low_memory=False).dropna()





sample_point=np.array([pf[["Longitude", "Latitude"]]])

sample_point=sample_point[0]

# divide_data(pf["Sale Amount"])


# _clustering_data(pf["Sale Amount"])




_clustering_data(standardize_scale(pf["Sale Amount"]))

# print(sample_point)


# print(pf["Sale Amount"])


# graph_voronoi(sample_point, pf["Sale Amount"], pf["Residential Type"], pf["Town"])


# graph_delaunay(generate_data(sample_point[0]), pf["Sale Amount"], pf["Residential Type"])


# graph_simple(sample_point[0], pf["Sale Amount"], pf["Residential Type"])    
