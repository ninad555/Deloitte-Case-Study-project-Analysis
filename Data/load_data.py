import pandas as pd
from util.app_logger import AppLogger
from util.get_past_current_date import Date
from util.root import ProjectRoot
import os

project_root = ProjectRoot().get_project_root()
app_log = AppLogger("load_data", os.path.join(project_root, 'Logs/load_data.log'))
logger = app_log.set_handlers()

class get_data:

    def __init__(self, file_path):

        """
                Name : Get Data Class
                Module : load_data
                Description : It loads the required excel data .
                Parameters:
                    - file_path : Excel file path.
                Returns : None
                Written By : Ninad
                Version : 1.0.0
                Revision : None

        """
        self.file_path = file_path

    def load_data(self):
        """
                        Name : load_data function
                        Module : load_data
                        Description : It loads the required excel data for given excel file
                                     path.
                        Parameters:
                            - file_path : Excel file path.
                        Returns : None
                        Written By : Ninad
                        Version : 1.0.0
                        Revision : None

        """
        try:
            loaded_data = pd.read_excel(self.file_path)
            logger.info("[Process 1 : load_data has runned succesfully !]")
            return loaded_data
        except:
            logger.info("[Error 1 : There is an error in load_data !]")

