import dash
import dash_html_components as html

from utils import socrata
from layouts import data_source_section, data_visualization_section

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "Airplane Crashes Data - Dash"

header = html.Header(children=[
    html.H1(app.title),
    html.P("Airplane crashes data visualisation project for purposes of presentation about Dash"),
])

app.df = socrata.get_air_crashes(limit=6000)

layout = [
    header,
    html.Div(children=[
        data_source_section(),
        data_visualization_section(app.df),
    ]),
]
app.layout = html.Div(layout, className='container')

from callbacks import *

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
