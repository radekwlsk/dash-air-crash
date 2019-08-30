import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import socrata

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "Airplane Crashes Data - Dash"

header = html.Header(children=[
    html.H1(app.title),
    html.P("Airplane crashes data visualisation project for purposes of presentation about Dash"),
])

data_source_url = 'https://opendata.socrata.com/Government/Airplane-Crashes-and-Fatalities-Since-1908/q2te-8cvq'
data_source_section = html.Section(
    children=[
        dcc.Markdown(f"""
            ## Data Source
            [Full history of airplane crashes throughout the world, from 1908-2009.]({data_source_url})
            
            Data details:
              - Total rows: 5268
              - Source Domain: opendata.socrata.com
              - Created: 24/06/2009, 18:35:20
        """)
    ],
    id='data-source'
)

df = socrata.get_air_crashes(limit=6000)
accidents_df = df.groupby(['year']).size().reset_index(name='accidents')
fatalities_df = df.groupby(['year'])['fatalities'].sum().reset_index(name='fatalities')


data_year_summary_graph = dcc.Graph(
    figure=go.Figure(
        data=[
            go.Bar(
                x=accidents_df['year'],
                y=accidents_df['accidents'],
                name='Accidents',
                hovertemplate='%{y}',
                yaxis='y',
            ),
            go.Scatter(
                x=fatalities_df['year'],
                y=fatalities_df['fatalities'],
                name='Fatalities',
                hovertemplate='%{y}',
                mode='lines',
                yaxis='y2',
            )
        ],
        layout=go.Layout(
            title='Accidents and total fatalities',
            yaxis=dict(title='accidents', gridcolor='lightgrey'),
            yaxis2=dict(title='fatalities', overlaying='y', side='right'),
            showlegend=False,
            hovermode='x',
            font=dict(
                family='sans-serif',
                color='#000'
            ),
            colorway=["#333333", "#10C10C"],
            plot_bgcolor="white"
        )
    ),
    config=dict(displayModeBar=False)
)
data_visualization_section = html.Section(
    children=[
        html.H2("Data visualization"),
        data_year_summary_graph,
    ],
    id='data-visualization-section'
)

air_crash_table = dash_table.DataTable(
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
    style_as_list_view=True,
    page_size=20,
)

layout = [
    header,
    html.Div(children=[
        data_source_section,
        air_crash_table,
        data_visualization_section,
    ]),
]
app.layout = html.Div(layout, className='container')

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
