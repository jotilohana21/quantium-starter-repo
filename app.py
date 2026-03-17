from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash(__name__)

# 1. Load and prepare the data
df = pd.read_csv('formatted_data.csv')
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# 2. Define the App Layout with Professional Styling (The "Dressing Up" part)
app.layout = html.Div(style={
    'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 
    'backgroundColor': '#f2f2f2', 
    'padding': '40px', 
    'minHeight': '100vh'
}, children=[
    
    # White card container to make the dashboard look like a modern app
    html.Div(style={
        'backgroundColor': 'white', 
        'padding': '30px', 
        'borderRadius': '15px', 
        'boxShadow': '0px 4px 12px rgba(0,0,0,0.1)',
        'maxWidth': '1100px',
        'margin': 'auto'
    }, children=[
        
        html.H1(
            children='Pink Morsel Sales Visualiser',
            style={'textAlign': 'center', 'color': '#1a2a6c', 'marginBottom': '10px'}
        ),

        html.Div(style={'textAlign': 'center', 'padding': '20px'}, children=[
            html.Label("Select Region: ", style={'fontWeight': 'bold', 'fontSize': '18px', 'marginRight': '15px'}),
            
            # The Radio Buttons with all 5 required options
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all', # Default starting value
                inline=True,
                labelStyle={'marginRight': '15px', 'cursor': 'pointer'}
            )
        ]),

        # The Visualisation component
        dcc.Graph(id='sales-line-chart')
    ])
])

# 3. Callback to handle the interactivity
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter the data based on user selection
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    # Generate the updated line chart
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales Trend - {selected_region.capitalize()} Region",
        labels={"date": "Transaction Date", "sales": "Total Sales (USD)"},
        color_discrete_sequence=["#1a2a6c"] # Professional blue color
    )
    
    # Smooth transition for better user experience
    fig.update_layout(transition_duration=500)
    return fig

# 4. Run the server
if __name__ == '__main__':
    app.run(debug=True)