from imports import *


dash.register_page(__name__, path='/gioi-thieu-ve-trai-phieu', name='Giới thiệu về trái phiếu')

# url = 'https://assets3.lottiefiles.com/packages/lf20_i2eyukor.json'
# options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
layout = html.Div([
    dbc.Container([
 
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