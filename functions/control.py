import logging
import numpy as np 
import pandas as pd 


def datatype_controll(data: any ):
    logging.info(f'{datatype_controll.__name__} --> Started')
    if isinstance(data, type(np.array) or type(pd.Series)):
        try :
            logging.info(f"Data type {type(data)} is correct as expected ")
            return data if isinstance(data, type(np.array)) else data.to_numpy()
       
        except Exception as e :
            logging.error(f'{e}')
    
    logging.info(f'{datatype_controll.__name__} --> Completed')       
   
