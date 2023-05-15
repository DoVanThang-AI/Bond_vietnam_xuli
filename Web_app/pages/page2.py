from imports import *
url = 'https://assets3.lottiefiles.com/packages/lf20_i2eyukor.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
page_2_layout = html.Div([
    dbc.Container([
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
                                html.Li(dcc.Link("2.Phân bổ tài sản", href="/",style={'font-size':'12px'})),
                                html.Li(dcc.Link("3.Tổng quan định giá trái phiếu", href="/page-3",style={'font-size':'12px'})),
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
        html.H1("Phân bổ tài sản",style={'text-align':'left','color':'#99A3A4'}),
        html.Br(),
        html.P("Phân tài sản liên quan đến việc phân chia các khoản đầu tư của bạn cho các tài sản khác nhau, chẳng hạn như cổ phiếu, trái phiếu và tiền mặt. Quyết định về Phân bổ tài sản là quyết định cá nhân. Khoản phân bổ phù hợp nhất với bạn sẽ thay đổi vào những thời điểm khác nhau trong cuộc đời bạn, tùy thuộc vào thời gian bạn phải đầu tư và khả năng chấp nhận rủi ro của bạn"),
        html.P("Các yếu tố cần xem xét bao gồm:"),
        html.P(children=[html.B("Thời gian"),"Khoảng thời gian của bạn là số tháng, số năm hoặc số thập kỷ bạn cần đầu tư để đạt được mục tiêu tài chính của mình. Các nhà đầu tư có thời hạn dài hơn có thể cảm thấy thoải mái khi thực hiện các khoản đầu tư rủi ro hơn hoặc biến động hơn. Những người có khoảng thời gian ngắn hơn có thể thích chấp nhận ít rủi ro hơn."]),
        html.P(children=[html.B("Chấp nhận rủi ro."),"Chấp nhận rủi ro là khả năng và sự sẵn sàng của bạn để mất một phần hoặc toàn bộ khoản đầu tư ban đầu của mình để đổi lấy lợi nhuận tiềm năng lớn hơn."]),html.Br(),html.Br(),
        html.H2("Đa dạng hóa là gì?",style={'color':'#99A3A4','text-align':'left'}), 
        html.P("Việc thực hành rải tiền giữa các khoản đầu tư khác nhau để giảm thiểu rủi ro được gọi là đa dạng hóa. Đa dạng hóa là một chiến lược có thể được tóm tắt gọn gàng là “Đừng bỏ tất cả trứng vào một giỏ."),html.Br(),
        html.P("Một cách để đa dạng hóa là phân bổ các khoản đầu tư của bạn vào các loại tài sản khác nhau. Trong lịch sử, cổ phiếu, trái phiếu và tiền mặt không tăng và giảm cùng một lúc. Các yếu tố có thể khiến một loại tài sản hoạt động kém có thể cải thiện lợi nhuận cho một loại tài sản khác. Mọi người đầu tư vào các loại tài sản khác nhau với hy vọng rằng nếu một người thua lỗ, những người khác sẽ bù đắp cho những khoản lỗ đó."),html.Br(),
        html.P("Bạn cũng sẽ đa dạng hóa tốt hơn nếu bạn dàn trải các khoản đầu tư của mình trong từng loại tài sản. Điều đó có nghĩa là nắm giữ một số cổ phiếu hoặc trái phiếu khác nhau và đầu tư vào các lĩnh vực công nghiệp khác nhau, chẳng hạn như hàng tiêu dùng, chăm sóc sức khỏe và công nghệ. Bằng cách đó, nếu một lĩnh vực hoạt động kém, bạn có thể bù đắp nó bằng các khoản nắm giữ khác trong các lĩnh vực đang hoạt động tốt."), html.Br(),
        html.P("Một số nhà đầu tư thấy việc đa dạng hóa dễ dàng hơn bằng cách sở hữu các quỹ tương hỗ. Quỹ tương hỗ là một công ty tập hợp tiền từ nhiều nhà đầu tư và đầu tư tiền vào cổ phiếu, trái phiếu và các sản phẩm tài chính khác. Các quỹ tương hỗ giúp các nhà đầu tư dễ dàng sở hữu một phần nhỏ trong nhiều khoản đầu tư. Ví dụ, một quỹ chỉ số thị trường chứng khoán tổng sở hữu cổ phiếu của hàng nghìn công ty, mang lại nhiều sự đa dạng hóa cho một khoản đầu tư."),html.Br(),
        html.P("Một quỹ tương hỗ không nhất thiết phải đa dạng hóa, đặc biệt nếu nó chỉ tập trung vào một lĩnh vực công nghiệp. Nếu bạn đầu tư vào các quỹ tương hỗ tập trung hẹp, bạn có thể cần đầu tư vào một số quỹ để đa dạng hóa. Khi bạn thêm nhiều khoản đầu tư vào danh mục đầu tư của mình, bạn có thể sẽ phải trả thêm phí và chi phí, điều này sẽ làm giảm lợi tức đầu tư của bạn. Vì vậy, bạn sẽ cần xem xét các chi phí này khi quyết định cách tốt nhất để đa dạng hóa danh mục đầu tư của mình."),html.Br(),
        html.H2("Tái cân bằng là gì?",style={'color':'#99A3A4','text-align':'left'}),html.Br(),
        html.P("Tái cân bằng là những gì các nhà đầu tư làm để đưa danh mục đầu tư của họ trở lại hỗn hợp phân bổ tài sản ban đầu. Tái cân bằng là cần thiết vì theo thời gian, một số khoản đầu tư sẽ tăng trưởng nhanh hơn những khoản đầu tư khác. Điều này có thể đẩy các khoản nắm giữ của bạn không phù hợp với mục tiêu đầu tư của bạn. Bằng cách tái cân bằng, bạn sẽ đảm bảo rằng danh mục đầu tư của mình không vượt quá một danh mục tài sản cụ thể và bạn sẽ đưa danh mục đầu tư của mình trở lại mức rủi ro dễ chịu."),html.Br(),
        html.P("Ví dụ: bạn có thể bắt đầu với 60% danh mục đầu tư của mình đầu tư vào cổ phiếu, nhưng sau đó sẽ tăng lên 80% do thị trường tăng giá. Để thiết lập lại tổ hợp sản phẩm Phân bổ tài nguyên ban đầu, bạn sẽ cần bán một số cổ phiếu của mình hoặc đầu tư vào các loại tài sản khác."),html.Br(),
        html.P(children=[html.B("Có ba cách bạn có thể cân bằng lại danh mục đầu tư của mình:")]),
        html.P(" 1. Bạn có thể bán các khoản đầu tư mà tài sản nắm giữ của bạn vượt quá tỷ trọng và sử dụng số tiền thu được để mua các khoản đầu tư cho các loại tài sản bị thiếu tỷ trọng"),
        html.P(" 2.Bạn có thể mua các khoản đầu tư mới cho các loại tài sản thiếu trọng số."),
        html.P(" 3.Nếu bạn đang tiếp tục thêm vào các khoản đầu tư của mình, bạn có thể thay đổi các khoản đóng góp của mình để nhiều hơn nữa được chuyển vào các danh mục tài sản thiếu trọng lượng cho đến khi danh mục đầu tư của bạn cân bằng trở lại."),html.Br(),

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
    ],fluid=True)
],style={'background-color':'#F4F6F6'})