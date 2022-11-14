# ***************************************
# Imports
# ***************************************
# Dash
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Plotly
import plotly.express as px
import plotly.graph_objects as go

# ***************************************
# Get data
# ***************************************
import datamodel
df_employees_sale = datamodel.get_data()
df_year = datamodel.get_year()

# ***************************************
# Diagram - Employee Sales
# ***************************************
fig_employee = px.bar(df_employees_sale, 
    x='Employee', y='Total', barmode='group',
    color='Employee', title='Sales by Employee')

# ***************************************
# Activate the app
# ***************************************
#app = dash.Dash(__name__)

dash_app = dash.Dash(__name__)
app = dash_app.server

# ***************************************
# Layout
# ***************************************
dash_app.layout = html.Div(
    children=[
        html.Div(className='row',
                children=[
                    html.Div(className='four columns div-user-controls',
                            children=[
                                html.H2('Salgs dashboard - Employee'),
                                html.P('Vælg år fra dropdown'),
                    html.Div(children="Aar", className="menu-title"),
                            dcc.Dropdown(
                                id='drop_year',
                                options=[{'label':selectyear, 'value':selectyear} for selectyear in df_year['order_year']]
                            ),
                            ]
                    ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                dcc.Graph(id="sales_employee", figure=fig_employee)
                            ]
                    ),
                ]
            )
        ]
)

# ***************************************
# Callbacks
# ***************************************
# Output er Diagrammet
# Input er DropDown
@dash_app.callback(Output('sales_employee', 'figure'),
              [Input('drop_year', 'value')])

def update_graph(drop_year):
    order_fig1 = df_employees_sale.loc[(df_employees_sale['order_year'] == drop_year)]
        
    return {'data':[go.Bar(
        x = order_fig1['Employee'],
        y = order_fig1['Total']
            )
        ]
    }

# ***************************************
# Run the app
# ***************************************
if __name__ == '__main__':
    dash_app.run_server(debug=True)