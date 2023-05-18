

from imports import *

dash.register_page(__name__, path='/bond-news/bao-cao-thi-truong-trai-phieu', name='Báo cáo thị trường trái phiếu')

layout = html.Div([
    dbc.Container([
    
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