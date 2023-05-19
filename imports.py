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
from scipy.optimize import newton

# from pages.Calculator_index import ytm_layout

from dash import dash_table
from dash.dash_table.Format import Group
from utils.funtions_cal import Yield_to_marturity,laisuat,df_modified,Data_table
from utils.Cal_index_ import ytm_layout,duration_bond, yield_to_call