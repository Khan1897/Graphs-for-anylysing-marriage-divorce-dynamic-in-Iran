import pandas as pd

import numpy as np

import plotly.express as pt

import matplotlib.pyplot as plt

from dash import Dash, dcc, html, Input, Output

zona = pd.read_csv(r'C:\Users\1\Downloads\Marriage and divorce in Iran.csv', encoding = 'utf-8-sig', delimiter = ',')

data = pd.DataFrame(zona)



data = data.dropna()

data.loc[38:39, 'Year'] = ['1396', '1397']

data['Year'] = data['Year'].astype('int64')

data['Year'] = data['Year'] + 622


data.loc[28:32, list(data)[3:]] =  '0'

data = data.astype('int64')


data['M. D. Ratio'] = data['marriage(country)']/ data['divorce(country)']


lola = data['marriage(country)'].mean()

vava = data['marriage(village)'] != 0

vova = pd.DataFrame(data[vava])

vova['M. D. Ratio for villages'] = vova['marriage(village)']/vova['divorce(village)']
vova['M. D. Ratio for cities'] = vova['marriage(city)']/vova['divorce(city)']

app = Dash()

fdrop = dcc.Dropdown(options = ['M. D. Ratio', 'M. D. Ratio for villages', 'M. D. Ratio for cities'], value = 'M. D. Ratio')

app.layout = html.Div(children = [
    html.Div([html.H1(children = 'Marriages/Divorces in Iran'),
             fdrop,
             dcc.Graph(id = 'For Iran')])
])

@app.callback(
Output(component_id = 'For Iran', component_property = 'figure'),
Input(component_id = fdrop, component_property = 'value'))
def what_to_show(hihi):
    if hihi == 'M. D. Ratio':
        fig = pt.line(data, x = 'Year', y = hihi)
    else:
        fig = pt.line(vova, x = 'Year', y = hihi)
    return fig


if __name__ == '__main__':
    app.run_server(debug = True)



