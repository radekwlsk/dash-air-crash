import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


from utils.dash_utils import range_to_marks


def data_year_summary_graph(df):
    accidents_df = df.groupby(['year']).size().reset_index(name='accidents')
    fatalities_df = df.groupby(['year'])['fatalities'].sum().reset_index(name='fatalities')

    return dcc.Graph(
        id='data-visualization-summary-graph',
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


def crash_locations_map(df):
    df['text'] = df['location'] + '<br>' + df['date'] + '<br>Fatalities: ' + df['fatalities'].astype(str)
    min_y = min(df["year"])
    max_y = max(df["year"])

    return dcc.Graph(
        id='data-visualization-location-map',
        figure=go.Figure(
            data=go.Scattergeo(
                lat=df["latitude"],
                lon=df["longitude"],
                marker=dict(
                    # size=df['fatalities'],
                    color=df["year"],
                    line_color='rgb(40,40,40)',
                    line_width=0.5,
                    opacity=0.8,
                    sizemode='area'
                ),
                text=df["text"],
                # projection="equirectangular",
                # marker_size=df["fatalities"]/10,
            ),
            layout=go.Layout(
                title=f'Crash sites in years {min_y}-{max_y} (colored by year)',
                showlegend=False,
                font=dict(
                    family='sans-serif',
                    color='#000'
                ),
                margin=dict(
                    l=10,
                    r=10,
                    b=0,
                    t=50,
                ),
                width=920,
                height=None,
                geo=dict(
                    scope='world',
                    landcolor="#10C10C",
                    countrycolor="#333333",
                    coastlinecolor="#333333",
                    resolution=110,
                    showcountries=True,
                    showframe=False,
                    uirevision='world',
                ),
                plot_bgcolor="white"
            )
        ),
        config=dict(displayModeBar=False),
        style={'margin': 'auto'}
    )


def data_visualization_section(df):
    min_y = min(df["year"])
    max_y = max(df["year"])
    return html.Section(
        children=[
            html.H2("Data visualization"),
            data_year_summary_graph(df),
            html.Div(
                children=[
                    crash_locations_map(df),
                    html.Div(
                        children=[
                            dcc.RangeSlider(
                                step=1,
                                min=min(df["year"]),
                                max=max(df["year"]),
                                marks=range_to_marks(min_y, max_y, 20),
                                value=(min_y, max_y),
                                id='data-visualization-location-map-year-slider'
                            ),
                            dcc.Dropdown(
                                id='data-visualization-location-map-year-scope',
                                options=[
                                    dict(label=scope.title(), value=scope)
                                    for scope in ['world', 'usa', 'europe']
                                ],
                                value='world',
                                multi=False,
                                clearable=False,
                            )
                        ],
                        style={'width': '80%', 'margin': 'auto'}
                    )
                ]
            )
        ],
        id='data-visualization-section'
    )
