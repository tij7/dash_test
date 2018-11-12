from sense_hat import SenseHat
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()
sense = SenseHat();

app.layout = html.Div(children=[
    html.Div(children='''
        Symbol to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    orientation = sense.get_orientation_degrees()

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [3, 5, 6, 1, 9], 'type': 'line', 'name': orientation},
            ],
            'layout': {
                'title': str(orientation)
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)
