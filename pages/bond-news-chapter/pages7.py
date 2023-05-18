from imports import *

dash.register_page(__name__, path='/bond-news/tin-tuc-trai-phieu-viet-nam', name='Tin tức trái phiếu Việt Nam')
''' Page 7 in here tin tuc'''

layout = html.Div([
    
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