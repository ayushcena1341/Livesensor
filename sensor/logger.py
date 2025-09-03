import logging
import os
import sys
from datetime import datetime

logfile=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"


logpath=os.path.join(os.getcwd(),"logs", f"logfile {logfile}")

os.makedirs(logpath,exist_ok=True)
LOG_FILE_PATH=os.path.join(logpath,logfile)


logging.basicConfig (
    filename= LOG_FILE_PATH,
    
    format= '[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s' ,
    level=logging.INFO
)