from dash.dependencies import Output, Input, State
import plotly.graph_objs as go

from app import app


@app.callback(
    Output('data-visualization-location-map', 'figure'),
    [Input('data-visualization-location-map-year-slider', 'value'),
     Input('data-visualization-location-map-year-scope', 'value')],
    [State('data-visualization-location-map', 'figure')]
)
def filter_data_points(value, scope, figure):
    min_year, max_year = value
    df = app.df[app.df['year'].between(min_year, max_year)]

    layout = figure['layout']
    layout['title'] = f'Crash sites in years {min_year}-{max_year} (colored by year)'
    if layout['geo']['scope'] != scope:
        layout['geo']['scope'] = scope
        layout['geo']['uirevision'] = scope

    return go.Figure(
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
        layout=layout,
    )
