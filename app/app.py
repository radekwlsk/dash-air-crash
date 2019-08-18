import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.title = "Airplane Crashes Data - Dash"
layout = [
    html.Header(children=[
        html.H1(app.title),
        html.P("Airplane crashes data visualisation project for purposes of presentation about Dash"),
    ]),

    html.Hr(),

    html.Section(children=[
            html.H2('Data Source'),
            html.A(
                'Full history of airplane crashes throughout the world, from 1908-present.',
                href='https://opendata.socrata.com/Government/Airplane-Crashes-and-Fatalities-Since-1908/q2te-8cvq'
            ),
            html.P("Data details:"),
            html.Ul(children=[
                html.Li("Total rows: 5268"),
                html.Li("Source Domain: opendata.socrata.com"),
                html.Li("Created: 24/06/2009, 18:35:20"),
            ])
    ]),
]

app.layout = html.Div(layout, className='container')

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
