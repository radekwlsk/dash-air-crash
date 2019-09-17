import dash_core_components as dcc
import dash_html_components as html

data_source_url = 'https://opendata.socrata.com/Government/Airplane-Crashes-and-Fatalities-Since-1908/q2te-8cvq'


def data_source_section():
    return html.Section(
        children=[
            dcc.Markdown(f"""
                ## Data Source
                [Full history of airplane crashes throughout the world, from 1908-2009.]({data_source_url})
    
                Data details:
                  - Total rows: 5268
                  - Source Domain: opendata.socrata.com
                  - Created: 24/06/2009, 18:35:20
            """),
            html.Button("Show data", id='data-source-table-button'),
            html.Div(id='data-source-table-div'),
        ],
        id='data-source'
    )
