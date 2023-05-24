from imports import *

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

# 
evalue_bonds = html.Div([
                html.Div([
                    html.H1("Đánh giá trái phiếu"),
                html.Div([
                        html.Label("Giá trái phiếu:"),
                        dcc.Input(id="bond-price-eva", type="number", step=0.01,value=96850),
                    ]),    
                html.Div(
                    [
                        html.Label("Mệnh giá:"),
                        dcc.Input(id="par-value-eva", type="number", value=100000),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Lãi suất hàng năm(%):"),
                        dcc.Input(id="interest-rate-eva", type="number", value=7.83),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div([
                    html.Label('YTM (%):'),
                    dcc.Input(id='YTM-eva',type="number", value = 10.81)
                ],style={"marginBottom": "10px"}),
                html.Div(
                    [
                        html.Label("thời gian đáo hạn(years):"),
                        dcc.Input(id="maturity-time-eva", type="number", value=5),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Tần suất đáo hạn:"),
                        dcc.Dropdown(
                            id="maturity-frequency-eva",
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
                html.Button("Calculate", id="calculate-button-eva", n_clicks=0),
                html.Div(id="result-eva"),
                ]),
                html.Hr(),
                html.Div([
                    html.P("Đánh giá trái phiếu là quá trình xác định giá trị hiện tại của một trái phiếu hoặc tập hợp các trái phiếu. Đây là một quá trình quan trọng trong lĩnh vực tài chính và đầu tư. Dưới đây là một số lý do tại sao đánh giá trái phiếu là cần thiết:"),
                    dbc.Card([
                        html.H1('🌀TIP:'),
                        html.P("Đưa ra quyết định đầu tư: Đánh giá trái phiếu giúp các nhà đầu tư đánh giá khả năng sinh lời và rủi ro của trái phiếu. Bằng cách xem xét các yếu tố như lãi suất, thời hạn, tín dụng của công ty phát hành trái phiếu, người đầu tư có thể quyết định xem liệu đầu tư vào trái phiếu đó có phù hợp với mục tiêu đầu tư của họ hay không."),
                        html.P("Xác định giá trị thực của trái phiếu: Đánh giá trái phiếu giúp xác định giá trị thực của trái phiếu bằng cách tính toán giá trị hiện tại của dòng tiền mà trái phiếu sẽ tạo ra trong tương lai. Điều này giúp nhà đầu tư biết xem mức giá trái phiếu hiện tại có phản ánh đúng giá trị của nó hay không."),
                        html.P('Đánh giá tín dụng: Đánh giá trái phiếu cũng liên quan đến việc đánh giá tín dụng của công ty phát hành trái phiếu. Nhà đầu tư cần xem xét khả năng công ty trả lãi và trả vốn cho những trái phiếu đã phát hành. Các tổ chức đánh giá tín dụng như Moodys và Fitch Ratings thường cung cấp các bảng điểm tín dụng để đánh giá mức độ rủi ro tín dụng của trái phiếu.'),
                        html.P("Quyết định mua bán trái phiếu: Đánh giá trái phiếu giúp nhà đầu tư đưa ra quyết định mua hoặc bán trái phiếu. Nếu giá trái phiếu được định giá thấp hơn giá trị thực, đó có thể là một cơ hội mua vào. Ngược lại, nếu giá trái phiếu được định giá cao hơn giá trị thực, có thể là thời điểm để bán.")

                    ],style={'background-color':'#c3c3c36e','color':'red','font-weight':'bold'})
                    
                ])

])
BEY_bonds =  html.Div([
                html.Div([
                    html.H1("Lợi tức tương đương trái phiếu"),
                html.Div([
                        html.Label("Giá trái phiếu:"),
                        dcc.Input(id="bond-price-bey", type="number", step=0.01,value=980),
                    ]),    
                html.Div(
                    [
                        html.Label("Mệnh giá:"),
                        dcc.Input(id="par-value-bey", type="number", value=1000),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Số ngày đáo hạn"),
                        dcc.Input(id="interest-rate-bey", type="number", step=1, value=300  ),
                    ],
                    style={"marginBottom": "10px"},
                ),
                
                html.Button("Calculate", id="calculate-button-bey", n_clicks=0),
                html.Div(id="result-bey"),
                ]),
                html.Br(),
                html.Div([
                    html.H3('Lợi tức tương đương trái phiếu (BEY) là gì?'),
                    html.P('Công thức lợi tức tương đương trái phiếu, còn được gọi là công thức BEY , là một trong nhiều cách để phân tích lợi tức đầu tư trái phiếu. Cụ thể hơn, BEY so sánh khoản thanh toán gốc với giá trái phiếu . Do đó, nó cho bạn biết bạn có thể nhận được bao nhiêu tiền lãi khi nhận tiền gốc sau khi mua trái phiếu.'),
                    html.P("Cách tính lợi tức tương đương trái phiếu đơn giãn như sau:"),
                    html.P("Ví dụ : có 1 trái phiếu có giá là $980 với mệnh giá của trái phiếu là $1000 , số ngày đến đáo hạn là 300 ngày"),
                    html.P(children =[html.B("1. Xác định giá trái phiếu"),'ở đây giá của trái phiếu là $920']),
                    html.P(children =[html.B("2. Xác định mệnh giá"),'ở đây giá của trái phiếu là $1000']),
                    html.P(children=[html.B("3. Xác định lợi tức trái phiếu (BEY)")]),
                    dcc.Markdown('$\dfrac{mệnh giá - giá trái phiếu}{giá * (365 / thời gian )}$', mathjax=True,style={'text-align':'center','font-size':'x-large'}),

                    html.P('Sử dụng công thức ta có: '),
                    dcc.Markdown('$\dfrac{$1,000 - $980}{$980} * \dfrac{365}{300} = 2.48\%$', mathjax=True,style={'text-align':'center','font-size':'x-medium'})
                    
                ])

])                

coupon_rate_bonds = html.Div([
                html.Div([
                    html.H1("tỷ lệ phiếu giảm giá"),  
                html.Div(
                    [
                        html.Label("Mệnh giá VND:"),
                        dcc.Input(id="par-value-coupon", type="number", value=100000),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("phiếu giảm giá mỗi kỳ (VND)"),
                        dcc.Input(id="interest-rate-coupon", type="number", step=1, value=25000 ),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Tần suất đáo hạn:"),
                        dcc.Dropdown(
                            id="maturity-frequency-coupon",
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
                
                html.Button("Calculate", id="calculate-button-coupon", n_clicks=0),
                html.Div(id="result-coupon"),
                ]),
                html.Br(),
                html.Div([
                    html.H3('Lãi suất coupon là gì?'),
                    html.P('Lãi suất coupon cho bạn biết số tiền thanh toán coupon tương đối so với mệnh giá , là số tiền bạn cho vay để mua trái phiếu.'),
                    html.P("Cách tính lãi suất coupon trái phiếu đơn giãn như sau:"),
                    html.P("Ví dụ : có 1 trái phiếu có mệnh giá là 100,000VND với phiếu giảm giá mỗi kỳ là 25,000 VND với tần suất trả lãi là 2 lần 1 năm "),
                    html.P(children =[html.B("1. Xác định mệnh giá trái phiếu"),'ở đây giá của trái phiếu là 100,000 VND']),
                    html.P(children =[html.B("2. Tính khoản thanh toán coupon hàng năm")]),
                    html.P('thanh toán coupon hàng năm = phiếu giảm giá mỗi kỳ * tần suất trả lãi'),
                    html.P(children=[html.B("Vì đây là trái phiếu nữa năm trả 1 lần nên khoản thanh toán coupon hàng năm của trái phiếu là 25000*2 = 50,000 VND")]),
                    html.P(children=[html.B("3.Tính lãi suất coupon ")]),
                    dcc.Markdown('$coupon_rate = \dfrac{thanh toán coupon hàng năm }{mệnh giá)}$', mathjax=True,style={'text-align':'center','font-size':'x-medium'}),

                    html.P('Sử dụng công thức ta có: '),
                    dcc.Markdown('$\dfrac{50,000}{100,000} = 5\%$', mathjax=True,style={'text-align':'center','font-size':'x-medium'})
                    
                ])

])                
coupon_payments_bonds = html.Div([
    html.Div([
    html.H1("Coupon Payment Caculator"),
    html.Br(),
    html.Div([
        html.Label("Face Value: (VNĐ)"),
        dcc.Input(id="face-value-eight", type="number", value=100000),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Annual coupon rate: (%)"),
        dcc.Input(id="annual-interest-rate-eight", type="number", value=7.83),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("payment frequency of year"),
        dcc.Dropdown(
            id="interest-frequency-dropdown-eight",
            options=[
                {"label": "Năm", "value": 1},
                {"label": "Nửa năm", "value": 2},
                {"label": "Tháng", "value": 12},
            ],
            value=2,
        ),
    ], style={"margin-bottom": "10px"}),
    html.Button("Tính toán", id="calculate-button-eight"),
    html.Div(id="result-output-eight", style={"margin-top": "10px"}),
    ]),
    html.Hr(),
    html.Div([
        html.H1('Phiếu giảm giá là gì?',style={'font-weight':'bold'}),
        html.P("Một khoản thanh toán coupon hoặc coupon là lãi suất hàng năm được trả cho trái phiếu, được biểu thị bằng tỷ lệ phần trăm của mệnh giá và được thanh toán từ ngày phát hành cho đến khi đáo hạn. Phiếu giảm giá thường được đề cập đến theo tỷ lệ lãi suất trái phiếu (tổng số phiếu giảm giá được trả trong một năm chia cho mệnh giá của trái phiếu được đề cập)."),
        dbc.Card([
            html.H1('🌀TIP:'),
            html.P("Thanh toán coupon đề cập đến tiền lãi hàng năm được trả cho trái phiếu giữa ngày phát hành và ngày đáo hạn."),
            html.P("Lãi suất trái phiếu được xác định bằng cách cộng tổng của tất cả các trái phiếu được trả mỗi năm,"),
            html.P(" sau đó chia tổng số đó cho mệnh giá của trái phiếu.")
        ],style={'background-color':'#c3c3c36e','color':'red','font-weight':'bold'}),

    ])
])

#  risk-adjusted bonds
risk_adjusted_bonds = html.Div([
    html.Div([
    html.H1("calculate risk-adjusted return"),
    html.Br(),
    html.P("Please filter Cty A"),
    html.Div([
        html.Label("porfolio return: {%}"),
        dcc.Input(id="pofolio-return", type="number", value=12),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Risk free return: (%)"),
        dcc.Input(id="risk-free", type="number", value=3),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Standard Deviation of Portfolio return {%}"),
        dcc.Input(id="standard", type="number", value=10),
    ], style={"margin-bottom": "10px"}),
    html.Br(),
    html.P("Please filter Cty B"),
    html.Div([
        html.Label("porfolio return: {%}"),
        dcc.Input(id="pofolio-return-b", type="number", value=10),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Risk free return: (%)"),
        dcc.Input(id="risk-free-b", type="number", value=3),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Standard Deviation of Portfolio return {%}"),
        dcc.Input(id="standard-b", type="number", value=7),
    ], style={"margin-bottom": "10px"}),
    html.Button("Calculator", id="calculate-button-risk"),
    html.Div(id="result-risk", style={"margin-top": "10px"}),
    ]),
    html.Hr(),
    html.Div([
        html.H1("‼️ CÂN NHẮC ĐẶC BIỆT",style={'text-align':'center','font-weight':'bold','font-size':'20px'}),
        html.P('Tránh rủi ro không phải lúc nào cũng là điều tốt trong đầu tư, vì vậy hãy cảnh giác với việc phản ứng thái quá với những con số này, đặc biệt nếu thời gian được đo lường là ngắn.'),
        html.P("Ở những thị trường mạnh, một quỹ tương hỗ có rủi ro thấp hơn mức chuẩn của nó  có thể hạn chế hiệu suất thực mà nhà đầu tư muốn thấy."),

        dbc.Card([
            html.P('🌀TIP: Hãy coi chừng phản ứng thái quá với những con số này, đặc biệt nếu thời gian được đo là ngắn. Rủi ro lớn hơn có thể có nghĩa là phần thưởng lớn hơn trong dài hạn.'),

        ],style={'background-color':'#c3c3c36e','color':'red'}),
        html.P("Một quỹ chấp nhận nhiều rủi ro hơn mức chuẩn của nó có thể thu được lợi nhuận tốt hơn. Trên thực tế, người ta đã chứng minh nhiều lần rằng các quỹ tương hỗ có rủi ro cao hơn có thể tích lũy các khoản lỗ lớn hơn trong các giai đoạn biến động"),
        html.P(", nhưng cũng có khả năng hoạt động tốt hơn các tiêu chuẩn của chúng trong toàn bộ chu kỳ thị trường . ")
    ]),
    html.Br(),

])

#zero coupont
zero_coupon_bonds = html.Div([
    html.Div([
    html.H1("Zero Coupon Bond Effective Yield Calculator"),
    html.Br(),
    html.Div([
        html.Label("Face Value: (VNĐ)"),
        dcc.Input(id="face-vl-zero", type="number", value=100000),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Present Value: (VNĐ)"),
        dcc.Input(id="present-vl-zero", type="number", value=96850),
    ], style={"margin-bottom": "10px"}),
    html.Div([
        html.Label("Time to Maturity"),
        dcc.Input(id="time-zero", type="number",step=1, value=3),
    ], style={"margin-bottom": "10px"}),
    html.Button("Calculator", id="calculate-button-zero"),
    html.Div(id="result-zero", style={"margin-top": "10px"}),
    ]),
    html.Hr(),
    html.Div([
        html.H5("‼️ CÂN NHẮC ĐẶC BIỆT"),
        html.P('Lợi suất đáo hạn (YTM) là một số liệu quan trọng được sử dụng trong thị trường trái phiếu để mô tả tổng tỷ suất lợi nhuận dự kiến ​​từ một trái phiếu sau khi trái phiếu đã thực hiện tất cả các khoản thanh toán lãi trong tương lai và hoàn trả số tiền gốc ban đầu. Tuy nhiên, trái phiếu không lãi suất (trái phiếu z) không có các khoản thanh toán lãi định kỳ, giúp phân biệt các tính toán YTM với trái phiếu có lãi suất coupon .'),
        html.P("Ở đây, chúng ta xem xét cách ước tính YTM của một trái phiếu không trả lãi định kỳ."),

        dbc.Card([
            html.P('🌀TIP: Lợi suất đáo hạn (YTM) cho các nhà đầu tư trái phiếu biết tổng lợi nhuận của họ sẽ là bao nhiêu nếu họ giữ trái phiếu cho đến khi đáo hạn.'),

        
        html.P("YTM tính đến các khoản thanh toán phiếu lãi thông thường được thực hiện cộng với việc hoàn trả tiền gốc."),
        html.P("Trái phiếu không lãi suất không trả lãi theo định kỳ."),
        html.P('Thay vào đó, trái phiếu z được phát hành với giá chiết khấu và đáo hạn theo mệnh giá của chúng.'),
        html.P('Kết quả là, tính toán YTM cho trái phiếu không lãi suất khác với trái phiếu truyền thống.')
        ],style={'background-color':'#c3c3c36e','color':'red'}),
    ])

])

inflation_bonds = html.Div(
    children=[
        html.Div([
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
        ]),
        html.Hr(),
        html.Div([
            html.P("Để tính tỷ lệ lạm phát cho một năm nhất định, chỉ số CPI sẽ hữu ích, nhưng nó chỉ tính từ năm 1913. Nếu bạn muốn tìm tỷ lệ lạm phát lịch sử trước đó, các nhà phân tích lấy chỉ số giá hiện tại rồi trừ đi chỉ số giá tương đương dựa trên trên dữ liệu lịch sử cho năm đó."),
            dbc.Card([
                html.H1('🌀TIP:'),
                html.P('(Chỉ số giá năm 2 - Chỉ số giá năm 1) ÷ Chỉ số giá năm 1 x 100 = Tỷ lệ lạm phát năm 1'),
                html.P('Trong công thức này, chỉ số năm 2 hiện tại là chỉ số giá tiêu dùng ở thời điểm hiện tại và chỉ số năm trước đó là chỉ số giá tiêu dùng ở thời điểm trước đó. Khi áp dụng công thức này, kết quả sẽ cho biết tỷ lệ tăng trưởng của CPI trong một khoảng thời gian cụ thể, thường được biểu thị dưới dạng phần trăm.'),
                html.P('Lạm phát là sự gia tăng chung và liên tục của mức giá hàng hóa và dịch vụ trong một nền kinh tế. Khi lạm phát xảy ra, giá cả sẽ tăng, và tiền tệ mất giá trị theo thời gian. Điều này có thể xảy ra do nhiều yếu tố, như tăng trưởng kinh tế, chi tiêu chính phủ, biến động nguồn cung và yêu cầu hàng hóa và dịch vụ.'),
                html.P('Lạm phát có thể có những tác động tiêu cực đến nền kinh tế và người dân. Một mức lạm phát quá cao có thể làm giảm sức mua của người tiêu dùng, giảm độ tin cậy vào tiền tệ và gây ra không ổn định kinh tế. Tuy nhiên, một mức lạm phát ổn định có thể có lợi cho kinh tế bằng cách thúc đẩy đầu tư và tiêu dùng.'),

            ],style={'background-color':'#c3c3c36e','color':'red'})
        ])
    ],
    style={"padding": "20px"},
)
