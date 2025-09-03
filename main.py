from sensor.exception import sensorException
from sensor.logger import logging  

import sys 
import os
def test_exception():
    try:
       logging.info("xxxxxxxxxxxxxxxxxxxxxxx")
       a=1/0
    except Exception as e:
        raise sensorException(e,sys)
            

if __name__=="__main__":
    try:
        test_exception()
    
    except Exception as e:
        print( e)
