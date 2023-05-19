from imports import *

dash.register_page(__name__, path='/bonds-analysis', name='Dashboard')


''' Page 4 have '''
layout = html.Div([
    
    dbc.Row([
        html.H1("this is page 4   have contents!!!"),
        html.H1("tính công thức trái phiếu doanh nghiệp tại đây")
    ])
])