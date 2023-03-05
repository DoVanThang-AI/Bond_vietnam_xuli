import dash
import dash_bootstrap_components as dbc
from dash import html
import dash
import dash_core_components as dcc
import dash_extensions as de
import dash_html_components as html
from dash.dependencies import Output, Input,State
import dash_bootstrap_components as dbc
import dash_extensions as de
from dash.dependencies import Input, Output

url = 'https://assets3.lottiefiles.com/packages/lf20_i2eyukor.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
app = dash.Dash(__name__,
                external_stylesheets=[dbc.icons.FONT_AWESOME,dbc.themes.BOOTSTRAP],
       )
url_bell = 'https://assets8.lottiefiles.com/packages/lf20_daV8h3.json'
# this is HOME FUNTIONS 
'''
Nội dung trang đầu tiên sẽ chứa ở đây tại `home_layout` 
'''

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
                html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/page-4",style={'font-size':'15px'})),
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

'''
Nội dung trang 1 với link : 
FIve question to Ask before you invest
'''
page_1_layout = html.Div([
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
                                html.Li(dcc.Link("1.Thị Trường trái phiếu là gì?", href="/",style={'font-size':'12px'})),
                                html.Li(dcc.Link("2.Phân bổ tài sản", href="/page-2",style={'font-size':'12px'})),
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
    #thij truong trai phieu la gi?


    dbc.Row([
       # page 1
       html.H3("Thị trường trái phiếu là gì?",style={'text-align':'left','color':'#797D7F'}),html.Br(),
       html.P(children=[html.B("Thị trường trái phiếu")," là nơi diễn ra các hoạt động trao đổi mua bán trái phiếu giữa các nhà đầu tư, tổ chức phát hành hoặc trung gian môi giới. "]),
       html.P("Đây là nơi các tổ chức phát hành công cụ nợ – trái phiếu – để thực hiện việc huy động vốn cho hoạt động của mình. Người nắm giữ trái phiếu được gọi là trái chủ, bên phát hành có trách nhiệm trả lãi cho trái chủ cùng với toàn bộ số vốn vào thời điểm đáo hạn."),
       html.P("Thị trường trái phiếu được chia thành rất nhiều loại phù hợp với từng đặc điểm và chức năng của nó. Tùy theo nhu cầu của nhà đầu tư mà có thể chọn và sở hữu loại trái phiếu phù hợp với mục tiêu đầu tư."),html.Br(),
       html.Img(src="https://cdn1.finhay.com.vn/wp-content/uploads/2021/06/03104724/tim-hieu-ve-thi-truong-trai-phieu.jpg",style={'width':'100%','height':'400px'}),html.Br(),
       html.H3("Đặc điểm của sản phẩm trong thị trường trái phiếu?",style={'text-align':'left','color':'#797D7F'}),html.Br(),
       html.P(children=[html.B("Đặc điểm của trái phiếu",style={'color':'blue'})]),
       html.P(children=[html.B("1.Trái phiếu có kỳ hạn: "),"Mỗi trái phiếu phát hành đều quy định kỳ hạn cụ thể. Trái phiếu có thể là ngắn hạn (1-5 năm), trung hạn (5-12 năm) và dài hạn (12-30 năm). Việc thanh toán lãi sẽ khác nhau tùy loại trái phiếu có thể chia thành 3 tháng, 6 tháng hoặc 12 tháng. Tại thời điểm đáo hạn, công ty phát hành sẽ hoàn trả toàn bộ số tiền mà nhà đầu tư đã bỏ ra để sở hữu trái phiếu, kèm theo đó là khoản tiền lãi tính theo lãi suất xác định."]),html.Br(),
       html.P("Trái phiếu có mệnh giá niêm yết là 100.000 VNĐ và bội số của 100.000 VNĐ nếu phát hành tại thị trường Việt Nam. Giá trái phiếu tỷ lệ nghịch với lãi sự thay đổi lãi suất trên thị trường. Trái chủ nhận được lợi tức cố định đối với các trái phiếu đã quy định trước mức lãi suất áp dụng trên trái phiếu. "),html.Br(),
       html.P("Trái chủ được ưu tiên thanh toán tài sản thanh lý nếu tổ chức phát hành bị phá sản. Tuy nhiên trái chủ không có quyền biểu quyết, tác động đến quyết định của công ty."),html.Br(),
       html.H3("Phân loại trái phiếu:",style={'text-align':'left','color':'#797D7F'}),html.Br(),
       html.P(children=[html.B("1.Dựa theo người phát hành: "),"Có trái phiếu chính phủ, trái phiếu doanh nghiệp, trái phiếu ngân hàng và các tổ chức tài chính."]),html.Br(),
       html.P(children=[html.B("2.Dựa theo hình thức trái phiếu: "),"Trái phiếu vô danh, trái phiếu ghi danh."]),html.Br(),
       html.P(children=[html.B("3.Dựa theo tính chất trái phiếu:"),"Trái phiếu có thể chuyển đổi, trái phiếu có thể mua lại và trái phiếu được phép chuyển đổi thành cổ phiếu."]),html.Br(),
       html.P(children=[html.B("Dựa theo lợi tức:"),"Trái phiếu có lãi suất cố định, trái phiếu có lãi suất bằng không và trái phiếu có lãi suất thả nổi."]),html.Br(),
       html.P(children=[html.B("Dựa theo độ đảm bảo thanh toán: "),"Trái phiếu đảm bảo và trái phiếu không có đảm bảo."]),html.Br(),
       html.H3("Các loại thị trường trái phiếu hiện nay",style={'text-align':'left','color':'#797D7F'}),html.Br(),
       html.P(children=[html.B("1. Thị trường trái phiếu chính phủ"),"chính là thị trường then chốt trên thị trường trái phiếu. Nó là nơi huy động nguồn vốn để bù đắp những thâm hụt trong ngân sách nhà nước. Đây cũng được xem là thị trường chuẩn cho thị trường tài chính."]),html.Br(),
       html.Img(src="https://cdn1.finhay.com.vn/wp-content/uploads/2021/06/03092541/nhung-uu-diem-trai-phieu.jpg",style={'width':'100%','height':'400px'}),html.Br(),
       html.P("rái phiếu chính phủ được phát hành theo phương thức đấu thầu, bảo lãnh hoặc bán lẻ. Hiện nay các chứng khoán sẽ được đăng ký, lưu ký và niêm yết trên sở giao dịch chứng khoán Hà Nội và phát hành theo hình thức đấu thầu là chủ yếu. Đối với những người tham gia và mua trái phiếu chính phủ trong thị trường này, Bộ tài chính hằng năm sẽ tiến hành kiểm tra về tình hình tài chính của doanh nghiệp, các hoạt động tham gia vào thị trường sơ cấp và thị trường thứ cấp."),html.Br(),
       html.P(children=[html.B("2.Thị trường trái phiếu chính phủ bảo lãnh"),"Thị trường trái phiếu chính phủ bảo lãnh là thị trường dành riêng cho các đối tượng thuộc diện được bảo lãnh theo quy định của chính phủ. Các đối tượng đó có thể là doanh nghiệp, ngân hàng chính sách và các tổ chức tài chính, tổ chức tín dụng,… Theo đó, việc phát hành trái phiếu sẽ huy động vốn để thực hiện các chương trình tín dụng theo mục tiêu của nhà nước.."]),html.Br(),
       html.P("Trái phiếu chính phủ bảo lãnh được phát hành theo phương thức đấu thầu, bảo lãnh, đại lý hoặc bán lẻ. "),
       html.H3("3.Thị trường trái phiếu chính quyền địa phương",style={'text-align':'left','color':'#797D7F'}),html.Br(),
       html.P("Đây là thị trường sẽ phát hành trái phiếu để huy động vốn tại địa phương dùng cho các phương án đầu tư, chương trình, dự án thuộc nhiệm vụ chi của ngân sách địa phương."),html.Br(),
       html.P("Trái phiếu chính quyền địa phương trước khi phát hành sẽ được đăng ký và niêm yết tại sở giao dịch. Sau đó mới tiến hành công bố ra thị trường theo hình thức đấu thầu, đại lý phát hành hoặc bảo lãnh."),html.Br(),
       html.Img(src="https://cdn1.finhay.com.vn/wp-content/uploads/2021/06/03104722/thi-truong-trai-phieu-chinh-phu-dia-phuong.jpg",style={'width':'100%','height':'400px'}),html.Br(),
       html.H3("4.Thị trường trái phiếu doanh nghiệp",style={'text-align':'left','color':'#797D7F'}),html.Br(),
       html.P("Thị trường trái phiếu doanh nghiệp là nơi huy động vốn cho doanh nghiệp dùng trong mục đích kinh doanh, mở rộng quy mô và phát triển đầu tư. Theo đó, thị trường này có thể được chia thành thị trường sơ cấp và thị trường thứ cấp."),html.Br(),
       html.P("Thị trường sơ cấp: Giao dịch với các chứng khoán mới phát hành, tạo vốn quan trọng cho tổ chức phát hành. Là nơi tập hợp các nguồn vốn trong thị trường và nâng cao hiệu quả hoạt động của nền kinh tế."),html.Br(),
       html.P("Thị trường thứ cấp: Nơi xảy ra các giao dịch trao đổi mua bán những chứng khoán đã được phát hành trên thị trường sơ cấp. Không tạo vốn cho tổ chức phát hành và thực hiện các giao dịch giữa các nhà đầu tư với nhau. Bạn có thể chuyển nhượng quyền sở hữu trái phiếu cho người khác tại thị trường này."),html.Br(),

       







           
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


#TRANG 2 
# Phân bổ tài sản
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


''' Page 4 have '''
page_4_layout = html.Div([
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
                html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/",style={'font-size':'15px'})),
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
        html.H1("Page main have statictis VN bonds")
    ])
],style={'background-color':'#F4F6F6'})


'''Page 5 here'''
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

'''page6 here'''
#Báo cáo thị trufong trái phiếu
page_6_layout = html.Div([
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
                                html.Li(dcc.Link("2.Phân bổ tài sản", href="/page-2",style={'font-size':'12px'})),
                                html.Li(dcc.Link("3.Tổng quan định giá trái phiếu", href="/page-3",style={'font-size':'12px'})),
                            ])
                        ],style={'background-color':'#00325b'}),
                        ],className="submenu")
                ],className="has-submenu"),
                html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/page-4",style={'font-size':'15px'})),
                html.Li(dcc.Link("Trung Tâm Truyền Thông", href="/page-5",style={'font-size':'15px'})),
                html.Li(dcc.Link("Báo cáo thị trường trái phiếu     ", href="/",style={'font-size':'15px'})),
                html.Li(dcc.Link("Tin tức",href="/page-7",style={'font-size':'15px'}))
            ],
            className="navbar-nav mr-auto",
        ),
    ],
    className="navbar navbar-expand-lg",
    ),
   html.Br(),
    #báo cáo thị trường trái phiếu tịa đây

    dbc.Row([
        html.H1("Báo cáo thị trường trái phiếu Việt Nam",style={'color':'#797D7F'}),html.Br(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430187728/vi/vec-to/17-th%C3%A1ng-2-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=1eWRY2CuwYdP6ys1ZZjXbZ1QuNGWb16cwHAKT_zEmhI=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Báo cáo thị trường trái phiếu năm 2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-nam-2022/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Tổng giá trị TPDN phát hành trong Q4/22 giảm 94,5% so với quý trước và giảm 98,8% so với cùng kỳ (svck), chỉ đạt 3.619 tỷ đồng. Tính cả năm 2022, tổng giá trị TPDN phát hành ước đạt 269.733…",style={'font-weight':'300'})
        ],style={'margin-bottom':'1.25rem'}),
        html.Hr(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430492156/vi/vec-to/11-th%C3%A1ng-10-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=STOACz-r9UMOTFtXG8sgbrYW3U61wZqwoL-CCY4w0zI=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Báo cáo thị trường trái phiếu Quý 3 năm 2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-quy-3-nam-2022v1/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Tổng giá trị TPDN phát hành trong Quý 3 giảm 50,5% so với quý trước và giảm 70,9% so với cùng kỳ (svck), chỉ đạt 60.635 tỷ đồng. Từ đầu năm đến nay, tổng giá trị TPDN phát hành ước…",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430474400/vi/vec-to/20-th%C3%A1ng-7-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=NRNBOoJFCyvcaxPCJaAN65N1-kGlen-HB3jTE9M_vnE=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Báo cáo thị trường trái phiếu Quý 2 năm 2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-quy-2-nam-20221/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong Q2/22 đạt 111.814 tỷ đồng, giảm 43,7% so với cùng kỳ. Tổng giá trị TPDN phát hành nửa đầu năm 2022 (6T22) ước đạt 176.867 tỷ đồng, giảm mạnh 23,7%…",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430451949/vi/vec-to/22-th%C3%A1ng-4-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=WO2SDPFRACE5joUQLjEhBkdsHmmLrmIlSh9Qyjx5R9Y=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Báo cáo Thị trường Trái phiếu Việt Nam Quý 1/2022",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-viet-nam-quy-1-2022/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Tổng giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong Quý 1/22 đạt 45.374 tỷ đồng, tăng mạnh 48,3% svck và giảm 84,9% so với quý trước. Chúng tôi cho rằng thị trường TPDN sẽ trầm lắng hơn trong…",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430181379/vi/vec-to/19-th%C3%A1ng-1-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=VeyRbGuJfsW4rCjoWY7AEyl4YRBvPB2tQMw7CjfAeXg=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("BÁO CÁO THỊ TRƯỜNG TRÁI PHIẾU NĂM 2021",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-nam-2021/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Tổng giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong Quý 4 đạt 189.652 tỷ đồng, giảm 7,6% so với quý trước (sv quý trước). Giá trị TPDN phát hành cả năm 2021 ước đạt 623.616 tỷ đồng, tăng…",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430492324/vi/vec-to/14-th%C3%A1ng-10-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=ZRYp8z7F8cG9lNWnhzNa--Ym_t05EgjtnuM5qRWO7yo=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Báo cáo Thị trường Trái phiếu Việt Nam quý 4 – 2021",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-quy-4-2021/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Tổng giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong Quý 3 đạt 111.744 tỷ đồng, giảm 2,2% so với cùng kỳ (svck) và giảm 25,0% so với quý trước. Giá trị TPDN phát hành lũy kế từ đầu…",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430474400/vi/vec-to/20-th%C3%A1ng-7-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=NRNBOoJFCyvcaxPCJaAN65N1-kGlen-HB3jTE9M_vnE=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Báo cáo Thị trường Trái phiếu quý 3 – 2021",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-quy-3-2021/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Tổng giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong quý 2/2021 đạt mức 134.703 tỷ đồng (+8,1% so với cùng kỳ) và tăng 3,4 lần so với quý trước. Giá trị TPDN phát hành lũy kế từ đầu…",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://media.istockphoto.com/id/1430193693/vi/vec-to/21-th%C3%A1ng-3-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-l%E1%BB%8Bch-h%C3%A0ng-ng%C3%A0y-n%E1%BB%81n-tr%E1%BA%AFng.jpg?s=612x612&w=0&k=20&c=pz1bbz1_kHmRkqD2YyeL55UpWbZQ4COKnr-_0vkwhfM=",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Báo cáo Thị trường Trái phiếu tháng 5 – 2021",href="https://www.vndirect.com.vn/bao-cao-thi-truong-trai-phieu-thang-5-2021/",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Tổng giá trị Trái phiếu doanh nghiệp (TPDN) phát hành trong tháng 4/2021 đạt mức 42.109 tỷ đồng (+71,4% svck), tăng 101,9% so với tháng trước. Giá trị TPDN phát hành lũy kế từ đầu năm đạt 81.681 tỷ đồng,…",style={'font-weight':'300'})
        ])
    ],style={'margin':'0px 400px 0px 400px'})

    ],fluid=True)
],style={'background-color':'#F4F6F6'})

''' Page 7 in here tin tuc'''

page_7_layout = html.Div([
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
                html.Li(dcc.Link("Trung Tâm Truyền Thông", href="/page-5",style={'font-size':'15px'})),
                html.Li(dcc.Link("Báo cáo thị trường trái phiếu", href="/page-6",style={'font-size':'15px'})),
                html.Li(dcc.Link("Tin tức",href="/",style={'font-size':'15px'}))
            ],
            className="navbar-nav mr-auto",
        ),
    ],
    className="navbar navbar-expand-lg",
    ),
    html.Br(),
    dbc.Row([
        html.H1("Tin tức thị trường trái phiếu Việt Nam",style={'color':'#797D7F'}),html.Br(),
        html.Div([
            html.Img(src="https://image.vietstock.vn/2023/03/03/Dat-xanh-ava_1811158.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Đất Xanh Miền Nam xin chậm trả lãi trái phiếu hơn 3 tỷ đồng",href="https://vietstock.vn/2023/03/dat-xanh-mien-nam-xin-cham-tra-lai-trai-phieu-hon-3-ty-dong-3118-1044817.htm",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Theo thông báo gửi đến Sở Giao dịch Chứng khoán Hà Nội (HNX), CTCP Đầu tư và Dịch vụ Đất Xanh Miền Nam (ĐXMN) đã không thể trả kịp số tiền hơn 3 tỷ...",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://image.vietstock.vn/2023/03/03/PSH-ava_150296.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Đại gia xăng dầu miền Tây tiếp tục mua lại trước hạn 110 tỷ đồng trái phiếu",href="https://vietstock.vn/2023/03/dai-gia-xang-dau-mien-tay-tiep-tuc-mua-lai-truoc-han-110-ty-dong-trai-phieu-3118-1044591.htm",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("CTCP Thương mại Đầu tư Dầu khí Nam Sông Hậu (HOSE: PSH) thông báo mua lại nốt số lượng còn lưu hành của lô trái phiếu mã PSHH2224001. Tổng giá trị...",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://image.vietstock.vn/2023/03/02/vdsc-1-2386-ava_924685.png",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Chứng khoán Rồng Việt muốn chào bán 410 tỷ đồng trái phiếu riêng lẻ",href="https://vietstock.vn/2023/03/chung-khoan-rong-viet-muon-chao-ban-410-ty-dong-trai-phieu-rieng-le-3118-1044013.htm",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("HĐQT CTCP Chứng khoán Rồng Việt (HOSE: VDS) vừa thông qua phương án phát hành 410 tỷ đồng trái phiếu riêng lẻ (lần 1 năm 2023) và phương án mua lại...",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://image.vietstock.vn/2023/02/25/duc-ca-tam-0.PNG",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Những lô trái phiếu của đại gia cá tầm Việt Nam",href="https://vietstock.vn/2023/02/nhung-lo-trai-phieu-cua-dai-gia-ca-tam-viet-nam-3118-1042436.htm",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Sở hữu những trang trại nuôi cá tầm hàng đầu Việt Nam, ông Lê Anh Đức còn lấn sân vào mảng bất động sản và năng lượng. Để có nguồn vốn cho các mảng...",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://image.vietstock.vn/2023/02/27/khat-no-trai-phieu_1040860.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("Doanh nghiệp khất nợ trái phiếu: Rồi sao nữa?",href="https://vietstock.vn/2023/02/doanh-nghiep-khat-no-trai-phieu-roi-sao-nua-3118-1042601.htm",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Sở Giao dịch Chứng khoán Hà Nội (HNX) vừa công bố danh sách các tổ chức phát hành chậm thanh toán gốc, lãi trái phiếu trong khoảng thời gian từ ngày...",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://image.vietstock.vn/2023/02/25/TDG-global_102793.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("TDG sẽ chào bán riêng lẻ 50 tỷ đồng trái phiếu",href="https://vietstock.vn/2023/02/tdg-se-chao-ban-rieng-le-50-ty-dong-trai-phieu-3118-1042425.htm",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("HĐQT CTCP Đầu tư TDG GLOBAL (HOSE: TDG) công bố nghị quyết thông qua việc chào bán trái phiếu riêng lẻ năm 2023. Tổng giá trị huy động là 50 tỷ đồng.",style={'font-weight':'300'})
        ]),
        html.Hr(),
        html.Div([
            html.Img(src="https://image.vietstock.vn/2023/02/23/tpdn-shaking-up-corporate-bond-issuance_1613766.jpg",style={'float':'left','margin': '0px 15px 15px 0px','height':'150px','width':'150px'}),html.Br(),
            html.A("HNX công bố danh sách 54 doanh nghiệp từng chậm thanh toán lãi trái phiếu",href="https://vietstock.vn/2023/02/hnx-cong-bo-danh-sach-54-doanh-nghiep-tung-cham-thanh-toan-lai-trai-phieu-785-1041849.htm",target="_blank",style={'color':'red','font-weight':'600','font-size':'18px'}),html.Br(),
            html.I("Ngày 21/02/2023, Sở Giao dịch Chứng khoán Hà Nội (HNX) thông báo danh sách các tổ chức phát hành công bố thông tin bất thường hoặc báo cáo theo yêu...",style={'font-weight':'300'})
        ]),

    ],style={'margin':'0px 400px 0px 400px'})
],style={'background-color':'#F4F6F6'})
app.layout = html.Div([
    dcc.Location(id = 'url', refresh=False),
    html.Div(id='page-content')
])

#Define the callback to update the page content based on the URL
@app.callback(Output('page-content','children'),
              [Input('url','pathname')])

def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-4':
        return page_4_layout
    elif pathname == '/page-5':
        return page_5_layout
    elif pathname == '/page-6':
        return page_6_layout
    elif pathname == '/page-7':
        return page_7_layout
    else:
        return '404 - Page not found'
    
if __name__ == '__main__':
    app.run_server(debug=True)