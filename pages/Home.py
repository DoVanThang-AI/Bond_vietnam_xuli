from imports import *

url = 'https://assets3.lottiefiles.com/packages/lf20_i2eyukor.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

home_layout = html.Div([
    dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Img(src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Logo_IUH.png/800px-Logo_IUH.png",style={'height':'150px','width':'300px'})     
        ],className="col-3"),
        dbc.Col([ 
            html.Br(),
            # html.H5("Tổng quan thị trường trái Phiếu Việt Nam",style={'font-weight':'1000', 'text-align':'center','font-size':'35px','margin-top':'10px'}),
        ],className="col-6"),
        dbc.Col([
            html.Div(de.Lottie(options=options, width="35%", height="25%", url=url))
        ],className='col-3')
        
    ],style={'background-image':'url(https://vnn-imgs-f.vgcloud.vn/2019/09/27/17/19.jpg)'}),
   html.Nav(
    [
        html.Ul(
            [
                html.Li([
                    html.A("Giới Thiệu Về trái phiếu", href="#",style={'font-size':'15px'}),
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
                # html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/page-4",style={'font-size':'15px'})),
                html.Li([
                    html.A("Công cụ tính toán", href="#",style={'font-size':'15px'}),
                    html.Ul([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Bắt đầu giới thiệu"),
                                html.Li(dcc.Link("Trái phiếu chính phủ", href="/page-4",style={'font-size':'12px'})),
                                html.Li(dcc.Link("Trái phiếu doanh nghiệp", href="/page-8",style={'font-size':'12px'})),
                               
                            ])
                        ],style={'background-color':'#00325b'}),
                        ],className="submenu")
                ],className="has-submenu"),
                html.Li(dcc.Link("Trung Tâm Truyền Thông", href="/page-5",style={'font-size':'15px'})),
                html.Li(dcc.Link("Báo cáo thị trường trái phiếu", href="/page-6",style={'font-size':'15px'})),
                html.Li(dcc.Link("Tin tức",href="/page-7",style={'font-size':'15px'}))
            ],
            className="navbar-nav mr-auto",
        ),
    ],
    className="navbar navbar-expand-lg",
    ),
    html.Div([
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    html.Img(src="https://media.baodautu.vn/Images/manhbon/2021/03/30/TPDN3003.png",style={'height':'400px','width':'90%'})
                #     html.Div([
                #     html.Img(src="https://media.istockphoto.com/id/1430187728/vi/vec-to/17-th%C3%A1ng-2-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=1eWRY2CuwYdP6ys1ZZjXbZ1QuNGWb16cwHAKT_zEmhI=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
                #     html.A("Báo cáo thị trường trái phiếu năm 2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-nam-2022/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                #     html.I("Tổng giá trị TPDN phát hành trong Q4/22 giảm 94,5% so với quý trước và giảm 98,8% so với cùng kỳ (svck), chỉ đạt 3.619 tỷ đồng. Tính cả năm 2022, tổng giá trị TPDN phát hành ước đạt 269.733…",style={'font-weight':'300'})
                #     ],style={'margin-bottom':'1.25rem'}),
                #     html.Hr(),
                #     html.Div([
                #         html.Img(src="https://media.istockphoto.com/id/1430492156/vi/vec-to/11-th%C3%A1ng-10-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=STOACz-r9UMOTFtXG8sgbrYW3U61wZqwoL-CCY4w0zI=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
                #         html.A("Báo cáo thị trường trái phiếu Quý 3 năm 2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-quy-3-nam-2022v1/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                #         html.I("Tổng giá trị TPDN phát hành trong Quý 3 giảm 50,5% so với quý trước và giảm 70,9% so với cùng kỳ (svck), chỉ đạt 60.635 tỷ đồng. Từ đầu năm đến nay, tổng giá trị TPDN phát hành ước…",style={'font-weight':'300'})
                #     ]),
                #     html.Hr(),
                #     html.Div([
                #         html.Img(src="https://media.istockphoto.com/id/1430474400/vi/vec-to/20-th%C3%A1ng-7-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=NRNBOoJFCyvcaxPCJaAN65N1-kGlen-HB3jTE9M_vnE=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
                #         html.A("Báo cáo thị trường trái phiếu Quý 2 năm 2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-quy-2-nam-20221/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                #         html.I("Giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong Q2/22 đạt 111.814 tỷ đồng, giảm 43,7% so với cùng kỳ. Tổng giá trị TPDN phát hành nửa đầu năm 2022 (6T22) ước đạt 176.867 tỷ đồng, giảm mạnh 23,7%…",style={'font-weight':'300'})
                #     ]),
                #     html.Hr(),
                #     html.Div([
                #         html.Img(src="https://media.istockphoto.com/id/1430451949/vi/vec-to/22-th%C3%A1ng-4-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=WO2SDPFRACE5joUQLjEhBkdsHmmLrmIlSh9Qyjx5R9Y=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
                #         html.A("Báo cáo Thị trường Trái phiếu Việt Nam Quý 1/2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-viet-nam-quy-1-2022/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                #         html.I("Tổng giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong Quý 1/22 đạt 45.374 tỷ đồng, tăng mạnh 48,3% svck và giảm 84,9% so với quý trước. Chúng tôi cho rằng thị trường TPDN sẽ trầm lắng hơn trong…",style={'font-weight':'300'})
                #     ]),
                #     html.Hr(),
                #     html.Div([
                #         html.Img(src="https://media.istockphoto.com/id/1430181379/vi/vec-to/19-th%C3%A1ng-1-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=VeyRbGuJfsW4rCjoWY7AEyl4YRBvPB2tQMw7CjfAeXg=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
                #         html.A("BÁO CÁO THỊ TRƯỜNG TRÁI PHIẾU NĂM 2021",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-nam-2021/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                #         html.I("Tổng giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong Quý 4 đạt 189.652 tỷ đồng, giảm 7,6% so với quý trước (sv quý trước). Giá trị TPDN phát hành cả năm 2021 ước đạt 623.616 tỷ đồng, tăng…",style={'font-weight':'300'})
                #     ]),
                
                ],className="col-6",style={'height':'400px','float':'left'}),
                dbc.Col([   
                    dbc.Row([
                        html.Div([
                            html.Img(src="https://i1-kinhdoanh.vnecdn.net/2023/03/03/0DD05A9E5568D8B9D0E32C4241A114-6838-2230-1677831766.jpg?w=500&h=300&q=100&dpr=1&fit=crop&s=irYXPTKNqmsnBoguOEs6IQ",style={'float':'left','width':'300px','height':'150px','margin': '0px 15px 15px 0px'}),
                            html.A("Nhiều doanh nghiệp địa ốc khuất nợ trái phiếu",href="https://vnexpress.net/nhieu-doanh-nghiep-dia-oc-khat-no-trai-phieu-4577091.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                            html.I("Ít nhất 10 doanh nghiệp bất động sản đã thông báo chậm trả lãi hoặc gốc trái phiếu trong nửa tháng qua với cùng lý do chưa thu xếp kịp nguồn thanh toán",style={'font-weight':'300'})
                        ],style={'margin-bottom':'1.25rem'}),
                        html.Hr(),
                        html.Div([
                            html.Img(src="https://i1-kinhdoanh.vnecdn.net/2023/02/24/z4128522439890e0601edd3bc6e3a5-4777-5361-1677224032.jpg?w=500&h=300&q=100&dpr=1&fit=crop&s=Bu_4-ZkQdmoxAJ9UzGu9Rg",style={'float':'left','width':'300px','height':'150px','margin': '0px 15px 15px 0px'}),
                            html.A("Một công ty địa ốc phát hành trái phiếu lãi suất 13,5%",href="https://vnexpress.net/mot-cong-ty-dia-oc-phat-hanh-trai-phieu-lai-suat-13-5-4574466.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                            html.I("Đều là chứng khoán xác nhận quyền và lợi ích hợp pháp của người sở hữu với tài sản hay phần vốn của doanh nghiệp nhưng trái phiếu doanh nghiệp khác nhiều cổ phiếu. ",style={'font-weight':'300'}),
                            
                        ]),
                        html.Hr(),
                        html.Div([
                            html.Img(src="https://i1-kinhdoanh.vnecdn.net/2023/02/14/vpbankthanhtung10-1676369306-1-4040-9042-1676369333.jpg?w=500&h=300&q=100&dpr=1&fit=crop&s=EkUAdWDpWiMMFuKU6aE0Dw",style={'float':'left','width':'300px','height':'150px','margin': '0px 15px 15px 0px'}),
                            html.A("Áp lực trái phiếu tăng mạnh vào giữa năm", href="https://vnexpress.net/ap-luc-dao-han-trai-phieu-tang-manh-vao-giua-nam-4570610.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                            html.I("VNDirect ước tính giá trị đáo hạn trái phiếu doanh nghiệp năm nay gần 273.000 tỷ đồng, tập trung nhiều vào quý II và III. ",style={'font-weight':'300'})
                        ]),
                        html.Hr(),
                        html.Div([
                            html.Img(src="https://i1-kinhdoanh.vnecdn.net/2023/01/21/23e5183b996d42331b7c-jpeg-1674-9270-9766-1674268897.jpg?w=500&h=300&q=100&dpr=1&fit=crop&s=84Igoybr18q-L9cspZZBQA",style={'float':'left','width':'300px','height':'150px','margin': '0px 15px 15px 0px'}),
                            html.A("Kinh tế trưởng ADB Việt Nam: 'Thị trường trái phiếu không thể tự điều tiết'",href="https://vnexpress.net/kinh-te-truong-adb-viet-nam-thi-truong-trai-phieu-khong-the-tu-dieu-tiet-4562563.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                            html.I("Kinh tế trưởng Nguyễn Minh Cường của Ngân hàng phát triển châu Á (ADB) Việt Nam cho rằng, nhà nước không nên để thị trường vốn tự xử lý mà cần can thiệp nhiều hơn.",style={'font-weight':'300'})
                        ]),
                        html.Hr(),
                        html.Div([
                            html.Img(src="https://i1-kinhdoanh.vnecdn.net/2023/01/21/1400x1-1674276469-3277-1674276879.jpg?w=500&h=300&q=100&dpr=1&fit=crop&s=xEPKQxHq3FahU4BrL0307g",style={'float':'left','width':'300px','height':'150px','margin': '0px 15px 15px 0px'}),
                            html.A("Bất động sản toàn cầu đối diện vòng xoáy nợ 175 tỷ USD",href="https://vnexpress.net/bat-dong-san-toan-cau-doi-dien-vong-xoay-no-175-ty-usd-4562587.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                            html.I("Đà sụt giảm của loại tài sản lớn nhất toàn cầu đã lan rộng từ thị trường nhà đất sang bất động sản thương mại, nguy cơ tạo làn sóng hỗn loạn tín dụng trên toàn thế giới.",style={'font-weight':'300'})
                        ]),
                        html.Hr(),
                        html.Div([
                            html.Img(src="https://i1-kinhdoanh.vnecdn.net/2023/01/22/investsettop-1674379832-7640-1674379837.jpg?w=500&h=300&q=100&dpr=1&fit=crop&s=l-9Oelgldoar48EPGxjM2Q",style={'float':'left','width':'300px','height':'150px','margin': '0px 15px 15px 0px'}),
                            html.A("Làm thế nào để đầu tư tốt hơn trong năm 2023?",href="https://vnexpress.net/lam-the-nao-de-dau-tu-tot-hon-trong-nam-2023-4562828.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                            html.I("Giới chuyên gia cho rằng bạn chỉ nên dành 3% danh mục cho tiền số, lập mục tiêu tài chính ngay từ đầu và đừng dao động theo tin đồn. ",style={'font-weight':'300'})
                        ]),
                        html.Hr(),
                        html.Div([
                            html.Img(src="https://i1-kinhdoanh.vnecdn.net/2023/01/17/a-tb-phan-khu-2-khu-do-thi-du-6186-9361-1673939702.jpg?w=500&h=300&q=100&dpr=1&fit=crop&s=ZuCxlGgaNIGNCu0W5p-Sew",style={'float':'left','width':'300px','height':'150px','margin': '0px 15px 15px 0px'}),
                            html.A("Phát Đạt mua thêm gần 900 tỷ đồng trái phiếu trước hạn",href="https://vnexpress.net/phat-dat-mua-them-gan-900-ty-dong-trai-phieu-truoc-han-4561137.html",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
                            html.I("Hôm nay, Công ty cổ phần Phát triển Bất động sản Phát Đạt (PDR) thông báo tất toán 5 lô trái phiếu trước hạn với tổng giá trị 893,4 tỷ đồng. ",style={'font-weight':'300'})
                        ]),

                    ])
                ],className="col-6",style={'overflow': 'scroll','height':'400px'})
                
            ],className="row_body"),
            html.Br(),
            dbc.Row([
                html.H1("Trái Phiếu",style={'color':'#838689','font-weight': '600','font-size':'35px'}),
                html.Br(),html.Br(),
                html.H2("Trái phiếu được hiểu như thế nào?",style={'color':'#00325b','font-weight': '600','font-size':'30px','text-align':'left'}),
                html.Br(),
                html.P('Trái phiếu là chứng khoán nợ, tương tự như IOU. Người đi vay phát hành trái phiếu để huy động tiền từ các nhà đầu tư sẵn sàng cho họ vay tiền trong một khoảng thời gian nhất định.'),
                html.Br(),
                html.P("Khi bạn mua trái phiếu, bạn đang cho người phát hành vay, có thể là chính phủ, thành phố hoặc công ty. Đổi lại, tổ chức phát hành hứa sẽ trả cho bạn một mức lãi suất cụ thể trong suốt thời hạn của trái phiếu và hoàn trả tiền gốc, còn được gọi là mệnh giá hoặc mệnh giá của trái phiếu, khi trái phiếu đáo hạn hoặc đến hạn sau một khoảng thời gian nhất định."),
                html.H2("Tại sao các nhà đầu tư lại mua trái phiếu",style={'color':'#00325b','font-weight': '600','font-size':'30px','text-align':'left'}),html.Br(),
                html.Img(src="https://cdn.hdbank.com.vn/hdbank-file/news/editor/K4TYh9jqRHQmSOqMOTJL20221212162344/traiphieudoanhnghieplagi1_1670837129403.jpeg"),
                html.P("Nhà đầu tư mua trái phiếu vì:"),
                html.I(" - Họ cung cấp một dòng thu nhập có thể dự đoán được. Thông thường, trái phiếu trả lãi hai lần một năm"),
                html.I(" - Nếu trái phiếu được giữ đến ngày đáo hạn, trái chủ sẽ nhận lại toàn bộ tiền gốc, vì vậy trái phiếu là một cách để bảo toàn vốn khi đầu tư."),
                html.I(" - Trái phiếu có thể giúp bù đắp rủi ro đối với việc nắm giữ cổ phiếu biến động hơn."),
                html.Br(),
                html.P("Công ty, chính phủ và thành phố phát hành trái phiếu để lấy tiền cho nhiều thứ khác nhau, có thể bao gồm:"),
                html.Br(),
                html.I(" - Cung cấp dòng tiền hoạt động"),
                html.I("- Nợ tài chính"),
                html.I("- Tài trợ vốn đầu tư vào trường học, đường cao tốc, bệnh viện và các dự án khác"),
                html.Br(),
                html.H2("Phân loại các loại trái phiếu thường hay gặp?",style={'color':'#00325b','font-weight': '600','font-size':'30px','text-align':'left'}),
                html.P("Theo chủ thể phát hành:"),
                html.P(children=[html.B("Trái phiếu doanh nghiệp",style={'color':'#218383'}), " là một loại chứng khoán mà các doanh nghiệp; các công ty phát hành ra để huy động nguồn vốn cho doanh nghiệp. Trái phiếu doanh nghiệp trên thị trường có rất nhiều loại và đa dạng,Phát hành trái phiếu doanh nghiệp phải theo nguyên tắc tự túc vay, trả, tự chịu các trách nhiệm hiệu quả sử dụng nguồn vốn. Đảm bảo khả năng thanh toán khoản vay nợ."]),
                html.P(children=[html.B("Trái phiếu ngân hàng "),"là các các loại trái phiếu do chủ thể là ngân hàng phát hành để huy động vốn đầu tư trong ngắn hạn với một mức lãi suất được ấn định trước đó.Tuy nhiên các loại trái phiếu ngân hàng sẽ đem lại cơ hội đầu tư an toàn như gửi tiết kiệm ngân hàng nhưng có lãi suất cao hơn."]),
                html.P(children=[html.B("Trái phiếu chính phủ ",style={'color':'#218383'}),"à một loại trái phiếu do chính phủ phát hành, chính phủ dùng loại trái phiếu này để huy động thêm nguồn vốn để thực hiện các hoạt động đầu tư công, các chương trình của chính phủ.Điểu kiện để có thể mua trái phiếu chính phủ không hề đơn giản. Các nhà đầu tư phải trải qua giai đoạn đấu thầu để xác định tư cách, cũng như điều kiện để mua trái phiếu chính phủ. Lãi suất trái phiếu chính phủ thường sẽ được thông báo công khai trên trang web của Sở giao dịch chứng khoán."]),
                html.Br(),
                html.Br(),
                html.B("Kết Luận"),html.Br(),
                html.I("Trên đây là những tin liên quan đến trái phiếu là gì. Cũng giống với mua cổ phiếu, có rất nhiều cách mua trái phiếu. Nhà đầu tư có thể tham khảo bài viết trên để xác định các kênh đầu tư phù hợp đúng đắn. Hy vọng bài viết sẽ có ích cho các nhà đầu tư.")

            ],className="row_body",style={'margin':'0px 400px 0px 400px'}),
            html.Br(),
            dbc.Row([
                html.H3("Tin chính"),
                dbc.Col([
                    dbc.Card([
                        html.Img(src="https://image.vietstock.vn/2023/03/02/vdsc-1-2386-ava_924685.png",style={'height':'400px'}),
                        html.A("Chứng khoán Rồng Việt muốn chào bán 410 tỷ đồng trái phiếu riêng lẻ",href="https://vietstock.vn/2023/03/chung-khoan-rong-viet-muon-chao-ban-410-ty-dong-trai-phieu-rieng-le-3118-1044013.htm",style={'color':'red','font-weight':'600','font-size':'18px'}),
                        html.I("HĐQT CTCP Chứng khoán Rồng Việt (HOSE: VDS) vừa thông qua phương án phát hành 410 tỷ đồng trái phiếu riêng lẻ (lần 1 năm 2023) và …",style={'font-weight':'300'})
                    ])
                ],className="col-4"),
                dbc.Col([
                    dbc.Card([
                        html.Img(src="https://image.vietstock.vn/2023/02/25/duc-ca-tam-0.PNG"),
                        html.A("Những lô trái phiếu của đại gia cá tầm Việt Nam",href="https://vietstock.vn/2023/02/nhung-lo-trai-phieu-cua-dai-gia-ca-tam-viet-nam-3118-1042436.htm",style={'color':'red','font-weight':'600','font-size':'18px'}),
                        html.I("Sở hữu những trang trại nuôi cá tầm hàng đầu Việt Nam, ông Lê Anh Đức còn lấn sân vào mảng bất động sản và năng lượng. Để có nguồn vốn …",style={'font-weight':'300'})
                    ])
                ],className="col-4"),
                dbc.Col([
                    dbc.Card([
                        html.Img(src="https://image.vietstock.vn/2023/02/23/tpdn-shaking-up-corporate-bond-issuance_1613766.jpg"),
                        html.A("HNX công bố danh sách 54 doanh nghiệp từng chậm thanh toán lãi trái phiếu",href="https://vietstock.vn/2023/02/hnx-cong-bo-danh-sach-54-doanh-nghiep-tung-cham-thanh-toan-lai-trai-phieu-785-1041849.htm",style={'color':'red','font-weight':'600','font-size':'18px'}),
                        html.I("Ngày 21/02/2023, Sở Giao dịch Chứng khoán Hà Nội (HNX) thông báo danh sách các tổ chức phát hành công bố thông tin bất thường hoặc báo …",style={'font-weight':'300'})
                    ])
                ],className="col-4")
            ],style={'margin':'0px 40px 0px 40px'}),

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
                
            
        ])



    ],fluid=True)
],style={'background-color':'#F4F6F6'})

