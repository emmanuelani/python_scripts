import dash # used to create web apllications
# import dash_html_components as html 
from dash import html # gives you access to html components \
# import dash_core_components as dcc
from dash import dcc

# create a dash application
app = dash.Dash()

# Get the layout of the application and adjust it.
# This is the division in our layout and from here we will add elements to teh page
app.layout = html.Div([
              # Title to our application using HTML, H1 component
              html.H1('Data Visualization in Python', 
              # adding a css style using style parameter which takes input through dictionary
              style={'color':'blue', 'fontSize':40,
                      'border-style': 'outset'
                }),
              # Adding dropdown
              html.Label('Dropdown'),
              dcc.Dropdown(
              options=[
                  {'label': 'Option 1', 'value': '1'},
                  {'label': 'Option 2', 'value': '2'},
                  {'label': 'Option 3', 'value': '3'},
              ], 
              value='3'),
              # Adding Slider
              dcc.Slider(
              min=0,
              max=5,
              marks={i: '{}'.format(i) for i in range(5)},
              value=2),

              # Adding paragragh component inside layout division
              html.P('This video is about dash basics', 
              style={'fontSize':20
              }), 
              # Creating another division inside the application layout division
              html.Div(['This is a new division'],
              style={'color':'red', 'fontSize':40,
                      'border-style': 'double'
                })
             ],
              style={'border-style': 'ridge', 'border-color': 'yellow'})


if __name__ == '__main__':
    # Grab the application and run the server
    app.run_server(port=8002, host='127.0.0.1', debug=True)


