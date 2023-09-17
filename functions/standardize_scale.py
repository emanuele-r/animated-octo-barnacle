import logging
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from functions.control import datatype_controll


#Logging istance to check operations

logging.basicConfig(filename="tracked_action.log", level=logging.INFO, format='%(asctime)s %(message)s')


#standardize dataset


def standardize_scale(data):
    logging.info(f'{standardize_scale.__name__}--> Started')
    datatype_controll(data)
    if data.ndim == 1:
        data = data.values.reshape(-1, 1)
        logging.info(f"Data has been reshape to data :{data.ndim}")
        try :
            scaler=StandardScaler()
            scaled_data=scaler.fit_transform(data)
        except Exception as e :
            print(f'{e}')
            logging.error(f'{e}')
    elif data.ndim ==2:
        logging.info(f'Data dimension :{data.ndim}')
        scaler=StandardScaler()
        scaled_data=scaler.fit_transform(data)
    logging.info(f'{standardize_scale.__name__} --> Completed with an output [0] of {scaled_data[0]}')
    return scaled_data

















