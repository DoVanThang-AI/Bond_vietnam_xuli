from imports import *
url = 'https://assets3.lottiefiles.com/packages/lf20_i2eyukor.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
''' PAGE 3 have '''
page_3_layout = html.Div([
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
                                html.Li(dcc.Link("3.Tổng quan định giá trái phiếu", href="/",style={'font-size':'12px'})),
])
                        ],style={'background-color':'#00325b'}),
                        ],className="submenu")
                ],className="has-submenu"),
                html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/page-4",style={'font-size':'15px'})),
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
        # comment taij day
        html.H3("Tìm hiểu tổng quan về định giá trái phiếu?",style={'color':'#99A3A4','text-align':'left'}),
        html.Img(src="https://ibond.com.vn/wp-content/uploads/2022/05/Tim-hieu-tong-quan-ve-dinh-gia-trai-phieu.jpg",style={'width':'100%','height':'400px'}),
        html.P("Định giá trái phiếu là việc xác định giá trị thực của một trái phiếu. Giá trị này bằng với giá trị hiện tại (hiện giá) của tất cả các dòng tiền nhận được trong tương lai được chiết khấu theo một lãi suất hợp lý."),html.Br(),
        html.P("Lãi suất chiết khấu khi định giá trái phiếu là lãi suất thị trường của một trái phiếu cụ thể. Đây cũng là lãi suất yêu cầu của nhà đầu tư. Lãi suất này thường được tính dựa trên lãi suất của trái phiếu chính phủ có cùng kỳ hạn và thời điểm đáo hạn, cộng thêm phần bù rủi ro."),html.Br(),

        html.H3("Quy trình định giá trái phiếu đến quyết định giao dịch",style={'color':'#99A3A4','text-align':'left'}),
        html.Img(src="https://ibond.com.vn/wp-content/uploads/2022/05/Quy-trinh-dinh-gia-trai-phieu-den-quyet-dinh-giao-dich.jpg",style={'width':'100%','height':'400px'}),html.Br(),
        html.P("Ước lượng dòng tiền sinh ra từ tài sản (thu nhập kỳ vọng)."),
        html.P("Ước lượng tỷ suất lợi nhuận NĐT yêu cầu (=lãi suất phi rủi ro +phần gia tăng do rủi ro)."),
        html.P("Lựa chọn mô hình định giá thích hợp để áp dụng. Tính hiện giá dòng tiền tệ thu nhập theo tỷ suất lợi nhuận vừa ước lượng."),
        html.P("So sánh giá trị lý thuyết vừa định ra so với giá trị thị trường."),
        html.P("Quyết định đầu tư (mua hay bán)."),

        html.Img(src="https://ibond.com.vn/wp-content/uploads/2022/05/Dinh-gia-trai-phieu-co-ky-han-va-khong-huong-loi-tuc-dinh-ky-Zero-coupon.jpg",style={'width':'100%','height':'400px'}),html.Br(),
        html.P("Zero – coupon là loại trái phiếu không được trả lợi tức định kỳ. Và người tham gia sẽ được mua nó với giá thấp hơn nhiều so với mệnh giá. Với loại trái phiếu này, lãi suất trái phiếu sẽ bằng 0 nên tất cả các khoản lợi tức I cũng sẽ bằng 0."),
    
    ],style={'margin':'0px 400px 0px 400px'}),
    html.Br(),
        dbc.Row(
            [
                dbc.Col([
                    html.H6('About',style={'color':'white'}),
                    html.P("This is a website that provides information on Vietnamese bonds and is calculated with many statistics so that investors can give investment advice to reduce financial risks.",style={'color':'white'})

                    
                ],className="col-3"),
                #dich vu
                dbc.Col([
                    html.H6("Device",style={'color':'white'}),
                    html.A('Investor information', href='https://www.hnx.vn/vi-vn/thong-tin-nha-dau-tu-gt.html',target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.A('Media Center', href="https://www.hnx.vn/trung-tam-truyen-thong-bc.html", target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.A('Procedure Guide',href='https://www.hnx.vn/huong-dan-thu-tuc.html', target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.A('Information service', href="https://www.hnx.vn/dich-vu-cctt.html", target="_blank",style={'font-size':'10px','text-align':'center'})

                ],className="col-3"),
                #tintuc
                dbc.Col([
                    html.H6("News"),
                    html.A('Event activities', href='https://www.hnx.vn/tin-tuc-su-kien-hnx.html',target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.A('Social activities', href='https://www.hnx.vn/tin-tuc-su-kien-hdxh.html',target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),


                ],className="col-3"),
                #   Ketnoi
                dbc.Col([
                    html.H6("Connect"),
                    html.A('Gmail',  href="mailto:contact@example.com",target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.A('Twitter', href="https://twitter.com/",target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),

                    html.P('Address',style={'font-size':'10px','font-weight':'500'}),
                    html.P(' 12 Nguyễn Văn Bảo, Phường 4, Gò Vấp, Thành phố Hồ Chí Minh',style={'font-size':'10px','font-weight':'500','color':'red'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.P("telephone: (+84) 769803053",style={'font-size':'10px','font-weight':'500','color':'red'})
                ],className="col-3")
            ],className="footer")
],style={'background-color':'#F4F6F6'})