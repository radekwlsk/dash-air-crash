import dash_table
from dash.dependencies import Output, Input

from app import app


def air_crash_table(df):
    return dash_table.DataTable(
        id='air-crash-table',
        columns=[
            {"name": "Date", "id": "date", "type": 'datetime'},
            {"name": "Location", "id": "location"},
            {"name": "Route", "id": "route"},
            {"name": "Passengers", "id": "aboard", "type": 'numeric'},
            {"name": "Fatalities", "id": "fatalities", "type": 'numeric'},
            {"name": "Registration", "id": "registration"},
            {"name": "Operator", "id": "operator"},
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


@app.callback(
    Output('data-source-table-div', 'children'),
    [Input('data-source-table-button', 'n_clicks')])
def show_data_graph(n_clicks):
    if n_clicks and n_clicks % 2:
        return air_crash_table(app.df)
    else:
        return []


@app.callback(
    Output('data-source-table-button', 'children'),
    [Input('data-source-table-div', 'children')])
def show_data_graph(children):
    if children:
        return "Hide data"
    else:
        return "Show data"
