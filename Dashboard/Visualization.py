import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from DataPreProcessing import  DataPreprocessing

from util.app_logger import AppLogger
from util.get_past_current_date import Date
from util.root import ProjectRoot
import os

project_root = ProjectRoot().get_project_root()
app_log = AppLogger("Visualization", os.path.join(project_root, 'Logs/Visualization.log'))
logger = app_log.set_handlers()

class Plotly_charts:
    """
            Name : Plotly_charts Class
            Module : Chart
            Description : This class creates all the charts which can passed further to the get_Chart class.
            Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
            Version : 1.0.0
            Revision : None

    """

    def __init__(self, data):
        """
                Name : Plotly_charts Class Constructor
                Module : Visualization
                Description : This function initiates the instance variables which will
                          be used by the class
                Parameters :
                        - data : This object stores the data and passes to the respective functions.
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """

        self.data = data

    def YoY_dropdown_chart(self):
        """
                Name : YoY_dropdown_chart function
                Module : Visualization
                Description : This function creates the Get YoY chart for any selected country in
                 the dropdown along with a slicers & buttons for years for the respective data.
                Parameters : None
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """
        try:
            buttons = []
            i = 0

            fig3 = go.Figure()

            country_list = list(self.data.columns[1:])
            # print(country_list)

            for country in country_list:
                fig3.add_trace(
                    go.Scatter(
                        x=self.data['Period'],
                        y=self.data[country],
                        name=country,
                        visible=(i == 0),

                        showlegend=False
                    )
                )

            for country in country_list:
                args = [False] * len(country_list)
                args[i] = True

                # create a button object for the country we are on
                button = dict(label=country,
                              method="update",
                              args=[{"visible": args}])

                # add the button to our list of buttons
                buttons.append(button)

                # i is an iterable used to tell our "args" list which value to set to True
                i += 1

            fig3.update_layout(updatemenus=[dict(active=0,
                                                 type="dropdown",
                                                 buttons=buttons,

                                                 x=0.646,
                                                 y=1.0,
                                                 xanchor='left',
                                                 yanchor='bottom'

                                                 ),
                                            ])

            # Add range slider
            fig3.update_layout(
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                 label="1y",
                                 step="year",
                                 stepmode="todate"),
                            dict(count=3,
                                 label="3y",
                                 step="year",
                                 stepmode="backward"),
                            dict(count=5,
                                 label="5y",
                                 step="year",
                                 stepmode="backward"),
                            dict(count=10,
                                 label="10y",
                                 step="year",
                                 stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(
                        visible=True
                    ),
                    type="date"
                ),
                annotations=[
                    dict(text="",
                         showarrow=False,
                         x=0.57,
                         xref="paper",
                         y=1.1,
                         yref="paper",
                         align="left")],
                title="Year-To-Year Analysis",
                title_x=0.4,
                title_y=0.95,
                xaxis_title="Years",
                yaxis_title="Rate of change",
                title_font_family="Balto",
                title_font_size=25,
                plot_bgcolor='white',

                font_color='black'
            )

            # to make bg transperent
            fig3.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                # paper_bgcolor= 'rgba(0, 0, 0, 0)’
            )

            # to change colour of gird lines
            fig3.update_yaxes(showgrid=False, gridwidth=1, gridcolor='black')
            fig3.update_xaxes(showgrid=False, gridwidth=1, gridcolor='black')
        except:
            logger.info("[Error V1 : There is an error in YoY_dropdown_chart !]")
        else:
            return fig3
        logger.info("[Process 1 : YoY_dropdown_chart has runned sucessfully !]")


    def YoY_mutipleselect_chart(self):
        """
                Name : YoY_mutipleselect_chart function
                Module : Visualization
                Description : This function creates YoY chart for multiple countries selected in the legend
                 along with a slicers & buttons for years for the respective data.
                Parameters : None
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """
        try:
            fig3 = go.Figure()

            country_list = list(self.data.columns[1:])
            # print(country_list)

            for country in country_list:
                fig3.add_trace(
                    go.Scatter(
                        x=self.data['Period'],
                        y=self.data[country],
                        name=country,
                        # visible = (i==0),
                        showlegend=True
                    )
                )

            # Add range slider
            fig3.update_layout(
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                 label="1y",
                                 step="year",
                                 stepmode="todate"),
                            dict(count=3,
                                 label="3y",
                                 step="year",
                                 stepmode="backward"),
                            dict(count=5,
                                 label="5y",
                                 step="year",
                                 stepmode="backward"),
                            dict(count=10,
                                 label="10y",
                                 step="year",
                                 stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(
                        visible=True
                    ),
                    type="date"
                ),

                title="Year-To-Year Analysis",
                title_x=0.49,
                title_y=0.95,
                legend_title="Choose countries",
                title_font_family="Balto",
                title_font_size=25,
                xaxis_title="Years",
                yaxis_title="Rate of change"
            ),

            # to make bg transperent
            fig3.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                # paper_bgcolor= 'rgba(0, 0, 0, 0)’
            )

            fig3.update_yaxes(showgrid=False, gridwidth=1, gridcolor='black')
            fig3.update_xaxes(showgrid=False, gridwidth=1, gridcolor='black')
        except:
            logger.info("[Process 2 : YoY_mutipleselect_chart has runned successfully !]")
        else:
            return fig3
        logger.info("[Process 2 : YoY_mutipleselect_chart has runned successfully !]")

    def cagr_dropdown_chart(self):
        """
                Name : cagr_dropdown_chart function
                Module : Visualization
                Description : This function creates the CAGR chart for selected country for different number
                of years for the respective data.
                Parameters : None
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """
        try:
            fig = go.Figure()

            # set up ONE trace
            fig.add_trace(go.Bar(x=self.data.index,
                                 y=self.data[self.data.columns[0]],
                                 marker={'color': " goldenrod"},

                                 visible=True)
                          )

            buttons = []

            # button with one option for each dataframe
            for col in self.data.columns:
                buttons.append(dict(method='restyle',
                                    label=col,
                                    visible=True,
                                    args=[{'y': [self.data[col]],
                                           'x': [self.data.index],
                                           'type': 'bar'}, [0]],
                                    )
                               )

            fig.update_layout(updatemenus=[dict(active=0,

                                                type="dropdown",
                                                buttons=buttons,
                                                x=0.64001,
                                                y=0.9999,
                                                xanchor='left',
                                                yanchor='bottom'),
                                           ],
                              title="CAGR ANALYSIS" + '<br><sup>CAGR Analysis for selected country</sup>',
                              title_x=0.455,
                              title_y=0.95,
                              title_font_family="Balto",
                              title_font_size=25,
                              xaxis_title="years",
                              paper_bgcolor='white',
                              # plot_bgcolor='black',

                              font_color='black',
                              yaxis_title="CAGR"
                              )
            # to make bg transperent
            fig.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                # paper_bgcolor= 'rgba(0, 0, 0, 0)’
            )
            fig.update_yaxes(showgrid=False, gridwidth=1, gridcolor='white')
        except:
            logger.info("[Error V3 : There is an error in cagr_dropdown_chart !]")
        else:
            return fig
        logger.info("[Process 3 : cagr_dropdown_chart has runned successfully !]")

    def cagr_all_years_chart(self):
        """
                Name : cagr_all_years_chart function
                Module : Visualization
                Description : This function creates the Get CAGR chart of all the countries
                for different number of years with the respective data.
                Parameters : None
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """
        try:
            transpoed_data = self.data.T
            # graph for all years and allcountries with legend as Years
            fig = px.bar(transpoed_data, x=transpoed_data.index, y=transpoed_data.columns)
            # Add range slider
            fig.update_layout(
                title="CAGR Analysis",
                #'<br><sup>Compare all the countries for the year Choosed in legend.(Can choose one or multiple Years from legend)</sup>'
                title_x=0.49,
                title_y=0.95,
                legend_title="Select years",
                title_font_family="Balto",
                title_font_size=25,
                xaxis_title="Years",
                yaxis_title="Rate of change"
            ),

            fig.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                # paper_bgcolor= 'rgba(0, 0, 0, 0)’
            )
        except:
            logger.info("[Error V4 : There is an error in cagr_all_years_chart !]")

        else:
            return fig
        logger.info("[Process 4 : cagr_all_years_chart has runned successfully !]")

    def cagr_grouped_countries(self):
        """
                Name : cagr_grouped_countries function
                Module : Visualization
                Description : This function creates the chart for CAGR chart of multiple countries
                 for different number of years for the respective data.
                Parameters : None
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """
        try:
            fig3 = go.Figure()

            country_list = list(self.data.columns)
            # print(country_list)

            for country in country_list:
                fig3.add_trace(
                    go.Bar(
                        x=self.data.index,
                        y=self.data[country],
                        name=country,
                        # visible = (i==0),
                        showlegend=True
                    )
                )

            # Add range slider
            fig3.update_layout(
                title="CAGR Analysis",
                #'<br><sup>Compare 6 or 7 countries CAGR at simultaneously.(Can choose one or multiple countires from legend)</sup>'
                title_x=0.49,
                title_y=0.95,
                legend_title="Choose countries",
                title_font_family="Balto",
                title_font_size=25,
                xaxis_title="Years",
                yaxis_title="Rate of change"
            ),

            # to make bg transperent
            fig3.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                # paper_bgcolor= 'rgba(0, 0, 0, 0)’
            )

            fig3.update_yaxes(showgrid=False, gridwidth=1, gridcolor='black')
        except:
            logger.info("[Error E5 : There is an error in cagr_grouped_countries !]")

        else:
            return fig3
        logger.info("[Process 5 : cagr_grouped_countries has runned successfully !]")


    def Plot_monthly_chart(self):
        """
                Name : Plot_monthly_chart function
                Module : Visualization
                Description : This function creates monthly analysis chart for all countries in the legend
                 for the respective data.
                Parameters : None
                Written By : Abhishek Mestry, Ninad Kadam, Viresh Dhuri
                Version : 1.0.0
                Revision : None

        """
        try:
            fig = px.line( self.data, y=self.data.columns[1:], x=self.data.index)
            fig.update_layout(
                title='Monthly Analysis of year 2017',
                title_x=0.410,
                title_y=0.95,
                legend_title=" Choose Countries",
                title_font_family="Balto",
                title_font_size=18,
                xaxis_title="years",
                paper_bgcolor='white',
                # plot_bgcolor='black',

                font_color='black',
                yaxis_title="CAGR"
            )
            # to make bg transperent
            fig.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                # paper_bgcolor= 'rgba(0, 0, 0, 0)’
            )
            fig.update_yaxes(showgrid=False, gridwidth=1, gridcolor='white')
        except:
            logger.info("[Error E6 : There is an error in Plotly_monthly_chart !]")

        else:
            return fig
        logger.info("[Process 6 : Plotly_monthly_chart has runned successfully !]")





