from imports import *


dash.register_page(__name__, path='/gioi-thieu-ve-trai-phieu/phan-bo-tai-san', name='Phân bổ tài sản')


layout = dbc.Row([
            dbc.Row([
                html.H1("Phân bổ tài sản",style={'font-size':'3rem', 'font-weight':'800'}),
                html.Br(),
                html.P("Phân tài sản liên quan đến việc phân chia các khoản đầu tư của bạn cho các tài sản khác nhau, chẳng hạn như cổ phiếu, trái phiếu và tiền mặt. Quyết định về Phân bổ tài sản là quyết định cá nhân. Khoản phân bổ phù hợp nhất với bạn sẽ thay đổi vào những thời điểm khác nhau trong cuộc đời bạn, tùy thuộc vào thời gian bạn phải đầu tư và khả năng chấp nhận rủi ro của bạn"),
                html.P("Các yếu tố cần xem xét bao gồm:"),html.Br(),
                
                html.P(children=[html.B("Thời gian:")," Khoảng thời gian của bạn là số tháng, số năm hoặc số thập kỷ bạn cần đầu tư để đạt được mục tiêu tài chính của mình. Các nhà đầu tư có thời hạn dài hơn có thể cảm thấy thoải mái khi thực hiện các khoản đầu tư rủi ro hơn hoặc biến động hơn. Những người có khoảng thời gian ngắn hơn có thể thích chấp nhận ít rủi ro hơn."]),
                html.P(children=[html.B("Chấp nhận rủi ro:")," Chấp nhận rủi ro là khả năng và sự sẵn sàng của bạn để mất một phần hoặc toàn bộ khoản đầu tư ban đầu của mình để đổi lấy lợi nhuận tiềm năng lớn hơn."])
            ],style={'text-align':'left'}),
            dbc.Row([
                html.H2("Đa dạng hóa là gì?",style={'text-align':'left','font-size':'2rem', 'font-weight':'800', 'color': 'black'}), 
                html.P("Việc thực hành rải tiền giữa các khoản đầu tư khác nhau để giảm thiểu rủi ro được gọi là đa dạng hóa. Đa dạng hóa là một chiến lược có thể được tóm tắt gọn gàng là “Đừng bỏ tất cả trứng vào một giỏ."),html.Br(),
                html.P("Một cách để đa dạng hóa là phân bổ các khoản đầu tư của bạn vào các loại tài sản khác nhau. Trong lịch sử, cổ phiếu, trái phiếu và tiền mặt không tăng và giảm cùng một lúc. Các yếu tố có thể khiến một loại tài sản hoạt động kém có thể cải thiện lợi nhuận cho một loại tài sản khác. Mọi người đầu tư vào các loại tài sản khác nhau với hy vọng rằng nếu một người thua lỗ, những người khác sẽ bù đắp cho những khoản lỗ đó."),html.Br(),
                html.P("Bạn cũng sẽ đa dạng hóa tốt hơn nếu bạn dàn trải các khoản đầu tư của mình trong từng loại tài sản. Điều đó có nghĩa là nắm giữ một số cổ phiếu hoặc trái phiếu khác nhau và đầu tư vào các lĩnh vực công nghiệp khác nhau, chẳng hạn như hàng tiêu dùng, chăm sóc sức khỏe và công nghệ. Bằng cách đó, nếu một lĩnh vực hoạt động kém, bạn có thể bù đắp nó bằng các khoản nắm giữ khác trong các lĩnh vực đang hoạt động tốt."), html.Br(),
                html.P("Một số nhà đầu tư thấy việc đa dạng hóa dễ dàng hơn bằng cách sở hữu các quỹ tương hỗ. Quỹ tương hỗ là một công ty tập hợp tiền từ nhiều nhà đầu tư và đầu tư tiền vào cổ phiếu, trái phiếu và các sản phẩm tài chính khác. Các quỹ tương hỗ giúp các nhà đầu tư dễ dàng sở hữu một phần nhỏ trong nhiều khoản đầu tư. Ví dụ, một quỹ chỉ số thị trường chứng khoán tổng sở hữu cổ phiếu của hàng nghìn công ty, mang lại nhiều sự đa dạng hóa cho một khoản đầu tư."),html.Br(),
                html.P("Một quỹ tương hỗ không nhất thiết phải đa dạng hóa, đặc biệt nếu nó chỉ tập trung vào một lĩnh vực công nghiệp. Nếu bạn đầu tư vào các quỹ tương hỗ tập trung hẹp, bạn có thể cần đầu tư vào một số quỹ để đa dạng hóa. Khi bạn thêm nhiều khoản đầu tư vào danh mục đầu tư của mình, bạn có thể sẽ phải trả thêm phí và chi phí, điều này sẽ làm giảm lợi tức đầu tư của bạn. Vì vậy, bạn sẽ cần xem xét các chi phí này khi quyết định cách tốt nhất để đa dạng hóa danh mục đầu tư của mình.")

            ], className="mt-4"),
            dbc.Row([
                html.H2("Tái cân bằng là gì?",style={'text-align':'left', 'font-size':'2rem', 'font-weight':'800', 'color': 'black'}),html.Br(),
                html.P("Tái cân bằng là những gì các nhà đầu tư làm để đưa danh mục đầu tư của họ trở lại hỗn hợp phân bổ tài sản ban đầu. Tái cân bằng là cần thiết vì theo thời gian, một số khoản đầu tư sẽ tăng trưởng nhanh hơn những khoản đầu tư khác. Điều này có thể đẩy các khoản nắm giữ của bạn không phù hợp với mục tiêu đầu tư của bạn. Bằng cách tái cân bằng, bạn sẽ đảm bảo rằng danh mục đầu tư của mình không vượt quá một danh mục tài sản cụ thể và bạn sẽ đưa danh mục đầu tư của mình trở lại mức rủi ro dễ chịu."),html.Br(),
                html.P("Ví dụ: bạn có thể bắt đầu với 60% danh mục đầu tư của mình đầu tư vào cổ phiếu, nhưng sau đó sẽ tăng lên 80% do thị trường tăng giá. Để thiết lập lại tổ hợp sản phẩm Phân bổ tài nguyên ban đầu, bạn sẽ cần bán một số cổ phiếu của mình hoặc đầu tư vào các loại tài sản khác."),html.Br(),
                html.P(children=[html.B("Có ba cách bạn có thể cân bằng lại danh mục đầu tư của mình:")]),
                html.P(" 1. Bạn có thể bán các khoản đầu tư mà tài sản nắm giữ của bạn vượt quá tỷ trọng và sử dụng số tiền thu được để mua các khoản đầu tư cho các loại tài sản bị thiếu tỷ trọng"),
                html.P(" 2.Bạn có thể mua các khoản đầu tư mới cho các loại tài sản thiếu trọng số."),
                html.P(" 3.Nếu bạn đang tiếp tục thêm vào các khoản đầu tư của mình, bạn có thể thay đổi các khoản đóng góp của mình để nhiều hơn nữa được chuyển vào các danh mục tài sản thiếu trọng lượng cho đến khi danh mục đầu tư của bạn cân bằng trở lại.")
            ], className="mt-4"),
        
        
], style={'margin-left': '100px','margin-right': '100px','margin-top': '50px','margin-bottom': '50px','text-align':'justify'})
            
