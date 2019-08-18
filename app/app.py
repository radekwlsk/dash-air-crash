import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.title = "Airplane Crashes Data - Dash"

colors = {
    'text': '#333333',
    'title': '#10C10C'
}

header = html.Header(children=[
    html.H1(app.title),
    html.P("Airplane crashes data visualisation project for purposes of presentation about Dash"),
], style={
    'textAlign': 'center',
    'color': colors['title'],
})

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
    html.Hr(),
    data_source_section,
]

style = {
    'color': colors['text'],
    'width': "960px",
    'margin': "0 auto",
}
app.layout = html.Div(layout, className='container', style=style)

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
