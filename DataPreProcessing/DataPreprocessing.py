import json
import pandas as pd
import numpy as np
from Data import load_data

from util.app_logger import AppLogger
from util.get_past_current_date import Date
from util.root import ProjectRoot
import os

project_root = ProjectRoot().get_project_root()
app_log = AppLogger("Data Preprocessing", os.path.join(project_root, 'Logs/DataPreprocessing.log'))
logger = app_log.set_handlers()

class data_preprocessing:
    """
            Name : data_preprocessing Class
            Module : DataPreprocessing
            Description : This class is to preprocess the data from database,
            i.e cleaning, preprocessing and analyzing data, these steps takes place
            in this class. This analyzed data can be used further for Visualisation

            Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
            Version : 1.0.0
            Revision : None

        """

    def __init__(self, file_path, year):
        """
            Name : data_preprocessing Class Constructor
            Module : DataPreprocessing
            Description : Initiates the instance variable which will
                          be used by the class
            Parameters:
                - file_path : This object fetches the path of data from directory.
                - year : This object takes year as a input.
                - loaded_data : This object loads the data returns the loaded data
            Returns : None
            Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
            Version : 1.0.0
            Revision : None

        """

        self.file_path = file_path
        self.year = year
        data = load_data.get_data(self.file_path)
        self.loaded_data = data.load_data()

    def extract_title(self):
        """
            Name : extract_title function
            Module : DataPreprocessing
            Description : This function alot the title to the chart according to the data.
            Parameters: None
            Returns : Title in string format
            Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
            Version : 1.0.0
            Revision : None

                """
        # if any("CPI" in self.file_path for i in self.file_path):
        #     title = "CPI(Consumer price index)"
        # elif any("Exchange rate" in self.file_path for i in self.file_path):
        #     title = "Exchange rate"
        # elif any("Exports Merchandise" in self.file_path for i in self.file_path):
        #     title = "Exports Merchandise"
        # logger.info("[Process 1 : extract_title has runned succesfully !]")
        # return title

    def fill_na_with_zero(self):
        """
            Name : fill_na_with_zero function
            Module : DataPreprocessing
            Description : This function fills the null values with zero in the data.
            Parameters: None
            Returns : Dataframe with zero null values.
            Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
            Version : 1.0.0
            Revision : None

        """

        filled_nan_values = self.loaded_data.fillna(0)
        logger.info("[Process 2 : fill_na_with_zero has runned succesfully !]")
        return filled_nan_values

    def drop_vacant_row(self):
        """
            Name : drop_vacant_row function
            Module : DataPreprocessing
            Description : This function drops the first vacant row (if present) from the data.
            Parameters: None
            Returns : Dataframe with no vacant rows .
            Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
            Version : 1.0.0
            Revision : None

        """
        try:
            cleaned_data = self.fill_na_with_zero()
            for i in cleaned_data.iloc[0]:
                if i == 0:
                    cleaned_data.drop([0], inplace=True)
                else:
                    pass
                break
            else:
                pass
            logger.info("[Process 3 : drop_vacant_row has runned succesfully !]")
            return cleaned_data
        except:
            logger.info("[Error E3 : There is an error in drop_vacant_row !]")

    def set_datetime_index(self):
        """
            Name : set_datetime_index function
            Module : DataPreprocessing
            Description : This function sets the "period" column to index and converting its datatype to datetime format.
            Parameters: None
            Returns : Dataframe with years as index.
            Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
            Version : 1.0.0
            Revision : None

        """
        try:
            clean_data = self.drop_vacant_row()
            date = clean_data.iloc[:, 0]
            date = pd.to_datetime(date, format='%Y')
            date = pd.DatetimeIndex(date).year
            date = pd.Series(date)

            # Setting 1st column as index(period)
            if clean_data.index.values[0] == 0:
                date.index =  np.arange(0, len(clean_data))
                clean_data.drop(columns=self.drop_vacant_row().columns[0], axis=1, inplace=True)

            else:
                date.index = np.arange(1, len(clean_data) + 1)
                clean_data.drop(columns=clean_data.columns[0], axis=1, inplace=True)

            set_data = pd.DataFrame(date).join(clean_data)
            set_data.set_index(set_data.columns[0], inplace=True)
            set_data.replace(to_replace=0, method="ffill", inplace=True)
            logger.info("[Process 4 : set_datetime_index has runned succesfully !]")
            return set_data
        except:
            logger.info("[Error E4 : There is an error in set_datetime_index !]", e)

    def Yoy_preprocessing(self):
        """
            Name : Yoy_preprocessing function
            Module : DataPreprocessing
            Description : This function does the Year to Year analysis of the data.
            Parameters: None
            Returns : A new dataframe of YOY analysis.
            Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
            Version : 1.0.0
            Revision : None

        """
        try:
            extract_col_one = self.drop_vacant_row().iloc[:, 0]

            pct_change_data = self.drop_vacant_row().iloc[0:, 1:].pct_change() * 100

            replacing_inf = pct_change_data.replace([np.inf, -np.inf], np.nan)
            filled_na = replacing_inf.fillna(0)

            df_chart1 = pd.DataFrame(extract_col_one).join(filled_na)
            df_chart1.rename(columns={df_chart1.columns[0]: 'Period'}, inplace=True)
            df_chart1["Period"] = pd.to_datetime(df_chart1['Period'], format='%Y')
            df_chart1['Period'] = pd.DatetimeIndex(df_chart1["Period"]).year
            logger.info("[Process 5 : Yoy_preprocessing has runned succesfully !]")
            return df_chart1
        except:
            logger.info("[Error E5 : Error in Yoy_preprocessing !]")

    def CAGR_preprocessing(self):
        """
           Name : CAGR_preprocessing function
           Module : DataPreprocessing
           Description : This function does the CAGR analysis of the data.
           Parameters: None
           Returns : A new dataframe of CAGR analysis.
           Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
           Version : 1.0.0
           Revision : None

       """
        try:

            country = self.set_datetime_index().columns
            time_period = [3, 5, 10, 15, 20, 25]  # length  = 6

            CAGR = []
            for T in time_period:
                for j in country:
                    country_data = self.set_datetime_index()[j]
                    start = country_data.index[-T]
                    end = country_data.index[-1]
                    formula_cagr =( ((country_data.loc[end] / country_data.loc[start]) ** (1 / T)) - 1 )
                    CAGR.append(formula_cagr)

            x = len(self.set_datetime_index().columns)

            three = CAGR[:x]
            five = CAGR[x:2 * x]
            ten = CAGR[2 * x:3 * x]
            fifteen = CAGR[3 * x:4 * x]
            twenty = CAGR[4 * x:5 * x]
            twentyfive = CAGR[5 * x:]

            processed_df = pd.DataFrame(
                {"Countries": country, "3 Yrs": three, "5 Yrs": five, "10 Yrs": ten, "15 Yrs": fifteen, "20 Yrs": twenty,
                 "25 Yrs": twentyfive})
            processed_df.set_index(processed_df.columns[0], inplace=True)

            #  transpose of df
            cagr_df = processed_df.T
            cagr_df.replace(to_replace=np.inf, value=0, inplace=True)
            #df_t.drop(df_t.columns[0],axis = 1,inplace = True)
            cagr_df.fillna(0, inplace=True)
            logger.info("[Process 6 : CAGR_preprocessing has runned succesfully !]")
            return cagr_df
        except:
            logger.info("[Error E6 : There is an error in CAGR_preprocessing !]")

    def monthly_preprocessing(self):
        """
           Name : monthly_preprocessing function
           Module : DataPreprocessing
           Description : This function does the preprocessing for monthly data.
           Parameters: None
           Returns : A new dataframe of preprocessed monthly data.
           Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
           Version : 1.0.0
           Revision : None

        """
        try:

            # loading the monthly_data
            monthly_data = pd.read_excel(self.file_path, sheet_name="monthly")
            unwanted_countries_EM = ["Developing Asia", "Developing Countries"
                , "East Asia & Pacific developing", "Europe & Central Asia developing"
                , "Middle Income Countries", "World (WBG members)"]
            unwanted_countries_ER = ["Angola", "Guinea", "Turkmenistan", "Timor-Leste"]

            # Data Preprocessing
            monthly_data.fillna(0, inplace=True)

            # for i in monthly_data.iloc[0]:
            #     if i == 0:
            #         monthly_data.drop([0],inplace = True)
            #     else:
            #         pass
            #     break
            # else:
            #     pass

            monthly_data.set_index(monthly_data.columns[0], inplace=True)

            if any("Export" in self.file_path for i in self.file_path):
                monthly_data.drop(unwanted_countries_EM, axis=1, inplace=True)
            elif any("Exchange" in self.file_path for i in self.file_path):
                monthly_data.drop(unwanted_countries_ER, axis=1, inplace=True)
                monthly_data.drop(["1988M12"], inplace=True)
            elif any("CPI" in self.file_path for i in self.file_path):
                monthly_data.drop(["1988M12"], inplace=True)

            monthly_data.replace(to_replace=0, method="ffill", inplace=True)

            # cleaned monthly_data
            # monthly_data

            # adding months column to the monthly_data
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

            if any("Export" in self.file_path for i in self.file_path):
                months = months * 28
                months = months[:-3]
            else:
                months = months * 30
                months = months[:-1]
            monthly_data.insert(0, "Months", months)

            # adding year column in the monthly_data
            a = np.arange(1989, 2019)
            years = (list(map(str, list(a))))
            all_years = []

            for i in years:
                Y = [i] * 12
                all_years.append(Y)

            # final list of all years together now ready to add it to the dataframe
            all_years_together = []
            for j in all_years:
                for k in j:
                    all_years_together.append(k)

            if any("Export" in self.file_path for i in self.file_path):
                all_years_together = all_years_together[24:-3]
            else:
                all_years_together = all_years_together[:-1]

            monthly_data.insert(0, "Year", all_years_together)

            monthly_data.reset_index(drop=True)
            monthly_data.set_index(["Months"], drop=True, inplace=True)
            monthly_data = monthly_data.loc[monthly_data['Year'] == str(self.year)]
            logger.info("[Process 7 : monthly_preprocessing has runned succesfully !]")
            return monthly_data

        except:
            logger.info("[Process 7 : monthly_preprocessing has runned succesfully !]")
