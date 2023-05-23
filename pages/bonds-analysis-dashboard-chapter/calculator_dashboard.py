from imports import *


from utils.funtions_cal import Yield_to_marturity,laisuat,df_modified,Data_table
from utils.Cal_index_ import ytm_layout,duration_bond, yield_to_call,evalue_bonds,BEY_bonds,coupon_rate_bonds,coupon_payments_bonds,risk_adjusted_bonds,zero_coupon_bonds
import dash_ag_grid
import dash_ag_grid as grid

dash.register_page(__name__, path='/bonds-analysis/calculator', name='Bonds Calculator')

df = pd.read_csv('./data/VietnamGovernanceBonds.csv')


prices_bonds = html.Div([

    html.Div(
            [
                html.Div([
                    html.H1("Face value"),
                html.Div(
                    [
                        html.Label("Mệnh giá:"),
                        dcc.Input(id="par-value", type="number", value=100000),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Annual coupon rate:"),
                        dcc.Input(id="interest-rate", type="number", value=7.83),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div([
                    html.Label('YTM (%):'),
                    dcc.Input(id='YTM',type="number", value = 10.81)
                ],style={"marginBottom": "10px"}),
                html.Div(
                    [
                        html.Label("Year to maturity(years):"),
                        dcc.Input(id="maturity-time", type="number", value=5),
                    ],
                    style={"marginBottom": "10px"},
                ),
                html.Div(
                    [
                        html.Label("Coupon frequency:"),
                        dcc.Dropdown(
                            id="maturity-frequency",
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
                html.Button("Calculate", id="calculate-button", n_clicks=0),
                html.Div(id="result"),
                html.Br(),
                ]),

                
                html.Div(dcc.Graph(id ='chart_bonds',figure={}),style={'width':'70%'})
           
            ],style={'display':'flex'}
        ),
        html.Hr(),
        html.Div([
            html.H3("Đầu vào của giá trị hiện tại của trái phiếu "),
            html.Br(),
            html.P(children=[html.B("Mệnh giá:"), "Giá mà trái phiếu giao dịch hôm nay"],style={'color':'black'}),
            html.P(children=[html.B("lãi suất hàng năm:"), "Lãi suất hàng năm của trái phiếu nhận được"],style={'color':'black'}),
            html.P(children=[html.B("thời gian đáo hạn:"), "thời gian mà trái phiếu đó tới lúc đáo hạn"],style={'color':'black'}),
            html.P(children=[html.B("tần suất đáo hạn:"), "số lần mà nhận trả lãi bao nhiêu lần trong năm"],style={'color':'black'}),
            html.Hr(),
            html.Div([
                html.H3("Công thức toán học dùng trong tính giá hiện tại của trái phiếu"),
                dcc.Markdown('$\sum_{n=1}^{n} \dfrac{C}{(1+r)^{n}} + \dfrac{F}{(1+r)^{n}}$', mathjax=True,style={'text-align':'center','font-size':'x-large'}),
                html.Br(),
                html.P("Trong đó:"),
                html.P("F là đại diện cho mệnh giá"),
                html.P("n là số năm còn lại từ thời điểm hiện tại cho đến khi đáo hạn"),
                html.P("C là tỷ lệ coupon"),
                html.P("r là biểu thị tỷ suất sinh lời"),
                html.P("Bond price về về cơ bản là tính toán giá trị hiện tại của dòng tiền trong tương lai có thể xảy ra, bao gồm các khoản thanh toán phiếu lãi và mệnh giá là số tiền mua lại khi đáo hạn")
            ],style={'align-items':'center'}),
            html.Hr(),
            html.Div([
                html.P(children=[html.B("1.Xác định mệnh giá")," Đây face valuelà khoản thanh toán bong bóng mà nhà đầu tư trái phiếu sẽ nhận được khi trái phiếu đáo hạn. Ví dụ của chúng tôi, nó là face = $1,000."]),
                html.P(children=[html.B("2. Tính tiền lãi mỗi kỳ")," Để tính toán coupon per period, bạn sẽ cần hai đầu vào, cụ thể là coupon ratevà frequency.", html.Br(), " coupon per period = face value × coupon rate / frequency"]),
                html.P(children=[html.B("3. Xác định số năm đáo hạn"),' Là nsố năm tính từ thời điểm hiện tại đến khi trái phiếu đáo hạn.']),
                html.P(children=[html.B("4. Xác định lợi suất đáo hạn (YTM)"),' Là YTMtỷ suất lợi nhuận hàng năm mà nhà đầu tư trái phiếu sẽ nhận được nếu họ nắm giữ trái phiếu từ bây giờ đến khi nó đáo hạn. Trong ví dụ này, YTM = 10.81%.'])
            ])
            

        ])
])


#End
''' Page 4 have '''
layout = dbc.Row([
            dbc.Col([

                    html.H1("Calculator", className="mt-4 mb-4 ", style={'text-align':'center', 'font-size':'2rem', 'font-weight':'700'}),




                    html.Ul(
                        [
                            html.Li(html.A("Bond Price", id="element1", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Yield", id="element2", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Term Bonds", id = "element3", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Yield to Call", id = "element4", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Evaluate Bonds", id = "element5", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Bond Equivalent Yield", id = "element6", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Calculate Coupon rate", id = "element7", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Payment coupon", id = "element8", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("risk-adjusted return", id = "element9", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center'}),
                            html.Li(html.A("Zero Coupon Bond Value Calculator", id = "element10", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','height':'80px'}),
                        ]
                        
                    ),
            ],className='col-3 p-4 ml-2',style={'background-color':'whitesmoke','border-radius':'25px'}),
    
    # dbc.Row([
    #     dbc.Col([
    #         html.Div(
    #         [
    #             html.H2("Công cụ tính toán",style={'color':'black'}),
    #             html.Ul(
    #                 [
    #                     html.Li(html.A("Bond price ", id="element1", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','text-font':'15px'}),
    #                     html.Li(html.A("YTM", id="element2", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','text-font':'15px'}),
    #                     html.Li(html.A("Thời hạn trái phiếu", id = "element3", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','text-font':'15px'}),
    #                     html.Li(html.A("Lợi tức trái phiếu để gọi", id = "element4", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','text-font':'15px'}),
    #                     html.Li(html.A("Đánh giá trái phiếu", id = "element5", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','text-font':'15px'}),
    #                     html.Li(html.A("Lợi tức tương đương", id = "element6", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','text-font':'15px'}),
    #                     html.Li(html.A("Calculate Coupon rate", id = "element7", n_clicks=0,style={'font-size':'15px'}),style={'color':'black','background-color':'white','border-radius':'150px','text-align':'center','text-font':'15px'}),
    #                 ]
                    
    #             ),
    #         ],
        
    #     ),
    #     ],className="col-3",style={'background-color':'whitesmoke','border-radius':'25px'}),
   
        dbc.Col([
           
            html.Div(id="content-area"),


        ],className="col-8"),#,style={'background-color':'whitesmoke','border-radius':'25px','margin':'0px 20px'}
   
    ],style={'margin':'0px 10px 0px 200px'}),


default_html = html.Div([
    dbc.Container([
        html.H3("1. Trái phiếu Doanh nghiệp"),
        html.Div([
            dbc.Row([
            html.H3("Tần suất của lãi suất trái phiếu doanh nghiệp Techcombank",style={'text-align':'center'}),
            html.Div(children=dbc.DropdownMenu(
                children=[
                    dcc.Checklist(
                        id ='drop_menu',
                        options=[
                            {
                                "label":html.Div([
                                    html.Div(x)
                                ],style={'text-align':'center','display': 'flex', 'align-items': 'center', 'justify-content': 'center','overflow-x': 'hidden'}),
                                "value":x
                            }for x in laisuat['Tổ chức phát hành'].unique()
                        ],
                        value=[x for x in laisuat['Tổ chức phát hành'].unique()]
                    ),
                    html.Button(
                                            className='button btn btn-primary btn-sm',
                                            id='all-or-none',
                                            n_clicks=1,
                                            children="Select/Unselect All"
                                    )
                ],label="choose Cty",
            ))
        ]),
        html.Br(),
        dbc.Row([
            dcc.Graph(id="tansuatlai_graph", figure={})
        ],style={'margin':'0px 20px'}),
        ],style={'background-color':'whitesmoke','border-radius':'25px','margin':'0px 20px'}),
        html.Br(),
        
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.H3("Moduration_duration - Rate",style={'text-align':'center'}),
                    html.Div(children=dbc.DropdownMenu(
                children=[
                    dcc.Checklist(
                        id ='drop_menu_layer2',
                        options=[
                            {
                                "label":html.Div([
                                    html.Div(x)
                                ],style={'text-align':'center','display': 'flex', 'align-items': 'center', 'justify-content': 'center','overflow-x': 'hidden'}),
                                "value":x
                            }for x in laisuat['Tổ chức phát hành'].unique()
                        ],
                        value=[x for x in laisuat['Tổ chức phát hành'].unique()]
                    ),
                    html.Button(
                                            className='button btn btn-primary btn-sm',
                                            id='all-or-none_layer2',
                                            n_clicks=1,
                                            children="Select/Unselect All"
                                    )
                ],label="choose Cty",
            )),
            html.Br(),
            html.Div([
                dcc.Graph(id ='chart_layer2', figure={})
            ])

                ],className='col-9',style={'background-color':'whitesmoke','border-radius':'25px','margin':'0px 20px'}),
                dbc.Col([
                    # html.P("Thật cân nhắc khi quản lý rủi ro")
                ],style={'background-color':'whitesmoke','border-radius':'25px','margin':'0px 20px','writing-mode': 'vertical-rl'},)
        
            ],style={'display':'flex'})
        ]),
        html.Br(),
        html.Div([
            dbc.Row([
                dash_ag_grid.AgGrid(
                    # id='ag-grid',
                    columnDefs=[{'headerName': col, 'field': col} for col in Data_table.columns],
                    rowData=Data_table.to_dict('records'),
                    # enableFilter=True
                )
            ])
        ]),
        html.Br(),
        html.H3("2. Trái phiếu Chính Phủ"),
        ######################################VIEt web 
        html.Div([
            dbc.Row(
                dbc.Col(
                    [
                        # dropdown
                        dcc.Dropdown(id='currency-dropdown', options=[
                            {'label': c, 'value': c} for c in df['currency_type'].unique()
                        ], value='VND'),
                    ], width=12,
                ),  className='mt-2'
            ),

            dbc.Row(
                
                    dbc.Col(
                        [
                        # charts
                        dcc.Graph(id="volume-chart", className='rounded overflow-hidden'),
                    ] , width=12,
                ), className='mt-2'
                
            ),

            dbc.Row(
                [ 
                    dbc.Col(
                        [
                            dcc.Graph(id="payment-chart", className='rounded overflow-hidden'),
                        ], width=4,
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id="rate-histogram", className='rounded overflow-hidden'),
                        ], width=8, 
                    ),
                ]
                , className='gx-2 mt-2'
            ),

            dbc.Row(   
                [
                    dbc.Col(
                        [
                            # table 
                            html.Div([grid], style={'height': '100%', 'width': '100%'}, className='rounded overflow-hidden'),
                        ], width=12
                    ) 
                ], className='mt-2'
            ),
        ])
       ############################################done viet wweb
    ],fluid=True)
])



@callback(
    Output("content-area", "children"),
    [Input("element1", "n_clicks"), Input("element2", "n_clicks"),Input("element3", "n_clicks"),Input("element4", "n_clicks"),Input("element5", "n_clicks"),Input("element6", "n_clicks"),Input("element7", "n_clicks"),Input("element8", "n_clicks"),Input("element9", "n_clicks"),Input("element10", "n_clicks")],
)
def display_content(element1_clicks, element2_clicks,element3_clicks,element4_clicks,element5_clicks,element6_clicks,element7_clicks,element8_clicks,element9_clicks,element10_clicks):
    ctx = dash.callback_context

    if not ctx.triggered:
        return prices_bonds

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]


    if triggered_id == "element1":
        return prices_bonds
    elif triggered_id == "element2":
        return ytm_layout
    elif triggered_id == "element3":
        return duration_bond
    elif triggered_id == "element4":
        return yield_to_call
    elif triggered_id =="element5":
        return evalue_bonds
    elif triggered_id =="element6":
        return BEY_bonds
    elif triggered_id =="element7":
        return coupon_rate_bonds
    elif triggered_id =="element8":
        return coupon_payments_bonds
    elif triggered_id =="element9":
        return risk_adjusted_bonds
    elif triggered_id =="element10":
        return zero_coupon_bonds
    else:
        return html.Div()
    
@callback(
   
    [Output("result", "children"),
    Output("chart_bonds",'figure'),
    ],
    [Input("calculate-button", "n_clicks")],
    [
        State("par-value", "value"),
        State("interest-rate", "value"),
        State('YTM','value'),
        State("maturity-time", "value"),
        State("maturity-frequency", "value"),
    ],
)
def calculate_present_value(n_clicks,face_vl,coupon,Yield,Time,per_time):
    if n_clicks >1:

        Data = pd.DataFrame()
        coupon_payment = [(coupon/per_time)/100*face_vl]*(Time*per_time-1)+[(coupon/per_time)/100*face_vl+face_vl]
        total_payment = Time*per_time
        Data['period']=pd.DataFrame(np.arange(1,total_payment+1),columns = ['Periods'])
        Data['Coupon_payment']= pd.DataFrame(coupon_payment)
        Data['D_CP']=Data['Coupon_payment'] / ((1+(Yield/per_time)/100) ** Data['period'])
        Data['PV/Total_DCP']= Data['D_CP']*Data['period'] / Data['D_CP'].sum()
        fig = px.bar(Data["period"], y = Data['D_CP'], template="plotly_white")
        fig.update_layout(title=f'Present value of payment {per_time} of year',
                      xaxis_title='Present values of payments',
                      yaxis_title='Amount of Money')
        fig.update_traces(
                      hovertemplate='kỳ lãi: %{x}<br>Giá trị: %{y}<extra></extra>')
        
        return f"giá trị trái phiếu là :{round(Data['D_CP'].sum(),2)} VND",fig
 


    
#BEGIN
@callback(Output('drop_menu', 'value'),
              [Input('all-or-none', 'n_clicks')],
              [Input('drop_menu', 'options')])
def select_all_none(all_selected, options):
    if all_selected % 2 == 0:
        all_or_none1 = []
        return all_or_none1
    else:
        all_or_none1 = [option['value'] for option in options if all_selected]
        return all_or_none1
  

@callback(
    Output('tansuatlai_graph','figure'),
    Input('drop_menu','value')
)

def update(crypto):
    laisuat_df = laisuat[laisuat['Tổ chức phát hành'].isin(crypto)]
    fig = px.bar(x = laisuat_df['Lãi suất'], y =laisuat_df['count'],color=laisuat_df['Tổ chức phát hành'],height=400)

    fig.update_xaxes(type='category')
    fig.update_layout(font=dict(size=10),template="plotly_white")
    fig.update_yaxes(gridwidth=1,mirror="ticks",showgrid=True,title="Value")
    fig.update_layout(  legend=dict(
                orientation="h",
                # entrywidth=70,
                yanchor="middle",
                y=-0.3,
                xanchor="center",
                x=0.5,
            ),margin=dict(l=20, r=20, t=10, b=20))
    fig.update_traces(hovertemplate ='%{label:label}'+ '<br>%{text}',textposition = "none")
    fig.update_layout(   
        paper_bgcolor='#F2F3F4',
        plot_bgcolor='#F2F3F4')
    fig.update_layout(hovermode="x unified",font=dict(size=10))
    return fig

#layer2
#BEGIN
@callback(Output('drop_menu_layer2', 'value'),
              [Input('all-or-none_layer2', 'n_clicks')],
              [Input('drop_menu_layer2', 'options')])
def select_all_none(all_selected, options):
    if all_selected % 2 == 0:
        all_or_none1 = []
        return all_or_none1
    else:
        all_or_none1 = [option['value'] for option in options if all_selected]
        return all_or_none1
  

@callback(
    Output('chart_layer2','figure'),
    Input('drop_menu_layer2','value')
)

def update(cty):
    modified = df_modified[df_modified['Tổ chức phát hành'].isin(cty)]
    fig = px.bar(x = modified['Lãi suất'], y = modified['Modified_duration'], color= modified['Tổ chức phát hành'])
    fig.update_xaxes(type='category')
    fig.update_layout(
        xaxis_title="Lãi suất", yaxis_title="Modified_duration"
        
    )
    fig.update_traces(hovertemplate='Lãi suất: %{x}<br>Modified_duration: %{y}')
    fig.update_layout(font=dict(size=10),template="plotly_white")
    fig.update_xaxes(rangeselector_font_color='#000000',# rangeslider_visible=True,
                    ticks= "outside",
                    ticklabelmode= "period", 
                    ticklen=12,
                
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1D", step="day", stepmode="backward"),
                    dict(count=7, label="1W", step="day", stepmode="backward"),
                    dict(count=1,label="1M", step="month", stepmode="backward"),
                    dict(count=3,label="3M", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
            ])
        )  )
    fig.update_yaxes(gridwidth=1,mirror="ticks",showgrid=True,title="Value")
    fig.update_layout(  legend=dict(
                orientation="h",
                # entrywidth=70,
                yanchor="middle",
                y=-0.6,
                xanchor="center",
                x=0.5,
            ),margin=dict(l=20, r=20, t=10, b=20))
    fig.update_traces(hovertemplate ='%{label:label}'+ '<br>%{text}',textposition = "none")
    fig.update_layout(   
        paper_bgcolor='#F2F3F4',
        plot_bgcolor='#F2F3F4')
    fig.update_layout(hovermode="x unified",font=dict(size=10))
    return fig

# callback cal YTM
# Callback function to calculate the bond yields
@callback(
    [dash.dependencies.Output('current-yield-result', 'children'),
     dash.dependencies.Output('yield-to-maturity-result', 'children')],
    [dash.dependencies.Input('calculate-button', 'n_clicks')],
    [dash.dependencies.State('current-price', 'value'),
     dash.dependencies.State('face-value', 'value'),
     dash.dependencies.State('interest-rate', 'value'),
     dash.dependencies.State('maturity-years', 'value')]
)
def calculate_yields(n_clicks, current_price, face_value, interest_rate, maturity_years):
    if n_clicks is None:
        return None, None
       
    
    # Perform yield calculations
    coupon_payment = (face_value * interest_rate) / 100
    current_yield = coupon_payment / current_price
    yield_to_maturity = (coupon_payment + (face_value - current_price) / maturity_years) / ((current_price + face_value) / 2)
    
    return f"{current_yield:.2%}", f"{yield_to_maturity:.2%}"
    

# call back is duration bonds
@callback(
   
    Output("result_layer3", "children"),
    [Input("calculate-button_layer3", "n_clicks")],
    [
        State("par-value_layer3", "value"),
        State("interest-rate_layer3", "value"),
        State('YTM_layer3','value'),
        State("maturity-time_layer3", "value"),
        State("maturity-frequency_layer3", "value"),
    ],
)
def calculate_present_value(n_clicks,face_vl,coupon,Yield,Time,per_time):
    # if n_clicks >1:
    if n_clicks is None:
        return None, None

    Data = pd.DataFrame()
    coupon_payment = [(coupon/per_time)/100*face_vl]*(Time*per_time-1)+[(coupon/per_time)/100*face_vl+face_vl]
    total_payment = Time*per_time
    Data['period']=pd.DataFrame(np.arange(1,total_payment+1),columns = ['Periods'])
    Data['Coupon_payment']= pd.DataFrame(coupon_payment)
    Data['D_CP']=Data['Coupon_payment'] / ((1+(Yield/per_time)/100) ** Data['period'])
    Data['PV/Total_DCP']= Data['D_CP']*Data['period'] / Data['D_CP'].sum()
    Duration = Data['PV/Total_DCP'].sum()/per_time
    Modified_Duration = Duration / (1+(Yield/per_time)/100)
    result = html.Div([
        dbc.Card([
            html.P(f"Một trái phiếu có mệnh giá {face_vl} với lãi suất hàng năm {coupon}, lợi suất đáo hạn là {Yield}, với thời gian đáo hạn là {Time} với tần suất trả lãi {per_time} trong năm thì có thời hạn là : {Modified_Duration}")
        ],style={'background-color': 'antiquewhite','border-radius':'20px'})
    ])
    return result
    # return f"Một trái phiếu có mệnh giá {face_vl} với lãi suất hàng năm {coupon}, lợi suất đáo hạn là {Yield}, với thời gian đáo hạn là {Time} với tần suất trả lãi {per_time} trong năm thì có thời hạn là : {Modified_Duration}"

# yield to call call back
@callback(
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
    if n_clicks is None:
        return None, None
    yield_to_call = (annual_coupon_rate*10+((call_price-bond_price)/years_to_call))/((call_price+bond_price)/interest_frequency)
    current_yield = (face_value*(annual_coupon_rate/100)/bond_price)
    result = html.Div([
            dbc.Card([

         
            html.P(children=[f"Một trái phiếu có giá hiện tại là: {bond_price}, mệnh giá là : {face_value}, giá gọi là : {call_price}, số năm gọi là : {years_to_call}, lãi suất hàng năm là: {annual_coupon_rate}, với tần suất trả lãi là: {interest_frequency} "]),
            html.P(f"Current Yield: {current_yield:.2%}"),
            html.P(f"Yield to Call: {yield_to_call:.2%}")
               ],style={'background-color': 'antiquewhite','border-radius':'20px'})
        ])
    return result


#++++++++++++++++++++++++++++++++++++Viet call back
@callback(
    Output("bond-table-grid", "children"), Input("bond-table-body", "cellClicked")
)
def display_cell_clicked_on(cell):
    if cell is None:
        return "Click on a cell"
    return f"clicked on cell value:  {cell['value']}, column:   {cell['colId']}, row index:   {cell['rowIndex']}"


@callback(
    Output("volume-chart", "figure"),
    [Input("currency-dropdown", "value")])
def update_volume_chart(currency):
    filtered_df = df[df['currency_type'] == currency]
    fig = px.line(filtered_df, x="bond_code", y="outstanding_volume", title="Outstanding Volume")
    return fig

@callback(
    Output("payment-chart", "figure"),
    [Input("currency-dropdown", "value")])
def update_payment_chart(currency):
    filtered_df = df[df['currency_type'] == currency]
    counts = filtered_df.groupby(["interest_payment_method", "interest_payment_type"]).size().reset_index(name="count")
    fig = px.pie(counts, values="count", names="interest_payment_type", hole=.3, title="Interest Payment Type")
    return fig

@callback(
    Output("rate-histogram", "figure"),
    [Input("currency-dropdown", "value")])
def update_rate_histogram(currency):
    filtered_df = df[df['currency_type'] == currency]
    fig = px.histogram(filtered_df, x="coupon_rate", nbins=20, title="Coupon Rate Distribution")
    return fig


@callback(
    Output("bond-table-body", "children"),
    [Input("currency-dropdown", "value")])
def update_bond_table(currency):
    filtered_df = df[df['currency_type'] == currency]
    rows = []
    for i in range(len(filtered_df)):
        row = html.Tr([
            html.Td(filtered_df.iloc[i]['bond_code']),
            html.Td(filtered_df.iloc[i]['issuance_date']),
            html.Td(filtered_df.iloc[i]['maturity_date']),
            html.Td(filtered_df.iloc[i]['remaining_tenor']),
            html.Td(filtered_df.iloc[i]['status'])
        ])
        rows.append(row)
    return rows

# callback evalute bonds

@callback(
   
    Output("result-eva", "children"),
 
    [Input("calculate-button-eva", "n_clicks")],
    [
        State('bond-price-eva','value'),
        State("par-value-eva", "value"),
        State("interest-rate-eva", "value"),
        State('YTM-eva','value'),
        State("maturity-time-eva", "value"),
        State("maturity-frequency-eva", "value"),
    ],
)
def calculate_present_value(n_clicks,bond_price,face_vl,coupon,Yield,Time,per_time):
    if n_clicks >1:

        Data = pd.DataFrame()
        coupon_payment = [(coupon/per_time)/100*face_vl]*(Time*per_time-1)+[(coupon/per_time)/100*face_vl+face_vl]
        total_payment = Time*per_time
        Data['period']=pd.DataFrame(np.arange(1,total_payment+1),columns = ['Periods'])
        Data['Coupon_payment']= pd.DataFrame(coupon_payment)
        Data['D_CP']=Data['Coupon_payment'] / ((1+(Yield/per_time)/100) ** Data['period'])
        Data['PV/Total_DCP']= Data['D_CP']*Data['period'] / Data['D_CP'].sum()
        present_value = round(Data['D_CP'].sum(),2)
         # Đánh giá trái phiếu dựa trên giá trị hiện tại
        if bond_price < present_value:
            return html.Div([
            dbc.Card([

         
            html.P(children=[f"Một trái phiếu có giá hiện tại là: {bond_price} VND, mệnh giá là : {face_vl} VND,lãi suất là: {coupon}, với YTM là: {Yield} với số năm đáo hạn là : {Time}, tần suất trả lãi mỗi năm : {per_time} lần "]),
            html.P(f"Trái phiếu định giá thấp hơn giá trị hiện tại là : {present_value} VND")
               ],style={'background-color': 'antiquewhite','border-radius':'20px'})
        ])
        elif bond_price > present_value:
            return html.Div([
            dbc.Card([

         
            html.P(children=[f"Một trái phiếu có giá hiện tại là: {bond_price} VND, mệnh giá là : {face_vl } VND,lãi suất là: {coupon}, với YTM là: {Yield} với số năm đáo hạn là : {Time}, tần suất trả lãi mỗi năm : {per_time} lần "]),
            html.P(f"Trái phiếu định giá cao hơn giá trị hiện tại là : {present_value} VND")
               ],style={'background-color': 'antiquewhite','border-radius':'20px'})
        ])
        else:
            return html.Div([
            dbc.Card([

         
            html.P(children=[f"Một trái phiếu có giá hiện tại là: {bond_price} VND, mệnh giá là : {face_vl} VND,lãi suất là: {coupon}, với YTM là: {Yield} với số năm đáo hạn là : {Time}, tần suất trả lãi mỗi năm : {per_time} lần "]),
            html.P(f"Trái phiếu định giá gần bằng giá trị hiện tại là : {present_value} VND")
               ],style={'background-color': 'antiquewhite','border-radius':'20px'})
        ])



# call back BEY bonds
@callback (
    Output("result-bey",'children'),
    [Input("calculate-button-bey",'n_clicks')],
    [
        State('bond-price-bey','value'),
        State('par-value-bey','value'),
        State('interest-rate-bey','value')
    ]
)
def update_calculator(n_clicks, bond_price, face_vl,time):
    if n_clicks > 1:
        BEY = (face_vl - bond_price) / bond_price * (365 / time)
        return html.Div([
            dbc.Card([
                html.P(f'Trái phiếu có giá là : {bond_price} với mệnh giá là :{face_vl} số ngày đến hạn là : {time} có lợi suất trái phiếu tương đương BEY là : {BEY:.2%}')
            ],style={'background-color': 'antiquewhite','border-radius':'20px'})
        ])
    
# coupon rate bonds
# callback coupon rate
@callback (
    Output("result-coupon",'children'),
    [Input("calculate-button-coupon",'n_clicks')],
    [
        State('par-value-coupon','value'),
        State('interest-rate-coupon','value'),
        State('maturity-frequency-coupon','value')
    ]
)
def update_calculator(n_clicks, face_vl,coupon_payment,frenquency):
    if n_clicks > 1:
        coupon_payments = coupon_payment*frenquency
        coupon_rate = coupon_payments / face_vl * 10
        return html.Div([
            dbc.Card([
                html.P(f"ta có 1 trái phiếu với mệnh giá là :{face_vl} VND với phiếu giảm giá mỗi kỳ là : {coupon_payment} VND với tần suất trả lãi: {frenquency} "),
                html.P(f'Phiếu giảm giá hàng năm là: {coupon_payments} VND'),
                html.P(f'lãi suất coupon là : {coupon_rate}%')
            ],style={'background-color': 'antiquewhite','border-radius':'20px'})
        ])
    
# coupon payemnt
@callback(
    Output("result-output-eight", "children"),
    [Input("calculate-button-eight", "n_clicks")],
    [
     dash.dependencies.State("face-value-eight", "value"),
     dash.dependencies.State("annual-interest-rate-eight", "value"),
     dash.dependencies.State("interest-frequency-dropdown-eight", "value")]
)
def calculate_yield(n_clicks, face_value, annual_coupon_rate, interest_frequency):
    if n_clicks is not None:
        annual_coupon_rate_t = annual_coupon_rate/100
        coupon_payment = (face_value*annual_coupon_rate_t)/interest_frequency
        result = html.Div([
            dbc.Card([
                html.P(f'Bond have face value is : {face_value}'),
                html.P(f'Bond have annual coupon rate is: {annual_coupon_rate}%'),
                html.P(f'Bond have payment frequency of year: {interest_frequency}'),
                html.P(f'Coupon payment is: {round(coupon_payment,2)} VNĐ')

            ],style={'background-color': 'antiquewhite','border-radius':'20px'})
        ])
        return result
    
#callback element9 risk-adjustes return 

@callback(
    Output("result-risk", "children"),
    [Input("calculate-button-risk", "n_clicks")],
    [
     dash.dependencies.State("pofolio-return", "value"),
     dash.dependencies.State("risk-free", "value"),
     dash.dependencies.State("standard", "value"),
     #B
     dash.dependencies.State("pofolio-return-b", "value"),
     dash.dependencies.State("risk-free-b", "value"),
     dash.dependencies.State("standard-b", "value"),
    ]
)
def calculate_yield(n_clicks,pofolio_A, risk_A,stand_A,profolio_B, risk_B,stand_B):
    if n_clicks is not None:
        Ctya = (pofolio_A - risk_A)/stand_A
        Ctyb = (profolio_B- risk_B)/stand_B
        if (pofolio_A > profolio_B) &(Ctya < Ctyb):
            result = html.Div([
                dbc.Card([
                    html.P('Tỷ lệ Sharpe'),
                    html.P(f'Quỹ tương hỗ (mutual fund) A: {Ctya} ',style={'color':'red'}),
                    html.P(f'Quỹ tương hỗ (mutual fund) B: {Ctyb} ',style={'color':'red'}),
                    html.P('Mặc dù Quỹ tương hỗ  (mutual fund)  A có lợi nhuận cao hơn, những Quỹ tương hỗ  (mutual fund)  B có lợi nhuận được điều chỉnh theo rủi ro cao hơn, nghĩa là kiếm được nhiều hơn trên mỗi đơn vị tổng rủi ro so với Quỹ tương hỗ  (mutual fund)  A')

                ],style={'background-color': 'antiquewhite','border-radius':'20px'})
            ])
            return result
        elif (pofolio_A < profolio_B) &(Ctya > Ctyb):
            result = html.Div([
                dbc.Card([
                    html.P('Tỷ lệ Sharpe'),
                    html.P(f'Quỹ tương hỗ (mutual fund) A: {Ctya} ',style={'color':'red'}),
                    html.P(f'Quỹ tương hỗ (mutual fund) B: {Ctyb} ',style={'color':'red'}),
                    html.P('Mặc dù Quỹ tương hỗ  (mutual fund)  B có lợi nhuận cao hơn, những Quỹ tương hỗ  (mutual fund)  A có lợi nhuận được điều chỉnh theo rủi ro cao hơn, nghĩa là kiếm được nhiều hơn trên mỗi đơn vị tổng rủi ro so với Quỹ tương hỗ  (mutual fund)  B')

                ],style={'background-color': 'antiquewhite','border-radius':'20px'})
            ])

            return result
        elif (pofolio_A > profolio_B) &(Ctya > Ctyb):
            result = html.Div([
                dbc.Card([
                    html.P('Tỷ lệ Sharpe'),
                    html.P(f'Quỹ tương hỗ (mutual fund) A: {Ctya} ',style={'color':'red'}),
                    html.P(f'Quỹ tương hỗ (mutual fund) B: {Ctyb} ',style={'color':'red'}),
                    html.P(['Quỹ tương hỗ  (mutual fund)  A có ', html.B("lợi nhuận cao hơn") , " và quỹ tương hỗ (mutual fund ) A lớn hơn B , nghĩa là A có ",html.B("lợi nhuận điều chỉnh theo rủi ro cao hơn")  ," nghĩa là kiếm được nhiều tiên hơn trên mỗi đơn vị tổng rủi ro với quỹ tương hỗ (mutual fund) B"])

                ],style={'background-color': 'antiquewhite','border-radius':'20px'})
            ])
        
            return result
        else:
            result = html.Div([
                dbc.Card([
                    html.P('Tỷ lệ Sharpe'),
                    html.P(f'Quỹ tương hỗ (mutual fund) A: {Ctya} ',style={'color':'red'}),
                    html.P(f'Quỹ tương hỗ (mutual fund) B: {Ctyb} ',style={'color':'red'}),
                    html.P('Quỹ tương hỗ  (mutual fund)  B có  lợi nhuận cao hơn, và quỹ tương hỗ (mutual fund ) B lớn hơn A , nghĩa là B có lợi nhuận điều chỉnh theo rủi ro cao hơn , nghĩa là kiếm được nhiều tiên hơn trên mỗi đơn vị tổng rủi ro với quỹ tương hỗ (mutual fund) A')

                ],style={'background-color': 'antiquewhite','border-radius':'20px'})
            ])
        
            return result 
            

#zero coupon

@callback(
    Output("result-zero", "children"),
    [Input("calculate-button-zero", "n_clicks")],
    [
     dash.dependencies.State("face-vl-zero", "value"),
     dash.dependencies.State("present-vl-zero", "value"),
     dash.dependencies.State("time-zero", "value"),
    ]
)
def calculate_yield(n_clicks,face_vl,present_vl,time):
    if n_clicks is not None:
        ketqua = pow((face_vl/present_vl),(1/time)) - 1
        result = html.Div([
            dbc.Card([
                html.P('Zero Coupon Bond Effective Yield: '),
                html.P(f'Trái phiếu có mệnh giá: {face_vl} ',style={'color':'red'}),
                html.P(f'Trái phiếu có giá trị hiện tại là: {present_vl} ',style={'color':'red'}),
                html.P(f'Trái phiếu có thời gian đáo hạn là : {time}'),
                html.P(f"Trái phiếu phiếu giảm giá bằng không Lợi tức hiệu quả: {ketqua:.2%}")

            ],style={'background-color':'#c3c3c36e','color':'red'})
        ])
    
        return result 