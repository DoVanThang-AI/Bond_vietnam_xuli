import pandas as pd
import numpy as np
import plotly.express as px
import datetime as dt
import dash
from dash import dcc
from dash import html, callback
from dash.dependencies import Input, Output,State
import scipy as sp
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import plotly.io as pio
import dash_extensions as de
import dash_table
from scipy.optimize import newton
from pages.Home import home_layout
from pages.page1 import page_1_layout
from pages.page2 import page_2_layout
from pages.page3 import page_3_layout
from pages.page4 import page_4_layout
from pages.page5 import page_5_layout
from pages.page6 import page_6_layout
from pages.pages_7 import page_7_layout
from pages.page8 import page_8_layout
# from pages.Calculator_index import ytm_layout

