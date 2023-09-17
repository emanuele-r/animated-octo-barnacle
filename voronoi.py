import numpy as np 
import random
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay, delaunay_plot_2d
import matplotlib.pyplot as plt 




def generate_data(gen_x):
    return gen_x



def rent_estimation(generate_data):
    rent_list=[]
    try:
        for x  in generate_data:
            rent=np.array([x*0.003, x*0.001])
            rent_list.append(rent)
            print(f'{rent}')
        return rent_list
    except Exception as e :
        print(f'ERROR : Could not Estimate Rent for this type of data -->{generate_data[0]}')
 
    
def graph_voronoi(data, sales, resindential_type, town):
    try:
        vor=Voronoi(data)
        voronoi_plot_2d(vor)
        plt.title(f'Voroid Regions, number of Coordinates{len(data)}')
        for i, (x,y) in enumerate(data):
            single_sale=sales[i]
            rent_est=rent_estimation([single_sale])
            plt.annotate(f'Town:{town[i]} | Residential Type: {resindential_type[i]} | Sales ; ${sales[i]} | Rent Esimation {rent_est[0]}', xy=(x,y), xytext=(0.001+x,y))
        plt.show()
    except Exception as e:
        print(f'An Error Occured :{e}')
    return 



def graph_delaunay(generate_data, text, residential_type, town):
    try:
        tri=Delaunay(generate_data)
        delaunay_plot_2d(tri)
        for i , (x, y ) in enumerate(generate_data):
            plt.annotate(f'{town[i]} -> {residential_type[i]} : $ {text[i]}', xy=(x,y), xytext=(x+0.05, y+0.05))
        plt.title("Delaunay")
        plt.show()
    except Exception as e :
        print(f'An Error Occured')
    
    return 


def graph_simple(generate_data, text, residential_type):
    for i, (x,y) in enumerate(generate_data):
        plt.scatter(x, y)
        plt.title(f'Simple Scatter Graph')
        plt.annotate(f' $ {text[i]}', xy=(x,y), xytext=(x,y))
        plt.annotate(f'{residential_type[i]}', xy=(x,y), xytext=(x+0.05, y+0.05))
        plt.legend(f'{text[i]}')
    plt.show()
    return