import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Airplane Crashes Data - Dash'),

    html.Div(children='''
        Airplane crashes data visualisation project for purposes of presentation about Dash
    '''),
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
