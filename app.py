from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import ipywidgets as widgets

import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots
import plotly.graph_objects as go

import json
import pandas as pd
import numpy as np
import plotly


def Chart_1(path):
    if any("CPI data" in path for i in path):
        a = "CPI(Consumer price index)"
    elif any("Exchange rate" in path for i in path):
        a = "Exchange rate"
    elif any("Exports Merchandise" in path for i in path):
        a = "Exports Merchandise"

    # preprocessing
    excel_data = pd.read_excel(path)
    excel_data = excel_data.fillna(0)
    # extract_col_one = pd.DataFrame(excel_data["period"])

    # loop by Viresh to drop 1st col if all 0s
    for i in excel_data.iloc[0]:
        if i == 0:
            excel_data.drop([0], inplace=True)
        else:
            pass
        break
    else:
        pass
    # ....

    extract_col_one = excel_data.iloc[:, 0]

    pct_change_data = excel_data.iloc[0:, 1:].pct_change() * 100

    replacing_inf = pct_change_data.replace([np.inf, -np.inf], np.nan)
    filled_na = replacing_inf.fillna(0)

    dff = pd.DataFrame(extract_col_one).join(filled_na)
    dff.rename(columns={'Unnamed: 0': 'Period'}, inplace=True)
    # dff.drop([0], inplace = True) # switch on this line if not using virey loop
    # pre_processed_data.reset_index(inplace=False)
    dff['Period'] = pd.to_datetime(dff['Period'], format='%Y')
    dff['Period'] = pd.DatetimeIndex(dff["Period"]).year  ##line by viresh

    # graphs
    buttons = []
    i = 0

    fig3 = go.Figure()

    country_list = list(dff.columns[1:])
    # print(country_list)

    for country in country_list:
        fig3.add_trace(
            go.Scatter(
                x=dff['Period'],
                y=dff[country],
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
                                         x=0.5,
                                         y=1.1,
                                         xanchor='left',
                                         yanchor='bottom'),
                                    ])

    # fig3.update_layout(
    #     autosize=False,
    #     width=1000,
    #     height=800,
    #     xaxis1_rangeslider_visible = True)

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
            dict(text="Choose a country:", showarrow=False,
                 x=0.43, xref="paper", y=1.2, yref="paper", align="left")],
        title=a + '<br><sup>Year to year Analysis</sup>',
        xaxis_title="years",
        yaxis_title="rate of change",
        font=dict(
                family="Times New Roman",
                size=16,
                color="Black"
                )
    )
    return fig3


def Chart_2(path):
    if any("CPI data" in path for i in path):
        a = "CPI"
    elif any("Exchange rate" in path for i in path):
        a = "Exchange rate"
    elif any("Exports Merchandise" in path for i in path):
        a = "Exports Merchandise"

    # preprocessing
    excel_data = pd.read_excel(path)
    excel_data = excel_data.fillna(0)
    # extract_col_one = pd.DataFrame(excel_data["period"])

    # loop by Viresh to drop 1st col if all 0s
    for i in excel_data.iloc[0]:
        if i == 0:
            excel_data.drop([0], inplace=True)
        else:
            pass
        break
    else:
        pass
    # ....

    extract_col_one = excel_data.iloc[:, 0]

    pct_change_data = excel_data.iloc[0:, 1:].pct_change() * 100

    replacing_inf = pct_change_data.replace([np.inf, -np.inf], np.nan)
    filled_na = replacing_inf.fillna(0)

    dff = pd.DataFrame(extract_col_one).join(filled_na)
    dff.rename(columns={'Unnamed: 0': 'Period'}, inplace=True)
    # dff.drop([0], inplace = True) # switch on this line if not using virey loop
    # pre_processed_data.reset_index(inplace=False)
    dff['Period'] = pd.to_datetime(dff['Period'], format='%Y')
    dff['Period'] = pd.DatetimeIndex(dff["Period"]).year  ##line by viresh

    fig4 = go.Figure()

    country_list = list(dff.columns[1:])
    # print(country_list)

    for country in country_list:
        fig4.add_trace(
            go.Scatter(
                x=dff['Period'],
                y=dff[country],
                name=country,
                # visible = (i==0),
                showlegend=True
            )
        )

    # Add range slider
    fig4.update_layout(
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

        #title=a,
        xaxis_title="years",
        yaxis_title="rate of change"
    )

    return fig4


def growth_rate(input_data):
    """
    It calculates the Percentage change between the current and a prior element.

    """
    excel_data = pd.read_excel(input_data)
    excel_data = excel_data.fillna(0)
    # extract_col_one = pd.DataFrame(excel_data["period"])

    extract_col_one = excel_data.iloc[:, 0]

    pct_change_data = excel_data.iloc[0:, 1:].pct_change() * 100

    replacing_inf = pct_change_data.replace([np.inf, -np.inf], np.nan)
    filled_na = replacing_inf.fillna(0)

    pre_processed_data = pd.DataFrame(extract_col_one).join(filled_na)
    return pre_processed_data

exg_data = growth_rate("Exchange rate.xlsx")
#print(growth_rate("Exchange rate.xlsx"))

fig = px.line(exg_data,  x= exg_data.index , y = "Poland")
fig.update_layout(title_x=0.5, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
fig.update_layout(height=500,
                          margin={'l': 20, 'b': 0, 'r': 5, 't': 50})

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/Exg_rate', methods=['GET'])
def Exg_rate():
    return render_template("exg_rate.html")


@app.route('/CPI', methods=['GET'])
def CPI():
    return render_template("CPI.html")


@app.route('/Exp_mrch', methods=['GET'])
def Exp_mrch():
    # exg_data = growth_rate("Exchange rate.xlsx")
    # #print(growth_rate("Exchange rate.xlsx"))
    #
    # fig = px.line(exg_data, x=exg_data.index, y="Poland")

    fig = Chart_1("Exports Merchandise.xlsx")
    #fig.update_layout(title_x=0.5, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
    fig.update_layout(height=500, width=1000)
    #header = "Exchange rate PLot "
    #description = "The Exchange rate data is been ploted against Poland"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    #fig1 = px.line(exg_data, x=exg_data.index, y="India")
    fig1 = Chart_2("Exports Merchandise.xlsx")
    #fig1.update_layout(title_x=0.5, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
    fig1.update_layout(height=500, width=900)
    header1 = "Exchange rate PLot"
    description1 = "The Exchange rate data is been ploted against Poland"
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("Exp_mrch.html", graphJSON=graphJSON,
                           #header=header,description=description,
                            graphJSON1=graphJSON1,
                           header1=header1, description1=description1
                           )

if __name__ == "__main__":
    app.run()

