from imports import *


dash.register_page(__name__, path='/gioi-thieu-ve-trai-phieu/dinh-gia-trai-phieu', name='Định giá trái phiếu')


''' PAGE 3 have '''
layout = dbc.Row([
        # comment taij day
        html.H1("Tìm hiểu tổng quan về định giá trái phiếu?", style={'font-size':'3rem', 'font-weight':'800'}),
        html.P("Định giá trái phiếu là việc xác định giá trị thực của một trái phiếu. Giá trị này bằng với giá trị hiện tại (hiện giá) của tất cả các dòng tiền nhận được trong tương lai được chiết khấu theo một lãi suất hợp lý."),
        html.P("Lãi suất chiết khấu khi định giá trái phiếu là lãi suất thị trường của một trái phiếu cụ thể. Đây cũng là lãi suất yêu cầu của nhà đầu tư. Lãi suất này thường được tính dựa trên lãi suất của trái phiếu chính phủ có cùng kỳ hạn và thời điểm đáo hạn, cộng thêm phần bù rủi ro."),

        html.H1("Quy trình định giá trái phiếu đến quyết định giao dịch", style={'font-size':'3rem', 'font-weight':'800'}),
        html.P("Ước lượng dòng tiền sinh ra từ tài sản (thu nhập kỳ vọng)."),
        html.P("Ước lượng tỷ suất lợi nhuận NĐT yêu cầu (=lãi suất phi rủi ro +phần gia tăng do rủi ro)."),
        html.P("Lựa chọn mô hình định giá thích hợp để áp dụng. Tính hiện giá dòng tiền tệ thu nhập theo tỷ suất lợi nhuận vừa ước lượng."),
        html.P("So sánh giá trị lý thuyết vừa định ra so với giá trị thị trường."),
        html.P("Quyết định đầu tư (mua hay bán)."),

        html.P("Zero – coupon là loại trái phiếu không được trả lợi tức định kỳ. Và người tham gia sẽ được mua nó với giá thấp hơn nhiều so với mệnh giá. Với loại trái phiếu này, lãi suất trái phiếu sẽ bằng 0 nên tất cả các khoản lợi tức I cũng sẽ bằng 0."),
    
], style={'margin-left': '100px','margin-right': '100px','margin-top': '50px','margin-bottom': '50px', 'height':'100vh'}),
