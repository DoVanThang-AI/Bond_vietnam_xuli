from imports import *


dash.register_page(__name__, path='/gioi-thieu-ve-trai-phieu/dinh-gia-trai-phieu', name='Định giá trái phiếu')


''' PAGE 3 have '''
layout = html.Div([
    
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
    
    ]),
    
],)