import codecs
import csv
import os
import shutil
import pymongo
import pandas as pd
import re

from util.app_logger import AppLogger
from util.root import ProjectRoot

class MongoDb:
    """
          Name : MongoDb Class
          Module : database_import
          Description : This class is to fetch the data from
                        the mongodb database where all the data
                        from the sensors are stored.

          Written By : Ninad Kadam.
          Version : 1.0.0
          Revision : None

      """

    def __init__(self):
        """
                        Name : MongoDb Class Constructor
                        Module : database_import
                        Description : Initiates the instance variable which will
                                      be used by the class
                        Parameters:
                            - date : Create date class object to fetch present and past date
                            - project_root : Project Root Directory Object to get parent directory
                            - logger : Logger Object to log the details
                            - server_url : MongoDb Database URL
                            - db : MongoDB Database Name
                            - collections : Create the collection name
                            - csv_path : Raw Dataset path
                        Returns : None
                        Written By : Ninad Kadam.
                        Version : 1.0.0
                        Revision : None

        """
        #self.date = Date()
        self.project_root = ProjectRoot().get_project_root()
        app_log = AppLogger("Database Import", os.path.join(self.project_root, 'Logs/ETL.log'))
        self.logger = app_log.set_handlers()
        # self.server_url = "mongodb+srv://m001-student:m001-mongodb-basics@esa.gnknw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.server_url = "mongodb://localhost:27017/"
        self.db = 'Database_BI'
        self.collections = ['Export Merchandise Monthly', 'Export Merchandise Yearly', 'Exchange Rate Monthly', 'CPI Yearly', 'Exchange Rate Yearly', 'CPI Monthly']
        self.csv_path = "Data/RawDataset"

    def connect_to_server(self) -> object:
        """
                        Name : connect_to_server function
                        Module : database_import
                        Description : Create connection to database
                        Parameters: None
                        Returns : Database connection object
                            - db  : type(Mongodb Object)
                            - on failure : Raise Exceptions
                        Written By : Ninad Kadam.
                        Version : 1.0.0
                        Revision : None

        """

        try:
            client = pymongo.MongoClient(self.server_url)
            self.logger.info("Sever Connected !")
            try:
                db = client[self.db]
                return db
            except ConnectionError:
                self.logger.exception("Cant not connect to db !")
        except ConnectionError:
            self.logger.exception("Can not connect to server!")
        except Exception as e:
            self.logger.exception(e)

    def import_to_csv(self):
        """
                                Name : import_to_csv function
                                Module : database_import
                                Description : Fetch all the data from database and store
                                              collection wise csv
                                Parameters: None
                                Returns : Collection Wise Csv
                                    - sensor.csv : type(Mongodb Object)
                                    - on failure : Raise Exceptions
                                Written By : Ninad Kadam.
                                Version : 1.0.0
                                Revision : None

        """

        # checking whether the folder for current data is present or not
        try:
            if not os.path.exists(self.csv_path):
                # if the demo_folder directory is not present
                # then create it.
                os.makedirs(self.csv_path)
            # if project root is present the change the directory to Data/RawDataset
            # if os.path.isdir(os.path.join(self.project_root, self.csv_path)):
            #     os.chdir(os.path.join(self.project_root, self.csv_path))
            # else:
            #     os.mkdir(os.path.join(self.project_root, self.csv_path, self.date.today_date()))
            #     os.chdir(os.path.join(self.project_root, self.csv_path, self.date.today_date()))
        except FileNotFoundError:
            self.logger.exception("Raw Dataset Folder not present")
        except Exception as e:
            self.logger.exception(e)

        # connecting to the server and then saving all the sensors data in the individual csv

        db = self.connect_to_server()

        try:

            for _, data in enumerate(self.collections):
                cursor = db[data].find({})
                print(cursor)
                file_name = data + ".csv"
                print(file_name)
                loaded_data = list(cursor)
                df = pd.DataFrame(loaded_data)
                df.drop(["_id"], axis=1, inplace=True)
                df.to_csv(self.csv_path + "/" + file_name, index=False)

                self.logger.info("{}.csv file created".format(data))
        except Exception as e:
                self.logger.exception(e)
        except Exception as e:
            self.logger.exception(e)


    def get_excel(self, path, sub_string, file_names, sheet_name1="Yearly", sheet_name2="Monthly"):
        """
                                        Name : import_to_csv function
                                        Module : database_import
                                        Description : Fetch all the data in .csv  and store
                                                      it as .xlsx
                                        Parameters: None
                                        Returns : Collection Wise Csv
                                            - sensor.csv : type(Mongodb Object)
                                            - on failure : Raise Exceptions
                                        Written By : Ninad kadam
                                        Version : 1.0.0
                                        Revision : None

        """
        comp_list = [name for name in file_names if re.search(sub_string, name)]
        df_1 = pd.read_csv(path + "/" + comp_list[1])
        df_2 = pd.read_csv(path + "/" + comp_list[0])
        op_path = path +"/" + sub_string + '.xlsx'
        with pd.ExcelWriter(op_path, engine='xlsxwriter') as writer:  # doctest: +SKIP
            df_1.to_excel(writer, sheet_name=sheet_name1, index=False)
            df_2.to_excel(writer, sheet_name=sheet_name2, index=False)

