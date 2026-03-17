from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash(__name__)

# 1. Load and process the data
df = pd.read_csv('formatted_data.csv')
# Important: Convert date column to datetime objects and sort them
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# 2. Create the line chart with labels
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Performance (Pre & Post Price Increase)",
    labels={"date": "Transaction Date", "sales": "Total Sales (USD)"} # Axis labels
)

# 3. Define the app layout (The Header and the Graph)
app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods: Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    html.Div(
        children='Analysis of sales before and after the price increase on Jan 15, 2021.',
        style={'textAlign': 'center', 'marginBottom': '30px'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 4. Run the server
if __name__ == '__main__':
    app.run(debug=True)