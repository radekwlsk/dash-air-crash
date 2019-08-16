import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Airplane Crashes Data - Dash'),

    html.Div(children='''
        Airplane crashes data visualisation project for purposes of presentation about Dash
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)
