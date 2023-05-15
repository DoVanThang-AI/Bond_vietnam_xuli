import pandas as pd
import numpy as np
import plotly.express as px
import datetime as dt
import dash
from dash import dcc
from dash import html, callback
from dash.dependencies import Input, Output,State
import scipy as sp
import dash_ag_grid as dag
import dash_bootstrap_components as dbc

ytm_layout = html.Div([
    html.Div([
    html.H1("Công cụ tính lợi suất trái phiếu"),
    html.Div([
        html.Label("Current Price:"),
        dcc.Input(id='current-price', type='number', step='0.01', value=96890)
    ]),
    html.Div([
        html.Label("Face Value:"),
        dcc.Input(id='face-value', type='number', step='0.01', value=100000)
    ]),
    html.Div([
        html.Label("Interest Rate (%):"),
        dcc.Input(id='interest-rate', type='number', step='0.01', value=7.83)
    ]),
    html.Div([
        html.Label("Maturity Years:"),
        dcc.Input(id='maturity-years', type='number', value=3)
    ]),
    html.Button('Calculate', id='calculate-button'),
    html.Div([
        html.Label("Current Yield:"),
        html.Div(id='current-yield-result'),
    # ]),
    # html.Div([
        html.Label("Yield to Maturity:"),
        html.Div(id='yield-to-maturity-result')
    ],style={'background-color': 'antiquewhite','border-radius':'20px'})
]),
html.Hr(),
html.Div([
    html.H3("Đầu vào của lợi suất của trái phiếu "),
    html.Br(),
            html.P(children=[html.B("Giá hiện tại:"), "Giá mà trái phiếu giao dịch hôm nay"],style={'color':'black'}),
            html.P(children=[html.B("mệnh giá:"), "định giá của trái phiếu"],style={'color':'black'}),
            html.P(children=[html.B("lãi suất hàng năm:"), "Lãi suất hàng năm của trái phiếu nhận được"],style={'color':'black'}),
            html.P(children=[html.B("thời gian đáo hạn:"), "thời gian mà trái phiếu đó tới lúc đáo hạn"],style={'color':'black'}),
            html.Hr(),
            html.Div([
                html.H3("Công thức toán học dùng trong tính lợi suất của trái phiếu"),
                html.P(children=[html.B('Lợi suất trái phiếu = tiền lãi hàng năm / giá trái phiếu')]),
                html.P("Giả sử, bạn mua trái phiếu với giá 1 tỷ, tiền lãi được nhận sau mỗi năm là 100 triệu / năm"),
                html.P("Nếu không bán trái phiếu trước hạn , bạn sẽ nhận đưuọc lãi suất coupon là 100 triệu mỗi năm trong thời gian 5 năm và nhận lại 1 tỷ"),
                html.P("khi đến thời hạn thanh toán từ người phát hành trái phiếu. khi đó lợi suất trái phiếu là 100.000.000/1.000.000.000 = 10% "),
                html.P("nếu bán trước hạn cũng không nhận được đủ 1 tỷ. Nguyên nhân là do giá trái phiếu thay đổi mỗi ngày. Nếu giá trái phiếu tại "),
                html.P("hiện tại thấp hơn giá ban đầu mua, bạn sẽ bán trái phiếu của mình dưới mệnh giá đó, đó được goi là chiết khấu. Còn nếu giá trái phiếu lúc đó là 1.2 tỷ"),
                html.P("thì lợi suất là 100 triệu / 1,2 tỷ là 8.33%. Nên hãy cân nhắc lựa chọn để đảm bảo thu về lợi nhuận tốt nhất cho bản thân mình nhé")
            ])  
])

])

duration_bond = html.Div(
            [
            html.Div([

           
                html.Div([
                    html.H1("Công cụ tính thời hạn trái phiếu"),
                html.Div(
                    [
                        html.Label("Mệnh giá:"),
                        dcc.Input(id="par-value_layer3", type="number", value=100000),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Lãi suất hàng năm(%):"),
                        dcc.Input(id="interest-rate_layer3", type="number", value=7.83),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div([
                    html.Label('YTM (%):'),
                    dcc.Input(id='YTM_layer3',type="number", value = 10.81)
                ],style={"marginBottom": "10px"}),
                html.Div(
                    [
                        html.Label("thời gian đáo hạn(years):"),
                        dcc.Input(id="maturity-time_layer3", type="number", value=5),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Tần suất đáo hạn:"),
                        dcc.Dropdown(
                            id="maturity-frequency_layer3",
                            options=[
                                {"label": "Annual", "value": 1},
                                {"label": "Semi-Annual", "value": 2},
                                {"label": "Quarterly", "value": 4},
                            ],
                            value=1,
                        ),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Button("Calculate", id="calculate-button_layer3", n_clicks=0),
                html.Div(id="result_layer3"),

                ]),
                html.Hr(),
                html.Div([  
                    html.H3("Công thức toán học dùng trong tính thời hạn của trái phiếu"),
                    dcc.Markdown('$\dfrac{\sum_{t=1}^{n}PV(CF_t)^t}{Market bond price}$', mathjax=True,style={'text-align':'center','font-size':'x-large'}),
                    html.Br(),
                    html.P("Trong đó:"),
                    html.P("PV(CF t ) Giá trị hiện tại của dòng tiền (coupon) tại thời điểm t"),
                    html.P("t – Khoảng thời gian cho mỗi dòng tiền"),
                    html.P("C là tỷ lệ coupon"),
                    html.P("n – Tổng số kỳ hạn đến hạn"),
                    html.P("M – Giá trị khi đáo hạn"),
                    html.P("Y – Sản lượng định kỳ"),
                    html.Br(),
                    html.P("Ví dụ: trái phiếu kỳ hạn 2 năm mệnh giá 1.000 đô la trả lãi coupon 6% nửa năm một lần và lãi suất hàng năm là 5%. Như vậy, giá thị trường của trái phiếu là $1.018,81, bằng tổng giá trị hiện tại của tất cả các dòng tiền. Thời điểm nhận được mỗi dòng tiền sau đó được tính theo giá trị hiện tại của dòng tiền đó với giá thị trường."),
                    html.P("Thời lượng Macaulay là tổng của các khoảng thời gian trung bình có trọng số này, là 1,915 năm. Một nhà đầu tư phải nắm giữ trái phiếu trong 1,915 năm để giá trị hiện tại của dòng tiền nhận được bù đắp chính xác giá đã thanh toán."),
                    html.Img(src='https://cdn.corporatefinanceinstitute.com/assets/macaulay-duration1-1024x365.png')
                ])
                 ]),
                

            
           
            ],style={'display':'flex'}
        )


yield_to_call = html.Div([
    html.Div([
    html.H1("Tính Yield to Call và Current Yield"),
    html.Div([
        html.Label("Giá trái phiếu (VNĐ):"),
        dcc.Input(id="bond-price-input", type="number", value=1175),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Mệnh giá trái phiếu (VNĐ):"),
        dcc.Input(id="face-value-input", type="number", value=1000),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Giá gọi (VNĐ):"),
        dcc.Input(id="call-price-input", type="number", value=1100),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Số năm đến khi gọi:"),
        dcc.Input(id="years-to-call-input", type="number", value=5),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Tỷ lệ lãi suất hàng năm (%):"),
        dcc.Input(id="annual-interest-rate-input", type="number", value=10),
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
    ]),
    html.Hr(),
    html.Div([
        html.H3("Đầu vào của tính năng suất gọi đầu vào của trái phiếu"),
        html.P('Giá giao dịch trái phiếu hiện tại ($) - Giá giao dịch của trái phiếu ngày hôm nay.'),
        html.P('Mệnh giá trái phiếu/Mệnh giá ($)'),
        html.P('- Mệnh giá của trái phiếu, còn được gọi là mệnh giá.'),

        html.P('Giá gọi ($) - Nói chung, trái phiếu có thể mua lại chỉ có thể được gọi ở một mức chênh lệch nào đó so với mệnh giá. Nếu có phí bảo hiểm, hãy nhập giá để gọi trái phiếu trong trường này.'),
        html.P('Số năm gọi - Số năm cho đến khi trái phiếu có thể được gọi.'),
        html.P('Tỷ lệ phiếu lãi hàng năm (%)'),
        html.P('- Tỷ lệ phần trăm hàng năm được trả cho trái phiếu dựa trên mệnh giá ( đọc: không tính toán lại nó cho giá giao dịch hiện tại, công cụ sẽ xử lý nó.)'),
        html.P('Tần suất thanh toán phiếu lãi - Tần suất trái phiếu thực hiện thanh toán phiếu lãi.'),
        html.Hr(),
        html.H3('Đầu ra của công cụ bao gồm'),
        html.P('Lợi suất thu hồi (%): Giải pháp hội tụ cho lợi suất thu hồi của trái phiếu hiện tại (tỷ lệ hoàn vốn nội bộ giả định trái phiếu được thu hồi).'),
        html.P('Lợi suất hiện tại (%): Lợi suất được tính toán đơn giản sử dụng giá giao dịch hiện tại và mệnh giá của trái phiếu. Xem công cụ tính lãi suất trái phiếu để được giải thích.'),
        html.Hr(),
        html.H3("Công thức của tính năng suất gọi đầu vào của trái phiếu"),
    ])
])