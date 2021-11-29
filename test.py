import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from ipywidgets.embed import embed_minimal_html

import ipywidgets as widgets
from ipywidgets.embed import embed_minimal_html


def run(country):
    path = "Exchange rate.xlsx"

    # to change the name oftitle
    if any("CPI" in path for i in path):
        a = "CPI"
    elif any("Exchange rate" in path for i in path):
        a = "Exchange rate"
    elif any("Exports Merchandise" in path for i in path):
        a = "Exports Merchandise"

    import pandas as pd
    import numpy as np
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

    fig = make_subplots()
    fig.add_trace(go.Bar(x=dff['Period'], y=dff[country],
                         name='Bar graph',
                         marker_color='blue',
                         opacity=0.4,
                         marker_line_color='rgb(8,48,107)',
                         marker_line_width=2),
                  row=1, col=1)

    # add first scatter trace at row = 1, col = 1
    fig.add_trace(go.Line(x=dff['Period'], y=dff[country], line=dict(color='red'), name='Line'),
                  row=1, col=1)

    fig.update_layout(
        title=country + " " + a,
        xaxis_title="years",
        yaxis_title="rate of change",
        legend_title="Graph types",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    return fig

dropdown = widgets.interact(run,country=['Afghanistan', 'Albania', 'United Arab Emirates', 'Armenia', 'Developing Asia',
                              'Antigua and Barbuda', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin',
                              'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina',
                              'Belarus', 'Belize', 'Bolivia', 'Brazil', 'Barbados', 'Bhutan', 'Botswana',
                              'Central African Republic', 'Canada', 'Switzerland', 'Chile', 'China',
                              "Cote d'Ivoire", 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia',
                              'Comoros', 'Cabo Verde', 'Costa Rica', 'Cyprus', 'Czech Republic',
                              'Germany', 'Developing Countries', 'Djibouti', 'Dominica', 'Denmark',
                              'Dominican Republic', 'Algeria', 'East Asia & Pacific developing',
                              'Europe & Central Asia developing', 'Ecuador', 'Egypt, Arab Rep.',
                              'Spain', 'Estonia', 'Finland', 'Fiji', 'France', 'Gabon',
                              'United Kingdom', 'Georgia', 'Guinea', 'Gambia, The', 'Equatorial Guinea',
                              'Greece', 'Grenada', 'Guatemala', 'Guyana', 'High Income Countries',
                              'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary',
                              'High income: OECD', 'Indonesia', 'India', 'Ireland', 'Iceland',
                              'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan',
                              'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati',
                              'St. Kitts and Nevis', 'Korea, Rep.',
                              'Latin America & Caribbean developing',
                              'Lao, PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia','Low Income',
                              'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Morocco', 'Moldova, Rep.',
                              'Madagascar', 'Maldives', 'Mexico', 'Middle Income Countries', 'Macedonia, FYR', 'Mali',
                              'Malta', 'Middle East & N. Africa developing', 'Montenegro', 'Mozambique',
                              'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'Nigeria', 'Nicaragua',
                              'Netherlands', 'Norway', 'Nepal', 'High Income: Non-OECD', 'Oman', 'Pakistan', 'Panama',
                              'Peru', 'Philippines', 'Poland', 'Portugal', 'Paraguay', 'West Bank and Gaza', 'Qatar',
                              'Romania', 'Russian Federation', 'Rwanda', 'South Asia developing', 'Saudi Arabia',
                              'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Serbia',
                              'Sub-Saharan Africa developing', 'Sao Tome and Principe', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden',
                              'Swaziland', 'Seychelles', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Timor-Leste', 'Tonga',
                              'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Taiwan, China',
                              'Uganda', 'Uruguay', 'United States', 'St. Vincent and the Grenadines',
                              'Venezuela, RB', 'Vietnam', 'World (WBG members)', 'Samoa', 'Yemen, Rep.', 'South Africa', 'Zambia']);


embed_minimal_html('export.html', views=[dropdown], title='Widgets export')

# def growth_rate(input_data):
#     """
#     It calculates the Percentage change between the current and a prior element.
#
#     """
#     excel_data = pd.read_excel(input_data)
#     excel_data = excel_data.fillna(0)
#     # extract_col_one = pd.DataFrame(excel_data["period"])
#
#     extract_col_one = excel_data.iloc[:, 0]
#
#     pct_change_data = excel_data.iloc[0:, 1:].pct_change() * 100
#
#     replacing_inf = pct_change_data.replace([np.inf, -np.inf], np.nan)
#     filled_na = replacing_inf.fillna(0)
#
#     pre_processed_data = pd.DataFrame(extract_col_one).join(filled_na)
#     return pre_processed_data
#
# exg_data = growth_rate("Exchange rate.xlsx")
# print(growth_rate("Exchange rate.xlsx"))
#
# fig = px.line(exg_data,  x= exg_data.index , y = "Poland")
# fig.update_layout(title_x=0.5, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
# fig.update_layout(height=500,
#                           margin={'l': 20, 'b': 0, 'r': 5, 't': 50})
# fig.show()
#



# from flask import Flask, render_template, request
# app = Flask(__name__)
# app.debug = True
#
#
# @app.route('/', methods=['GET'])
# def dropdown():
#     colours = ['Red', 'Blue', 'Black', 'Orange']
#     return render_template('test.html', colours=colours)
#
# if __name__ == "__main__":
#     app.run()


#hello world

#hello from omkar sutar 
