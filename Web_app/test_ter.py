import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Tính Yield to Call và Current Yield"),
    html.Div([
        html.Label("Giá trái phiếu (VNĐ):"),
        dcc.Input(id="bond-price-input", type="number", value=1000),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Mệnh giá trái phiếu (VNĐ):"),
        dcc.Input(id="face-value-input", type="number", value=1000),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Giá gọi (VNĐ):"),
        dcc.Input(id="call-price-input", type="number", value=1050),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Số năm đến khi gọi:"),
        dcc.Input(id="years-to-call-input", type="number", value=5),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Tỷ lệ lãi suất hàng năm (%):"),
        dcc.Input(id="annual-interest-rate-input", type="number", value=5),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Tần suất trả lãi:"),
        dcc.Dropdown(
            id="interest-frequency-dropdown",
            options=[
                {"label": "Năm", "value": 1},
                {"label": "Nửa năm", "value": 2},
                {"label": "Tháng", "value": 12},
            ],
            value=1,
        ),
    ], style={"margin-bottom": "10px"}),
    html.Button("Tính toán", id="calculate-button"),
    html.Div(id="result-output", style={"margin-top": "10px"}),
])

@app.callback(
    Output("result-output", "children"),
    [Input("calculate-button", "n_clicks")],
    [dash.dependencies.State("bond-price-input", "value"),
     dash.dependencies.State("face-value-input", "value"),
     dash.dependencies.State("call-price-input", "value"),
     dash.dependencies.State("years-to-call-input", "value"),
     dash.dependencies.State("annual-interest-rate-input", "value"),
     dash.dependencies.State("interest-frequency-dropdown", "value")]
)
def calculate_yield(n_clicks, bond_price, face_value, call_price, years_to_call, annual_coupon_rate, interest_frequency):
    if n_clicks is not None:
        yield_to_call = (annual_coupon_rate*10+((call_price-bond_price)/years_to_call))/((call_price+bond_price)/interest_frequency)
        current_yield = (face_value*(annual_coupon_rate/100)/bond_price)
        result = html.Div([
            html.P(f"Current Yield: {current_yield:.2%}"),
            html.P(f"Yield to Call: {yield_to_call:.2%}")
        ])
        return result
if __name__ == '__main__':
    app.run_server(debug=True)
	