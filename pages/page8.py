from imports import *

url = 'https://assets3.lottiefiles.com/packages/lf20_i2eyukor.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

''' Page 4 have '''
page_8_layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.Img(src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Logo_IUH.png/800px-Logo_IUH.png",style={'height':'150px','width':'300px'})     
        ],className="col-4"),
        dbc.Col([ 
            html.Br(),
            # html.P("Viet Nam Bonds",style={'font-weight':'1000', 'text-align':'center','font-size':'80px'}),
        ],className="col-5"),
        dbc.Col([
            html.Div(de.Lottie(options=options, width="35%", height="25%", url=url))
        ],className='col-3')
        
    ],style={'background-image':'url(https://vnn-imgs-f.vgcloud.vn/2019/09/27/17/19.jpg)'}),
    html.Nav(
    [
        html.Ul(
            [
                html.Li([
                    html.A("Giới Thiệu Về trái phiếu", href="/",style={'font-size':'15px'}),
                    html.Ul([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Bắt đầu giới thiệu"),
                                html.Li(dcc.Link("1.Thị Trường trái phiếu là gì?", href="/page-1",style={'font-size':'12px'})),
                                html.Li(dcc.Link("2.Phân bổ tài sản", href="/page-2",style={'font-size':'12px'})),
                                html.Li(dcc.Link("3.Tổng quan định giá trái phiếu", href="/page-3",style={'font-size':'12px'})),
                            ])
                        ],style={'background-color':'#00325b'}),
                        ],className="submenu")
                ],className="has-submenu"),

               html.Li([
                    html.A("Công cụ tính toán", href="#",style={'font-size':'15px'}),
                    html.Ul([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Bắt đầu giới thiệu"),
                                html.Li(dcc.Link("Trái phiếu chính phủ", href="/page-4",style={'font-size':'12px'})),
                                html.Li(dcc.Link("Trái phiếu doanh nghiệp", href="/",style={'font-size':'12px'})),
                               
                            ])
                        ],style={'background-color':'#00325b'}),
                        ],className="submenu")
                ],className="has-submenu"),
                # html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/",style={'font-size':'15px'})),
                html.Li(dcc.Link("Trung Tâm Truyền Thông", href="/page-5",style={'font-size':'15px'})),
                html.Li(dcc.Link("Báo cáo thị trường trái phiếu     ", href="/page-6",style={'font-size':'15px'})),
                html.Li(dcc.Link("Tin tức",href="/page-7",style={'font-size':'15px'}))
            ],
            className="navbar-nav mr-auto",
        ),
    ],
    className="navbar navbar-expand-lg",
    ),
    html.Br(),
    dbc.Row([
        html.H1("this is page 4   have contents!!!"),
        html.H1("tính công thức trái phiếu doanh nghiệp tại đây")
    ])
],style={'background-color':'#F4F6F6'})