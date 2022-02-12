from Dashboard import  Visualization

from DataPreProcessing import  DataPreprocessing

from util.app_logger import AppLogger
from util.get_past_current_date import Date
from util.root import ProjectRoot
import os

project_root = ProjectRoot().get_project_root()
app_log = AppLogger("Chart", os.path.join(project_root, 'Logs/Chart.log'))
logger = app_log.set_handlers()

class get_chart:
    """
            Name : get_chart Class
            Module : Chart
            Description : This class is to get the all charts together which can passed further
            to the respective web pages.
            Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
            Version : 1.0.0
            Revision : None

    """

    def __init__(self, data , year):
        """
                Name : get_chart Class Constructor
                Module : Chart
                Description : This function initiates the instance variables which will
                          be used by the class
                Parameters :
                        - data : This object stores the data and passes to the respective functions.
                        - year : The object stores the year (string) and passes to the respective function.
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """

        self.data = data
        self.year = year
        pre = DataPreprocessing.data_preprocessing(self.data, self.year)

        self.to_chart_monthly = pre.monthly_preprocessing()
        self.get_monthly_chart = Visualization.Plotly_charts(self.to_chart_monthly)

        self.to_chart_yoy = pre.Yoy_preprocessing()
        self.get_yoy_plot = Visualization.Plotly_charts(self.to_chart_yoy)

        self.to_chart_cagr = pre.CAGR_preprocessing()
        self.get_cagr_plot = Visualization.Plotly_charts(self.to_chart_cagr)

    def get_yoy_dropdown_chart(self):
        """
               Name : get_yoy_dropdown_chart function
               Module : Chart
               Description : This function returns the dropdown chart for year to year analysis.
               Parameters : None
               Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
               Version : 1.0.0
               Revision : None

        """
        #get_plot = Visualization.Plotly_charts(self.chart_data)
        yoy_dropdown_chart = self.get_yoy_plot.YoY_dropdown_chart()
        logger.info("[Process 1 : get_yoy_dropdown_chart has runned successfully]")
        return yoy_dropdown_chart

    def get_yoy_multipleselect_chart(self):
        """
               Name : get_yoy_multipleselect_chart function
               Module : Chart
               Description : This function returns the multiselect chart for year to year analysis.
               Parameters : None
               Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
               Version : 1.0.0
               Revision : None

        """
        #get_plot1 = Visualization.Plotly_charts(self.chart_data)
        yoy_multiselect_chart = self.get_yoy_plot.YoY_mutipleselect_chart()
        logger.info("[Process 2 : get_yoy_multipleselect_chart has runned successfully]")
        return yoy_multiselect_chart

    def get_cagr_dropdown_chart(self):
        """
               Name : get_cagr_dropdown_chart function
               Module : Chart
               Description : This function returns the dropdown chart for CAGR analysis.
               Parameters : None
               Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
               Version : 1.0.0
               Revision : None

        """
        #get_plot = Visualization.Plotly_charts(self.chart_data)
        cagr_dropdown_chart = self.get_cagr_plot.cagr_dropdown_chart()
        logger.info("[Process 3 : get_cagr_dropdown_chart has runned successfully]")
        return cagr_dropdown_chart

    def get_cagr_years_chart(self):
        """
               Name : get_cagr_years_chart function
               Module : Chart
               Description : This function returns the CAGR charts for years.
               Parameters : None
               Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
               Version : 1.0.0
               Revision : None

        """
        #get_plot1 = Visualization.Plotly_charts(self.chart_data)
        cagr_years_chart = self.get_cagr_plot.cagr_all_years_chart()
        logger.info("[Process 4 : get_cagr_years_chart has runned successfully]")
        return cagr_years_chart


    def get_cagr_grouped_chart(self):
        """
               Name : get_cagr_grouped_chart function
               Module : Chart
               Description : This function returns the grouped chart graph for CAGR analysis.
               Parameters : None
               Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
               Version : 1.0.0
               Revision : None

        """
        #get_plot1 = Visualization.Plotly_charts(self.chart_data)
        cagr_grouped_chart = self.get_cagr_plot.cagr_grouped_countries()
        logger.info("[Process 5 : get_cagr_grouped_chart has runned successfully]")
        return cagr_grouped_chart   

    def get_monthly_post_chart(self):
        """
               Name : get_monthly_post_chart function
               Module : Chart
               Description : This function returns the monthly analysis chart.
               Parameters : None
               Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
               Version : 1.0.0
               Revision : None

        """
        #get_plot1 = Visualization.Plotly_charts(self.chart_data)
        monthly_chart = self.get_monthly_chart.Plot_monthly_chart()
        logger.info("[Process 6 : get_monthly_post_chart has runned successfully]")
        return monthly_chart






