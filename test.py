from sense_hat import SenseHat
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output

app = dash.Dash()
sense = SenseHat();
sense.set_imu_config(True, True, True)  # gyroscope only

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
    acc = sense.get_accelerometer_raw()
    z = acc['z']
    y = acc['y']
    x = acc['x']
    
    angle = np.arctan2(np.sqrt(x**2 + y**2), z) * 180 / np.pi

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [3, 5, 6, 1, 9], 'type': 'line', 'name': angle},
            ],
            'layout': {
                'title': str(angle)
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port = 8050)
