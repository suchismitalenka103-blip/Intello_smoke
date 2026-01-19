import inspect
import logging


class BaseClass:
    def getLogger(self):
        
        loggername = inspect.stack()[1][3]  # This is print the testcase name from where the class file is called
        # _name_ will print the test case name in the log
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # file handler object
        logger.setLevel(logging.DEBUG)
        return logger