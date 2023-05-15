'''Page 5 here'''
from imports import *

url = 'https://assets3.lottiefiles.com/packages/lf20_i2eyukor.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
## Trung tâm truyền thông
page_5_layout = html.Div([
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
                html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/page-4",style={'font-size':'15px'})),
                html.Li(dcc.Link("Trung Tâm Truyền Thông", href="/")),
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
        html.H1("Trung tâm truyền thông",style={'text-align':'center','color':'#797D7F'}),
        html.Div([
            html.Img(src="https://owa.hnx.vn/ftp/PORTALNEW/HEADER_IMAGES/308022023030316.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("TTCK phái sinh tháng 1/2023: Giao dịch hợp đồng tương lai chỉ số VN30 giảm 35,72% so với tháng trước",href="https://www.hnx.vn/trung-tam-truyen-thong/chi-tiet-tin-bc-60015995-0.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Thị trường chứng khoán phái sinh có giao dịch sụt giảm khá mạnh trong tháng 1/2023. Trong bối cảnh sau khi VSD công bố điều chỉnh tỷ lệ ký quỹ ban đầu hợp đồng tương lai chỉ số VN30 tối thiểu từ 13% lên 17%, áp dụng từ ngày 15/12/2022, mặc dù chỉ số VN30 đóng cửa tháng 1/2023 tại mức 1,125.07 điểm, tăng 11,93% so với tháng 12/2022",style={'font-weight':'300'})
        ],style={'margin-bottom':'1.25rem'}),
        html.Hr(),
        html.Div([
            html.Img(src="https://owa.hnx.vn/ftp/PORTALNEW/HEADER_IMAGES/208022023093637.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Thị trường UPCoM tháng 1/2023: Nhà đầu tư nước ngoài mua ròng 64,9 tỷ đồng",href="https://www.hnx.vn/trung-tam-truyen-thong/chi-tiet-tin-bc-60015994-0.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Thị trường UPCoM tháng 1/2023 có diễn biến giao dịch kém sôi động với thanh khoản giảm đáng kể. Khối lượng giao dịch (KLGD) bình quân đạt xấp xỉ 36,82 triệu cổ phiếu/phiên, giảm 23,07% so với tháng 12/2022, đồng thời giá trị giao dịch (GTGD) bình quân đạt hơn 462 tỷ đồng/phiên, giảm 23,36%.",style={'font-weight':'300'})
        ],style={'margin-bottom':'1.25rem'}),
        html.Hr(),
        html.Div([
            html.Img(src="https://owa.hnx.vn/ftp/PORTALNEW/HEADER_IMAGES/108022023093712.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Thị trường cổ phiếu niêm yết HNX tháng 01/2023: NĐT nước ngoài mua ròng 334 tỷ đồng",href="https://www.hnx.vn/trung-tam-truyen-thong/chi-tiet-tin-bc-60015989-0.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Thị trường cổ phiếu niêm yết tại HNX tháng đầu tiên của năm 2023 có diễn biến giao dịch khá trầm lắng. Chỉ số HNX Index biến động trong biên độ hẹp. trong khoảng từ 210 – 220 điểm và đóng cửa đạt mức cao nhất tháng với 222,43 điểm vào ngày 31/01/2023, tăng 1,12% so với tháng 12/2022.",style={'font-weight':'300'})
        ],style={'margin-bottom':'1.25rem'}),
        html.Hr(),
        html.Div([
            html.Img(src="https://owa.hnx.vn/ftp/PORTALNEW/HEADER_IMAGES/ps%20t1004112022045024.png",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("TTCK phái sinh tháng 10/2022: Giao dịch hợp đồng tương lai chỉ số VN30 tăng 66,73% so với tháng trước",href="https://www.hnx.vn/trung-tam-truyen-thong/chi-tiet-tin-bc-60015470-0.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Chỉ số VN30 đóng cửa tháng 10/222 tại mức 1.026,84 điểm, giảm 10,86% so với tháng 9/2022. Trên thị trường chứng khoán phái sinh, hợp đồng tương lai chỉ số VN30 có giao dịch tang mạnh với khối lượng giao dịch bình quân đạt 423.041 hợp đồng/phiên, tăng 66,73% so với tháng trước, tương ứng giá trị giao dịch bình quân (theo danh nghĩa hợp đồng) đạt 43.566 tỷ đồng, tăng 39,89% so với tháng trước",style={'font-weight':'300'})
        ],style={'margin-bottom':'1.25rem'}),
        html.Hr(),
        html.Div([
            html.Img(src="https://owa.hnx.vn/ftp/PORTALNEW/HEADER_IMAGES/a02112022044709.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Thị trường cổ phiếu niêm yết HNX tháng 10/2022: Nhà đầu tư nước ngoài mua ròng hơn 481 tỷ đồng, mức lớn nhất từ đầu năm",href="https://www.hnx.vn/trung-tam-truyen-thong/chi-tiet-tin-bc-60015452-0.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Thị trường cổ phiếu niêm yết tại HNX có diễn biến giao dịch giảm mạnh trong tháng 10. Chỉ số HNX Index có xu hướng giảm, đan xen một số phiên phục hồi nhẹ và đóng cửa tháng 10/2022 đạt 210,43 điểm, giảm 15,91% so với tháng 9/2022.",style={'font-weight':'300'})
        ],style={'margin-bottom':'1.25rem'}),
        html.Hr(),
        html.Div([
            html.Img(src="https://owa.hnx.vn/ftp/PORTALNEW/HEADER_IMAGES/102112022043202.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Thị trường UPCoM tháng 10/2022: Giá trị vốn hóa thị trường giảm 11,42%",href="https://www.hnx.vn/trung-tam-truyen-thong/chi-tiet-tin-bc-60015448-0.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Thị trường UPCoM tháng 10/2022 chứng kiến mức giảm đáng kể cả về khối lượng và giá trị giao dịch. Khối lượng giao dịch (KLGD) bình quân đạt xấp xỉ 32,99 triệu cổ phiếu/phiên, giá trị giao dịch (GTGD) bình quân đạt hơn 476 tỷ đồng/phiên, giảm lần lượt 23,21% về khối lượng giao dịch và 34,07% về giá trị giao dịch so với tháng trước.",style={'font-weight':'300'})
        ],style={'margin-bottom':'1.25rem'}),
    ],style={'margin':'0px 400px 0px 400px'})
],style={'background-color':'#F4F6F6'})
