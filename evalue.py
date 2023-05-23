import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random

def generate_random_list(start, end, length):
    random_list = [random.uniform(start, end) for _ in range(length)]
    return random_list
start = 0.02
end = 0.04
length = 21

random_values = generate_random_list(start, end, length)
inflation_data = {
    2000: 0.03,
    2001: 0.02,
    2002: 0.035,
    2003:random_values[0],
    2004:random_values[1],
    2005:random_values[2],
    2006:random_values[3],
    2007:random_values[4],
    2008:random_values[5],
    2009:random_values[6],
    2010:random_values[7],
    2011:random_values[8],
    2012:random_values[9],
    2013:random_values[10],
    2014:random_values[11],
    2015:random_values[12],
    2016:random_values[13],
    2017:random_values[14],
    2018:random_values[15],
    2019:random_values[16],
    2020:random_values[17],
    2021:random_values[18],
    2022:random_values[19],
    2023:random_values[20],



    # Add more years and corresponding inflation rates here
}

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Inflation Calculator"),
        html.Div(
            children=[
                html.Label("Initial Sum:"),
                dcc.Input(id="initial-sum", type="number", value=1000),
            ],
            style={"margin-bottom": "10px"},
        ),
        html.Div(
            children=[
                html.Label("Initial Year:"),
                dcc.Input(id="initial-year", type="number", value=2010),
            ],
            style={"margin-bottom": "10px"},
        ),
        html.Div(
            children=[
                html.Label("Final Year:"),
                dcc.Input(id="final-year", type="number", value=2022),
            ],
            style={"margin-bottom": "10px"},
        ),
        dcc.Graph(id="inflation-chart"),
    ],
    style={"padding": "20px"},
)


@app.callback(
    Output("inflation-chart", "figure"),
    [
    Input("initial-sum", "value"),
    Input("initial-year", "value"),
    Input("final-year", "value")]
)
def update_chart(initial_sum, initial_year, final_year):
    years = range(initial_year, final_year + 1)
    adjusted_values = [initial_sum]

    for year in years[1:]:
        inflation_rate = inflation_data.get(year, 0)
        adjusted_value = adjusted_values[-1] * (1 + inflation_rate)
        adjusted_values.append(adjusted_value)

    return {
        "data": [
            {
                "x": list(years),
                "y": adjusted_values,
                "type": "line",
                "marker": {"color": "blue"},
            }
        ],
        "layout": {
            "title": "Inflation Calculator",
            "xaxis": {"title": "Year"},
            "yaxis": {"title": "Adjusted Value"},
        },
    }


if __name__ == "__main__":
    app.run_server(debug=True)

