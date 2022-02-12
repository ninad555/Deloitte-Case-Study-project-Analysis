from application import app
from flask import render_template , url_for
import pandas as pd
import json
import os
import plotly
import plotly.express as px
from flask import Flask, render_template, request,url_for
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from Dashboard import Chart
import json
import plotly
from util.root import ProjectRoot
from load_data.database_import import MongoDb
import os


from util.app_logger import AppLogger

#
project_root = ProjectRoot().get_project_root()
app_log = AppLogger("test", os.path.join(project_root, 'Logs/test.log'))
logger = app_log.set_handlers()
# app_log = AppLogger("routes", os.path.join(project_root, 'Logs/routes.log'))  # adding logger
# logger = app_log.set_handlers()
#
# logger.info('ETL API Hit')
# etl = MongoDb()
# logger.info('Starting to Import Data')
# etl.import_to_csv()
# logger.info('All the data are fetched from Database and ready to be combined !')
yearly_data = os.path.join(project_root, "Data\RawDataset\Export Merchandise Yearly.csv")
monthly_data_path = os.path.join(project_root, "Data\RawDataset\Export Merchandise Monthly.csv")
logger.info("checkpoint")
def funct():
    try:
        file_path="Data/RawDataset/Export Merchandise Monthly.csv"

        monthly_data = pd.read_csv(monthly_data_path)


        #
        year = 2000
        #
        # from_charts = Chart.get_chart(yearly_data, year)
        #pmonthly_from_charts = Chart.get_chart(monthly_data, year)

        #print(monthly_from_charts)


        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        if any("Export" in file_path for i in file_path):
            months = months * 28
            months = months[:-3]
        else:
            months = months * 30
            months = months[:-1]

        monthly_data.insert(0, "Months", months)
        logger.info("reached inside fuctn")
    except:
        logger.info("kfsgi")
    else:
        print(monthly_data.head(10))
        logger.info("success!")



