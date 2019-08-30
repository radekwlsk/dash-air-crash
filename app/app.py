import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

from utils import socrata

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "Airplane Crashes Data - Dash"

header = html.Header(children=[
    html.H1(app.title),
    html.P("Airplane crashes data visualisation project for purposes of presentation about Dash"),
])

data_source_url = 'https://opendata.socrata.com/Government/Airplane-Crashes-and-Fatalities-Since-1908/q2te-8cvq'
data_source_section = dcc.Markdown(f"""
## Data Source
[Full history of airplane crashes throughout the world, from 1908-2009.]({data_source_url})

Data details:
  - Total rows: 5268
  - Source Domain: opendata.socrata.com
  - Created: 24/06/2009, 18:35:20
""")

df = socrata.get_air_crashes(limit=None)
air_crashed_table = dash_table.DataTable(
    id='air-crash-table',
    columns=[
        {
            "name": "Date",
            "id": "date",
            "type": 'datetime',
        },
        {
            "name": "Location",
            "id": "location",
        },
        {
            "name": "Route",
            "id": "route",
        },
        {
            "name": "Passengers",
            "id": "aboard",
            "type": 'numeric',
        },
        {
            "name": "Fatalities",
            "id": "fatalities",
            "type": 'numeric',
        },
        {
            "name": "Registration",
            "id": "registration",
        },
        {
            "name": "Operator",
            "id": "operator",
        },
    ],
    data=df.to_dict('records'),
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    style_table={'overflowX': 'scroll'},
    style_cell={
        'minWidth': '80px', 'maxWidth': '180px',
        'whiteSpace': 'normal',
        'textAlign': 'center',
        'fontFamily': 'sans-serif',
        'fontSize': '0.9em'
    },
    # style_as_list_view=True,
    page_size=20,
)

layout = [
    header,
    html.Div(children=[
        data_source_section,
        air_crashed_table,
    ]),
]
app.layout = html.Div(layout, className='container')

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
