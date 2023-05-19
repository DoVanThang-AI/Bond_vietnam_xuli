from imports import *

dash.register_page(__name__, path='/bonds-analysis', name='Dashboard')
df = pd.read_csv('./data/VietnamGovernanceBonds.csv')
grid = dag.AgGrid(
    id="bond-table-grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth":125},
    columnSize="sizeToFit",
)


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
                dag.AgGrid(
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


''' Page 4 have '''
layout = dbc.Row([
        default_html
])