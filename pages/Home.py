from imports import *

dash.register_page(__name__, path='/', name='Home')

layout = [
    dbc.Row([
            dbc.Col(
                
                dbc.Carousel(
                    id="carousel",
                    items=[
                        {"key": "1", "src": "/assets/1.jpg"},
                        {"key": "2", "src": "/assets/2.jpg"},
                        {"key": "3", "src": "/assets/3.jpg"}
                    ],
                    interval=5000,
                ), class_name="m-0 p-0"
            )
        ],
    ),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("Giới thiệu", className="card-title"),
                        html.P(
                            "Trang web này được xây dựng nhằm mục đích cung cấp thông tin về các quy trình, quy định, quy chế của trường Đại học Công nghiệp TP.HCM.",
                            className="card-text",
                        ),
                        dbc.Button("Xem thêm", color="primary", href="/gioi-thieu"),
                    ]
                )
            ),
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("Giới thiệu", className="card-title"),
                        html.P(
                            "Trang web này được xây dựng nhằm mục đích cung cấp thông tin về các quy trình, quy định, quy chế của trường Đại học Công nghiệp TP.HCM.",
                            className="card-text",
                        ),
                        dbc.Button("Xem thêm", color="primary", href="/gioi-thieu"),
                    ]
                )
            ),
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("Giới thiệu", className="card-title"),
                        html.P(
                            "Trang web này được xây dựng nhằm mục đích cung cấp thông tin về các quy trình, quy định, quy chế của trường Đại học Công nghiệp TP.HCM.",
                            className="card-text",
                        ),
                        dbc.Button("Xem thêm", color="primary", href="/gioi-thieu"),
                    ]
                )
            ),
        ),
    ], 
    ),

]

