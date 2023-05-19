from imports import *

dash.register_page(__name__, path="/", name="Home")


layout = [
    dbc.Row(
        [
            dbc.Container(
                [
                    html.H1(
                        "HỆ THỐNG THÔNG TIN",
                        className="align-self-center",
                        style={"font-size": "3rem", "font-weight": "900"},
                    ),
                    html.H1(
                        "VÀ ĐỊNH GIÁ TRÁI PHIẾU VIỆT NAM",
                        className="align-self-center",
                        style={"font-size": "3rem", "font-weight": "900"},
                    ),
                    html.H6(
                        "Hệ thống thông tin và định giá trái phiếu Việt Nam!",
                        className="font-weight-normal text-muted pb-3",
                         style={ "font-weight": "300"}
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
                    html.Img(src="/assets/6.svg", className="img-fluid"),
                ],
                className="d-flex flex-column justify-content-center align-items-center",
            )
        ],
        style={"background-color": "#F1F6F9", 'height': '100vh'},
        id="banner",
    ),
    dbc.Container(
        [
            dbc.Row([
                html.H1(
                        "About this project...",
                        style={"font-size": "3rem", "font-weight": "800"},
                    ),
                
                html.H6(
                    "Hệ thống thông tin và định giá trái phiếu Việt Nam!",
                    className="font-weight-normal text-muted pb-3",
                ),
                
            ], className="mb-5 mt-5"),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(src="/assets/building.gif", top=True, style={'height': '5rem', 'width': '5rem'}, className='align-self-center'),
                                dbc.CardBody(
                                    [
                                        html.H4("Giới thiệu về trái phiếu", className="card-title", style={'font-size':'2rem', 'font-weight':'600'}),
                                        html.P(
                                            "Some quick example text to build on the card title and "
                                            "make up the bulk of the card's content.",
                                            className="card-text", 
                                        ),
                                        dbc.CardLink("External link", href="https://google.com"),
                                    ], style={'border':'none', 'text-align':'center'}
                                ),
                            ],
                        )
                    ),
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(src="/assets/presentation.gif", top=True, style={'height': '5rem', 'width': '5rem'}, className='align-self-center'),
                                dbc.CardBody(
                                    [
                                        html.H4("Dashboard Trái Phiếu", className="card-title", style={'font-size':'2rem', 'font-weight':'600'}),
                                        html.P(
                                            "Some quick example text to build on the card title and "
                                            "make up the bulk of the card's content.",
                                            className="card-text", 
                                        ),
                                        dbc.CardLink("External link", href="https://google.com"),
                                    ], style={'border':'none', 'text-align':'center'}
                                ),
                            ],
                        )
                    ),
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(src="/assets/document.gif", top=True, style={'height': '5rem', 'width': '5rem'}, className='align-self-center'),
                                dbc.CardBody(
                                    [
                                        html.H4("Trung tâm truyền thông", className="card-title", style={'font-size':'2rem', 'font-weight':'600'}),
                                        html.P(
                                            "Some quick example text to build on the card title and "
                                            "make up the bulk of the card's content.",
                                            className="card-text", 
                                        ),
                                        dbc.CardLink("External link", href="https://google.com"),
                                    ], style={'border':'none', 'text-align':'center'}
                                ),
                            ],
                        )
                    ),
                ], id="about-us"
            ),
            
        ],
        className="p-5",
        style={'height': '100vh'}
    ),
]

