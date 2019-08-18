import dash
import dash_core_components as dcc
import dash_html_components as html

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
[Full history of airplane crashes throughout the world, from 1908-present.]({data_source_url})

Data details:
  - Total rows: 5268
  - Source Domain: opendata.socrata.com
  - Created: 24/06/2009, 18:35:20
""")

layout = [
    header,
    data_source_section,
]

app.layout = html.Div(layout, className='container')

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
