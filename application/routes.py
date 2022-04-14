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
#from load_data.database_import import MongoDb

from util.app_logger import  AppLogger

project_root = ProjectRoot().get_project_root()
app_log = AppLogger("routes", os.path.join(project_root, 'Logs/routes.log'))
logger = app_log.set_handlers()


# logger.info('ETL API Hit')
# etl = MongoDb()
# logger.info('Starting to Import Data')
# etl.import_to_csv()
# logger.info('All the data are fetched from Database and ready to be combined !')
#
#
# path = r"G:\Delloite Case Study Analysis\Deloitte-Case-Study-project-Analysis-master\Deloitte-Case-Study-project-Analysis-master\Data\RawDataset"
# extension = 'csv'
# all_filenames = [i for i in os.listdir(path)]
#
# CPI = etl.get_excel(path, "CPI", all_filenames)
# Exg = etl.get_excel(path, "Exchange Rate", all_filenames)
# Exp = etl.get_excel(path, "Export Merchandise", all_filenames)
# logger.info('All the data are fetched from Database in .csv and saved as .xlsx !')

@app.route('/', methods=['GET', "POST"])
def index():
    """
       Name : index function
       Module : routes
       Description : This function loads index.html page.
       Parameters: None
       Returns : This function returns the Home page tab of the Web app.
       Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
       Version : 1.0.0
       Revision : None

   """

    logger.info("[Process 2 : Index page loaded sucessfully!]")
    return render_template("index.html")

@app.route('/about1', methods=['GET', "POST"])
def about1():
    """
       Name : about1 function
       Module : routes
       Description : This function loads about1.html page.
       Parameters: None
       Returns : This function returns the About-us tab of the Web app.
       Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
       Version : 1.0.0
       Revision : None

   """
    logger.info("[Process 3 : About us page sucessfully!]")
    return render_template("about1.html")

@app.route("/Exp_mrch", methods=["GET", "POST"])
def Exp_mrch():
    """
       Name : Exp_mrch function
       Module : routes
       Description : This function loads Exp_mrch.html page.
       Parameters: None
       Returns : This function returns the Export Merchandise tab of the Web app.
       Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
       Version : 1.0.0
       Revision : None

    """

    data = "Data/RawDataset/Exports Merchandise.xlsx"
    year = 2017
    #data = r"{}\Data\RawDataset\Exports Merchandise.xlsx".format(project_root)

    try:

        from_charts = Chart.get_chart(data,year)

        fig = from_charts.get_monthly_post_chart()
        graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        fig1 = from_charts.get_yoy_dropdown_chart()
        graph2JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

        fig1 = from_charts.get_yoy_multipleselect_chart()
        graph3JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

        fig2 = from_charts.get_cagr_dropdown_chart()
        graph4JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

        fig3 = from_charts.get_cagr_years_chart()
        graph5JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

        fig4 = from_charts.get_cagr_grouped_chart()
        graph6JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    except:
        logger.info("[Error : Error in fetching Export_Merchandise charts!]")

    try:
        
        if request.method == "POST":
            year = request.form["multiple"]
            logger.info("Post request fetch for year{}".format(year))
            #fig5 = get_montly_chart(montly_chart(data, year))
            monthly_from_chart = Chart.get_chart(data, year)
            fig = monthly_from_chart.get_monthly_post_chart()
            fig.update_layout(
                title='Monthly Analysis of year'+" "+ year,
                title_x=0.45,
                title_y=0.95,
                title_font_family="Balto",
                title_font_size=18,
                xaxis_title="years",
                paper_bgcolor='white',
                # plot_bgcolor='black',

                font_color='black',
                yaxis_title="CAGR"
            )

            # fig3.update_layout(title_x=0.5, plot_bgcolor= "#c1efde", paper_bgcolor= "#c1efde")
            # fig2.update_layout(title_x=0.5, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
            #fig5.update_layout(height=500, width=900)
            graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            logger.info("Post request executed & Export Merchandise.html loaded Successfully.")
            return render_template("Exp_mrch.html", title="Export merchandise", graph1JSON=graph1JSON, graph2JSON=graph2JSON,
                                   graph3JSON=graph3JSON, graph4JSON=graph4JSON, graph5JSON=graph5JSON,
                                   graph6JSON=graph6JSON)

        else:
            try:
                return render_template("Exp_mrch.html" , title="Export merchandise" , graph1JSON = graph1JSON , graph2JSON = graph2JSON,
                                   graph3JSON = graph3JSON, graph4JSON = graph4JSON , graph5JSON = graph5JSON,
                                   graph6JSON = graph6JSON)
            except:
                logger.info("[Error : Error in Export_Merchandise route!]")
    except:
        logger.info("[Error : Error in Post request in Export_Merchandise route.]")

        

@app.route("/Exchange_rate", methods=["GET", "POST"])
def Exchange_rate():
    """
       Name : Exchange_rate function
       Module : routes
       Description : This function loads Exchange_rate.html page.
       Parameters: None
       Returns : This function returns the Exchange Rate tab of the Web app.
       Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
       Version : 1.0.0
       Revision : None

    """
    
    
    data = "Data/RawDataset/Exchange rate.xlsx"
    year = 2017
    
    #data = r"{}\Data\RawDataset\Exports Merchandise.xlsx".format(project_root)

    try:

        from_charts = Chart.get_chart(data,year)

        fig = from_charts.get_monthly_post_chart()
        graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        fig1 = from_charts.get_yoy_dropdown_chart()
        graph2JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

        fig1 = from_charts.get_yoy_multipleselect_chart()
        graph3JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

        fig2 = from_charts.get_cagr_dropdown_chart()
        graph4JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

        fig3 = from_charts.get_cagr_years_chart()
        graph5JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

        fig4 = from_charts.get_cagr_grouped_chart()
        graph6JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    except:
        logger.info("[Error : Error in fetching Export_Merchandise charts!]")

    try:
        
        if request.method == "POST":
            year = request.form["multiple"]
            logger.info("Post request fetch for year{}".format(year))
            #fig5 = get_montly_chart(montly_chart(data, year))
            monthly_from_chart = Chart.get_chart(data, year)
            fig = monthly_from_chart.get_monthly_post_chart()
            fig.update_layout(
                title='Monthly Analysis of year'+" "+ year,
                title_x=0.45,
                title_y=0.95,
                title_font_family="Balto",
                title_font_size=18,
                xaxis_title="years",
                paper_bgcolor='white',
                # plot_bgcolor='black',

                font_color='black',
                yaxis_title="CAGR"
            )

            # fig3.update_layout(title_x=0.5, plot_bgcolor= "#c1efde", paper_bgcolor= "#c1efde")
            # fig2.update_layout(title_x=0.5, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
            #fig5.update_layout(height=500, width=900)
            graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            logger.info("Post request executed & Export Merchandise.html loaded Successfully.")
            return render_template("Exchange_rate.html", title="Exchange Rate", graph1JSON=graph1JSON, graph2JSON=graph2JSON,
                                   graph3JSON=graph3JSON, graph4JSON=graph4JSON, graph5JSON=graph5JSON,
                                   graph6JSON=graph6JSON)

        else:
            try:
                return render_template("Exchange_rate.html" , title="Exchange Rate" , graph1JSON = graph1JSON , graph2JSON = graph2JSON,
                                   graph3JSON = graph3JSON, graph4JSON = graph4JSON , graph5JSON = graph5JSON,
                                   graph6JSON = graph6JSON)
            except:
                logger.info("[Error : Error in Exchange Rate route!]")
    except:
        logger.info("[Error : Error in Post request in Exchange Rate route.]")
   
@app.route("/CPI", methods=["GET", "POST"])
def CPI():
    """
       Name : CPI function
       Module : routes
       Description : This function loads CPI.html page.
       Parameters: None
       Returns : This function returns the CPI tab of the Web app.
       Written By : Abhishek Mestry ,Ninad Kadam ,Viresh Dhuri
       Version : 1.0.0
       Revision : None

    """
    data = "Data/RawDataset/CPI Data.xlsx"
    year = 2017
    try:

        from_charts = Chart.get_chart(data, year)
        fig = from_charts.get_monthly_post_chart()
        #fig = get_montly_chart(montly_chart(data, 2013))
        # fig = from_charts.get_monthly_chart()
        graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        fig1 = from_charts.get_yoy_dropdown_chart()
        graph2JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

        fig1 = from_charts.get_yoy_multipleselect_chart()
        graph3JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

        fig2 = from_charts.get_cagr_dropdown_chart()
        graph4JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

        fig3 = from_charts.get_cagr_years_chart()
        graph5JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

        fig4 = from_charts.get_cagr_grouped_chart()
        graph6JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    except:
        logger.info("[Error : Error in fetching CPI charts!]")

    try:
        if request.method == "POST":
            year = request.form["multiple"]
            logger.info("Post request fetch for year{}".format(year))
            # fig5 = get_montly_chart(montly_chart(data, year))
            from_charts = Chart.get_chart(data, year)
            fig = from_charts.get_monthly_post_chart()
            fig.update_layout(
                title='Monthly Analysis of year' + " " + year,
                title_x=0.45,
                title_y=0.95,
                title_font_family="Balto",
                title_font_size=18,
                xaxis_title="years",
                paper_bgcolor='white',
                # plot_bgcolor='black',

                font_color='black',
                yaxis_title="CAGR"
            )

            # fig3.update_layout(title_x=0.5, plot_bgcolor= "#c1efde", paper_bgcolor= "#c1efde")
            # fig2.update_layout(title_x=0.5, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
            # fig5.update_layout(height=500, width=900)
            graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            logger.info("[Process 6 : CPI.html loaded sucessfully!]")
            return render_template("CPI.html", title="Consumer Price Index(CPI)", graph1JSON=graph1JSON,
                                   graph2JSON=graph2JSON,
                                   graph3JSON=graph3JSON, graph4JSON=graph4JSON, graph5JSON=graph5JSON,
                                   graph6JSON=graph6JSON)
        else:
            try:
                logger.info("[Process 6 : CPI.html page loaded sucessfully!]")
                return render_template("CPI.html", title="Consumer Price Index(CPI)", graph1JSON=graph1JSON,
                                       graph2JSON=graph2JSON,
                                       graph3JSON=graph3JSON, graph4JSON=graph4JSON, graph5JSON=graph5JSON,
                                       graph6JSON=graph6JSON)
            except:
                  logger.info("[Error E6 : There is an error in CPI.html !]")
    except:
        logger.info("[Error : Error in Post request in CPI   route.]")
        
