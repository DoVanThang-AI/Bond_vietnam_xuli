from imports import *

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id = 'url', refresh=False),
    html.Div(id='page-content')
])

#Define the callback to update the page content based on the URL
@app.callback(Output('page-content','children'),
              [Input('url','pathname')])

def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-4':
        return page_4_layout
    elif pathname == '/page-5':
        return page_5_layout
    elif pathname == '/page-6':
        return page_6_layout
    elif pathname == '/page-7':
        return page_7_layout
    elif pathname == '/page-8':
        return page_8_layout
    else:
        return '404 - Page not found'
if __name__ == '__main__':
    app.run_server(debug=True)
	