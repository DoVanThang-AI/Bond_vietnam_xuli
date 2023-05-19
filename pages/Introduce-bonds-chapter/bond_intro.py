from imports import *


dash.register_page(__name__, path='/gioi-thieu-ve-trai-phieu', name='Giới thiệu về trái phiếu')

layout = dbc.Row([
    html.Iframe(src="https://vi.wikipedia.org/wiki/Tr%C3%A1i_phi%E1%BA%BFu",
                style={'width':'100%','height':'100vh'}),
])
