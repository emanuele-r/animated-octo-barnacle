import logging
import numpy as np



#function to split a dataset (if Array) of data
#in Test data and Train data

def divide_data(data: np.array):
    logging.info("Divide data Started")
    # Control if data is an array type of object
    try:
        if isinstance(data, type(np.array)):
            count=len(data)
            split_index=count//2
            x_train=data[:split_index]
            x_test=data[split_index:]
            # print(f'Test data :{x_test} values :{len(x_test)}')
            # print(f'Train data :{x_train} values :{len(x_train)}')
            logging.info(f"Data divided successfully, dimension {len(x_train), len(x_test)} ")
            return x_train, x_test        
        else:
            # Convert non-array data to a NumPy array
            data_array = np.array(data) 
            count = len(data_array)
            x_train = np.array(data_array[:count // 2])
            x_test = np.array(data_array[count // 2:])
            # print(f'Test Data: {x_test} , values :{len(x_test)} , type :{type(x_train)}')
            # print(f'Train Data: {x_train}, values :{len(x_train)}, type: {type(x_train)}')
            logging.info(f"Data divided successfully, dimension {len(x_train), len(x_test)} ")
        return x_train, x_test
    except Exception as e:
           print(f"ERROR: {e}")
    logging.error(f'Error in dividing data{e}')
    logging.info("function perfomed correctly")
    return None, None
