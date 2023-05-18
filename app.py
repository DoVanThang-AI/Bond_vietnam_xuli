from imports import *

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True, assets_url_path='./assets/')

#    dbc.Row([
#         dbc.Col([
#             html.Img(src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Logo_IUH.png/800px-Logo_IUH.png",style={'height':'150px','width':'300px'})     
#         ],className="col-4"),
#         dbc.Col([ 
#             html.Br(),
#             # html.P("Viet Nam Bonds",style={'font-weight':'1000', 'text-align':'center','font-size':'80px'}),
#         ],className="col-5"),
#         # dbc.Col([
#         #     html.Div(de.Lottie(options=options, width="35%", height="25%", url=url))
#         # ],className='col-3')
        
#     ],style={'background-image':'url(https://vnn-imgs-f.vgcloud.vn/2019/09/27/17/19.jpg)'}),
#     html.Nav(
#     [
#         html.Ul(
#             [
#                 html.Li([
#                     html.A("Giới Thiệu Về trái phiếu", href="/",style={'font-size':'15px'}),
#                     html.Ul([
#                         dbc.Card([
#                             dbc.CardBody([
#                                 html.H5("Bắt đầu giới thiệu"),
#                                 html.Li(dcc.Link("1.Thị Trường trái phiếu là gì?", href="/",style={'font-size':'12px'})),
#                                 html.Li(dcc.Link("2.Phân bổ tài sản", href="/page-2",style={'font-size':'12px'})),
#                                 html.Li(dcc.Link("3.Tổng quan định giá trái phiếu", href="/page-3",style={'font-size':'12px'})),
#                             ])
#                         ],style={'background-color':'#00325b'}),
#                         ],className="submenu")
#                 ],className="has-submenu"),
#                 html.Li(dcc.Link("Công cụ hỗ trợ & thống kê", href="/page-4",style={'font-size':'15px'})),
#                 html.Li(dcc.Link("Trung Tâm Truyền Thông", href="/page-5",style={'font-size':'15px'})),
#                 html.Li(dcc.Link("Báo cáo thị trường trái phiếu     ", href="/page-6",style={'font-size':'15px'})),
#                 html.Li(dcc.Link("Tin tức",href="/page-7",style={'font-size':'15px'}))
#             ],
#             className="navbar-nav mr-auto",
#         ),
#     ],
#     className="navbar navbar-expand-lg",
#     ),
#     html.Br(),
# nav contents
nav_contents = []
for i, page in enumerate(dash.page_registry.values()):
    print(i, page['name'], page["relative_path"])
    nav_contents.append(dbc.NavItem(dbc.NavLink(page['name'], href=page["relative_path"], active=True)))

pages = list(dash.page_registry.values())

# navbar 
navBar = dbc.Navbar(
    dbc.Container(
        [
              
            html.A(
                dbc.Row(
                    dbc.Col(dbc.NavbarBrand("VN Governance Bonds", className="ms-2")),
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(nav_contents[0]),
                                dbc.NavItem(nav_contents[1]),
                                dbc.DropdownMenu(
                                    [
                                        dbc.DropdownMenuItem(pages[2]['name'], href=pages[2]['relative_path'], header=True),
                                        dbc.DropdownMenuItem(pages[3]['name'], href=pages[3]['relative_path']),
                                        dbc.DropdownMenuItem(pages[4]['name'], href=pages[4]['relative_path']),
                                    ],
                                    nav=True,
                                    label="Tin tức trái phiếu"
                                ),

                                dbc.NavItem(nav_contents[5]),
                                dbc.NavItem(nav_contents[6]),
                                dbc.NavItem(nav_contents[7]),
                                dbc.NavItem(nav_contents[8],
                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto"
                                ),
                                dbc.NavItem(dbc.NavLink("Help")),
                                dbc.NavItem(dbc.NavLink("About")),
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                # the row should expand to fill the available horizontal space
                className="flex-grow-1", 
            )
        ],
        fluid=True,
    ),
    dark=True,
    color="#212A3E",
    
)

app.layout = dbc.Container(
        [   
            # header container
            dbc.Container(navBar, fluid=True, className='p-0 m-0'), 

            # page container
            dbc.Container(dash.page_container, fluid=True, className='p-0 m-0')

        ], style={'background-color': '#F1F6F9'}, fluid=True, className='p-0 m-0'
)

    
if __name__ == '__main__':
    app.run_server(debug=False)
	