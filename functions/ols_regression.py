import statsmodels.api as sm
from statsmodels.api import OLS 
from functions.dividedata import divide_data
import logging
import os 

def ols_regression(data, output_filename="output_file/OLS Regression Results.txt"):
    logging.info(f'{ols_regression.__name__} --> Started ')
    olsres=None
    try :
        
        if not os.path.exists("output_file"):
            os.mkdir("output_file")
        
        print(f'"output_file" --> Completed')
        
        x_train , x_test= divide_data(data=data)
        
        olsmod=sm.OLS(x_test, x_train)
        olsres=olsmod.fit()
        # print(olsres.summary())
        logging.info(f'{olsres.summary()}')
        
        
        
        with open(output_filename, 'w') as file:
            file.write(str(olsres.summary()))

        logging.info(
            f'Saved OLS summary to {os.path.join("output_file", output_filename)}')
        
    except Exception as e :
        print(f'{e}')
        logging.error(f'{e}')
    return olsres, print(f'{ols_regression.__name__} --> Completed')
    
