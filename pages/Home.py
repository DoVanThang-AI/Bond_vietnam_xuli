from imports import *

dash.register_page(__name__, path="/", name="Home")
IUH_LOGO='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Logo_IUH.png/800px-Logo_IUH.png'


layout = [
    dbc.Row(
        [
            dbc.Container(
                [
                    html.Img(src=IUH_LOGO, height="80px"),

                    html.H1(
                        "HỆ THỐNG THÔNG TIN",
                        className="align-self-center",
                        style={
                            "font-size": "3rem",
                            "font-weight": "700",
                            "color": "#212A3E",
                        },
                    ),
                    html.H1(
                        "VÀ ĐỊNH GIÁ TRÁI PHIẾU VIỆT NAM",
                        className="align-self-center",
                        style={
                            "font-size": "3rem",
                            "font-weight": "700",
                            "color": "#212A3E",
                        },
                    ),
                    html.H6(
                        "Hệ thống thông tin và định giá trái phiếu Việt Nam!",
                        className="font-weight-normal text-muted pb-3",
                        style={"font-weight": "300"},
                    ),
                    html.Div(
                        [
                            dbc.Button(
                                "About us",
                                id="about-us-btn",
                                className="me-2",
                                color="secondary",
                                href="#about-us",
                            ),
                            dbc.Button(
                                "Help",
                                id="help-button",
                                className="me-2",
                                color="secondary",
                                href="#help",
                            ),
                        ]
                    ),
                    html.Img(src="/assets/Group171.svg", className="img-fluid"),
                ],
                className="d-flex flex-column justify-content-center align-items-center",
            )
        ],
        style={"background-color": "#F1F6F9", "height": "100vh"},
        id="banner",
    ),
    dbc.Row(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            html.H1(
                                "About this project...",
                                style={"font-size": "3rem", "font-weight": "800"},
                            ),
                            html.H6(
                                "\"",
                                style={"font-weight": "800", 'font-size':'3rem'},
                            ),
                            html.H6(
                                "Khóa luận này tập trung vào việc xây dựng một giao diện điều khiển tiên tiến cho việc theo dõi trái phiếu Việt Nam. Được thiết kế để cung cấp những thông tin chi tiết và chính xác nhất về trái phiếu, giao diện này không chỉ giúp người dùng có thể dễ dàng theo dõi thông tin về lãi suất, giá trị và thời hạn đáo hạn, mà còn cho phép họ tương tác với dữ liệu này một cách chủ động và hiệu quả hơn bao giờ hết. Bên cạnh đó, đồ án cũng tập trung vào việc giải quyết các thách thức phức tạp liên quan đến việc đầu tư vào trái phiếu Việt Nam, giúp các nhà đầu tư và các công ty tài chính có thể đưa ra các quyết định đúng đắn hơn. Với khả năng cung cấp được những thông tin chi tiết, giao diện điều khiển được thiết kế để đáp ứng các yêu cầu khắt khe của người sử dụng, giúp họ có thể dễ dàng tiếp cận và nắm bắt được bức tranh toàn diện về thị trường trái phiếu Việt Nam. Từ đó, họ có thể tạo ra các chiến lược đầu tư thông minh và hiệu quả, đồng thời giảm thiểu các rủi ro tiềm ẩn trong quá trình đầu tư.",
                                className="font-weight-normal text-muted pb-3",
                                style={"font-weight": "300"},
                            ),
                            html.H6(
                                "\"",
                                className="font-weight-normal text-muted pb-3",
                                style={"font-weight": "800", 'font-size': '3rem', 'text-align': 'right'},
                            ),
                        ],
                        className="mb-5 mt-5",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="/assets/building.gif",
                                            top=True,
                                            style={"height": "5rem", "width": "5rem"},
                                            className="align-self-center",
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H4(
                                                    "Giới thiệu về trái phiếu",
                                                    className="card-title",
                                                    style={
                                                        "font-size": "2rem",
                                                        "font-weight": "600",
                                                    },
                                                ),
                                                html.P(
                                                    "Đây là giao diện cho thanh công cụ tiên với mục thị trường trái phiếu là gì? Bao gồm các thông tin và hình ảnh mô tả cho người dùng những thông tin liên quan đến những thông tin cần thiết cho người dùng mới tiếp cận đến trái phiếu, đặc điểm của trái phiếu. ",
                                                    className="card-text",
                                                ),
                                            ],
                                            style={
                                                "border": "none",
                                                "text-align": "center",
                                            },
                                        ),
                                        dbc.CardLink(
                                            "Xem thêm",
                                            href="/gioi-thieu-ve-trai-phieu",
                                            style={
                                                "color": "#007bff",
                                                "text-align": "center",
                                            },
                                            className="mt-3 p-3",
                                        ),
                                    ],
                                ),
                                className="p-5",
                            ),
                            dbc.Col(
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="/assets/presentation.gif",
                                            top=True,
                                            style={"height": "5rem", "width": "5rem"},
                                            className="align-self-center",
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H4(
                                                    "Định giá trái phiếu",
                                                    className="card-title",
                                                    style={
                                                        "font-size": "2rem",
                                                        "font-weight": "600",
                                                    },
                                                ),
                                                html.P(
                                                    "Giao diện tính toán và biểu diễn trên Dashboard được thiết kế nhằm cung cấp các công cụ và chức năng hỗ trợ trong việc tính toán và biểu diễn thông tin liên quan đến trái phiếu. Giao diện này nhằm giúp người dùng dễ dàng thao tác và tìm hiểu các thông tin quan trọng về trái phiếu một cách trực quan và thuận tiện.",
                                                    className="card-text",
                                                ),
                                            ],
                                            style={
                                                "border": "none",
                                                "text-align": "center",
                                            },
                                        ),
                                        dbc.CardLink(
                                            "Xem thêm",
                                            href="/bonds-analysis/dashboard-analysis",
                                            style={
                                                "color": "#007bff",
                                                "text-align": "center",
                                            },
                                            className="mt-3 p-3",
                                        ),
                                    ],
                                ),
                                className="p-5",
                            ),
                            dbc.Col(
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="/assets/document.gif",
                                            top=True,
                                            style={"height": "5rem", "width": "5rem"},
                                            className="align-self-center",
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H4(
                                                    "Trung tâm truyền thông",
                                                    className="card-title",
                                                    style={
                                                        "font-size": "2rem",
                                                        "font-weight": "600",
                                                    },
                                                ),
                                                html.P(
                                                    "Trung tâm truyền thông trái phiếu là nguồn thông tin đáng tin cậy và toàn diện về thị trường trái phiếu. Mục tiêu giúp độc giả hiểu rõ hơn về trái phiếu và cung cấp thông tin cập nhật về thị trường.",
                                                    className="card-text",
                                                ),
                                            ],
                                            style={
                                                "border": "none",
                                                "text-align": "center",
                                            },
                                        ),
                                        dbc.CardLink(
                                            "Xem thêm",
                                            href="/bond-news",
                                            style={
                                                "color": "#007bff",
                                                "text-align": "center",
                                            },
                                            className="mt-3 p-3",
                                        ),
                                    ],
                                ),
                                className="p-5",
                            ),
                        ],
                        id="about-us",
                    ),
                ],
                className="p-5",
            ),
        ]
    ),
    dbc.Row([
        dbc.Container(
                [
                    dbc.Row(
                        [
                            html.H1(
                                "About us",
                                style={"font-size": "3rem", "font-weight": "800", "text-align": "center"},
                            ), 
                            
                        ],
                        className="mb-5 mt-5",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="/assets/viet_avatar.jpg",
                                            top=True,
                                            style={"height": "20rem", "width": "20rem", "border-radius": "50%"},
                                            className="align-self-center",
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H4(
                                                    "Phan Lê Hoàng Việt",
                                                    className="card-title mt-3",
                                                    style={
                                                        "font-size": "2rem",
                                                        "font-weight": "600",
                                                    },
                                                ),
                                                html.P(
                                                    "MSSV: 19512321",
                                                    className="card-text p-3",
                                                ),
                                            ],
                                            style={
                                                "border": "none",
                                                "text-align": "center",
                                            },
                                        ),
                                        dbc.CardLink(
                                            "FACEBOOK",
                                            href="https://www.facebook.com/phanlehoangviet/",
                                            style={
                                                "color": "#007bff",
                                                "text-align": "center",
                                            },
                                            className="mt-3 p-3",
                                        ),
                                    ],  className="p-3",
                                ),
                                className="p-5",
                            ),
                            dbc.Col(
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="/assets/thang_avatar.jpg",
                                            top=True,
                                            style={"height": "20rem", "width": "20rem", "border-radius": "50%"},
                                            className="align-self-center",
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H4(
                                                    "Đỗ Văn Thắng",
                                                    className="card-title mt-3",
                                                    style={
                                                        "font-size": "2rem",
                                                        "font-weight": "600",
                                                    },
                                                ),
                                                html.P(
                                                    "MSSV: 19469481",
                                                    className="card-text p-3",
                                                ),
                                            ],
                                            style={
                                                "border": "none",
                                                "text-align": "center",
                                            },
                                        ),
                                        dbc.CardLink(
                                            "FACEBOOK",
                                            href="https://www.facebook.com/profile.php?id=100009525892037",
                                            style={
                                                "color": "#007bff",
                                                "text-align": "center",
                                            },
                                            className="mt-3 p-3",
                                        ),
                                    ], className="p-3",
                                ),
                                className="p-5",
                            ),
                            
                        ],
                        id="about-us",
                    ),
                ],
                className="p-5",
            ),
    ], style={"background-color": "#394867"}),
]
