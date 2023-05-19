from imports import *

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True, assets_url_path='assets', )

# nav contents
IUH_LOGO='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Logo_IUH.png/800px-Logo_IUH.png'

nav_contents = []
for i, page in enumerate(dash.page_registry.values()):
    print(i, page['name'], page["relative_path"])
    nav_contents.append(dbc.NavItem(dbc.NavLink(page['name'], href=page["relative_path"], active=True, style={'color':'#212A3E'})))

pages = list(dash.page_registry.values())


   

# navbar 
navBar = dbc.Navbar(
    dbc.Container(
        [
              
            html.A(
                dbc.Row([
                        dbc.Col(html.Img(src=IUH_LOGO, height="80px")),
                        dbc.Col(dbc.NavbarBrand("VN-IUH Bonds", className=" ms-2", style={'font-weight':'1700', 'text-align':'center','font-size':'20px', 'color':'#212A3E'}), className="ml-2"),
                    ],

                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            
                            [
                                dbc.NavItem(nav_contents[0]),
                                dbc.NavItem(dbc.DropdownMenu(
                                    [
                                        dbc.DropdownMenuItem(pages[1]['name'], href=pages[1]['relative_path']),
                                        dbc.DropdownMenuItem(pages[2]['name'], href=pages[2]['relative_path']),
                                        dbc.DropdownMenuItem(pages[3]['name'], href=pages[3]['relative_path']),
                                    ],
                                    label="Giới thiệu",
                                    nav=True,
                                    toggle_style={"color": "#212A3E",
                                                  'font-weight':'1200',},
                                ), ),
                                
                                dbc.DropdownMenu(
                                    [
                                        dbc.DropdownMenuItem(pages[4]['name'], href=pages[4]['relative_path']),
                                        dbc.DropdownMenuItem(pages[5]['name'], href=pages[5]['relative_path']),
                                        dbc.DropdownMenuItem(pages[6]['name'], href=pages[6]['relative_path']),
                                    ],
                                    nav=True,
                                    label="Tin tức",
                                    toggle_style={"color": "#212A3E", "font-weight": "1200"}
                                ),
                                dbc.DropdownMenu(
                                    [
                                        dbc.DropdownMenuItem(pages[7]['name'], href=pages[7]['relative_path']),
                                        dbc.DropdownMenuItem(pages[8]['name'], href=pages[8]['relative_path']),
                                    ],
                                    nav=True,
                                    label="Dashboard",
                                    toggle_style={"color": "#212A3E", "font-weight": "1200"},

                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto"
                                ),
                                dbc.NavItem(dbc.NavLink("Help", style={'color':'#212A3E', 'font-weight':'1200'})),
                                dbc.NavItem(dbc.NavLink("About", style={'color':'#212A3E', 'font-weight':'1200'})),
                                
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100 align-items-center",                        

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
    color="#F1F6F9",
    className="pt-3 pb-3",
    
    
)

footer = dbc.Row(
            [
                dbc.Col([
                    html.H6('About',style={'color':'white'}),
                    html.P("This is a website that provides information on Vietnamese bonds and is calculated with many statistics so that investors can give investment advice to reduce financial risks.",style={'color':'white'})

                    
                ],className="col-3"),
                #dich vu
                dbc.Col([
                    html.H6("Dịch vụ",style={'color':'white'}),
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
                    html.H6("Tin tức"),
                    html.A('Event activities', href='https://www.hnx.vn/tin-tuc-su-kien-hnx.html',target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.A('Social activities', href='https://www.hnx.vn/tin-tuc-su-kien-hdxh.html',target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),


                ],className="col-3"),
                #   Ketnoi
                dbc.Col([
                    html.H6("Về chúng tôi"),
                    html.A('Gmail',  href="mailto:contact@example.com",target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),
                    html.A('Twitter', href="https://twitter.com/",target="_blank",style={'font-size':'10px','text-align':'center'}),
                    html.Hr(style={'margin': '5px 0px 0px 0px'}),

                    html.P('Address',style={'font-size':'10px','font-weight':'500'}),
                    html.P('12 Nguyễn Văn Bảo, Phường 4, Gò Vấp, Thành phố Hồ Chí Minh',style={'font-size':'10px','font-weight':'500'}),
                    html.P("telephone: (+84) 769803053",style={'font-size':'10px','font-weight':'500','color':'red'})
                ],className="col-3")
], class_name="p-4")

app.layout = dbc.Container(
        [   
            # header container
            dbc.Container(navBar, fluid=True, className='p-0 m-0'), 


            # page container
            dbc.Container(dash.page_container, fluid=True, className='p-0 m-0'),


            # footer container
            html.Footer(dbc.Container(footer, fluid=True, className='p-0 m-0'))

        ], fluid=True, className='p-0 m-0'
)

    
if __name__ == '__main__':
    app.run_server(debug=False)

app.clientside_callback(
    """
    function(clicks, elemid) {
        document.getElementById(elemid).scrollIntoView({
          behavior: 'smooth'
        });
    }
    """,
    Output('garbage-output-0', 'children'),
    [Input('about-us-btn', 'n_clicks')],
    [State('about-us', 'id')]
)